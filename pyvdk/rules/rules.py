from typing import Any, Callable, Dict, List, Optional, Tuple, Union
import random
import time
import re

import vbml

from ..types import Message
from .abc import ABCRule, ABCRulesBunch, RuleResult
from .bunch import RulesBunch


class Rule(ABCRule):

    def __and__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(self, rule)

    def __or__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(self, alternative_rule=rule)

    def __eq__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="eq"
        )

    def __ne__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="ne"
        )


class MessageRule(Rule):

    def check(self, obj: Message) -> Optional[RuleResult]:
        return self.ok()


class TextRule(MessageRule):
    """  """

    _text: str
    _lower: bool

    def __init__(
        self,
        text: str,
        lower: bool = True
    ) -> None:

        self._text = text.lower() if lower else text
        self._lower = lower

    def check(self, msg: Message) -> Optional[RuleResult]:
        text = msg.text

        if self._lower:
            text = text.lower()

        if text == self._text:
            return self.ok()


class RegexRule(MessageRule):
    """  """

    _regex: re.Pattern
    _fullmatch: bool

    def __init__(
        self,
        regex: Union[str, re.Pattern],
        fullmatch: bool = False
    ) -> None:

        if isinstance(regex, str):
            self._regex = re.compile(regex)
        else:
            self._regex = regex
        self._fullmatch = fullmatch

    def check(self, msg: Message) -> Optional[RuleResult]:
        if self._fullmatch:
            match = self._regex.fullmatch(msg.text)  # noqa
        else:
            match = self._regex.search(msg.text)

        if match is not None:
            return self.ok(match)


class VBMLRule(MessageRule):
    """  """

    _patcher = vbml.Patcher()
    _patterns: List[vbml.Pattern]

    def __init__(
        self,
        pattern: Union[str, List[str]],
        patcher: Optional[vbml.Patcher] = None,
        flags: Optional[re.RegexFlag] = None
    ) -> None:

        if isinstance(pattern, str):
            _patterns = [pattern]
        elif isinstance(pattern, list):
            _patterns = pattern
        else:
            _patterns = list(pattern)

        self._patterns = [vbml.Pattern(i, flags=flags) for i in _patterns]

        if patcher is not None:
            self._patcher = patcher

    def check(self, msg: Message) -> Optional[RuleResult]:
        for i in self._patterns:
            result = self._patcher.check(i, msg.text)
            if result is True:
                return self.ok()
            if isinstance(result, dict):
                return self.ok(*result.values())


class PayloadRule(MessageRule):
    def __init__(self, *payload: dict):
        self.payload = [
            i if isinstance(i, dict) else {"command": i}
            for i in payload
        ]

    def check(self, msg: Message) -> Optional[RuleResult]:
        if msg.payload in self.payload:
            return self.ok()


class PayloadContainsRule(MessageRule):
    def __init__(self, payload: dict):
        self.payload = payload

    def check(self, msg: Message) -> Optional[RuleResult]:
        for k, v in self.payload.items():
            if msg.payload.get(k) != v:
                return self.wrong()
        return self.ok()


class PayloadMapRule(MessageRule):
    def __init__(self, payload_map: Dict[str, type]):
        self.payload = payload_map

    def check(self, msg: Message) -> Optional[RuleResult]:
        for k, v in self.payload.items():
            if k not in msg.payload:
                return self.wrong()
            elif not isinstance(msg.payload[k], v):
                return self.wrong()
        return self.ok()


class StartButtonRule(MessageRule):
    def check(self, msg: Message) -> Optional[RuleResult]:
        if msg.payload == {'command': 'start'}:
            return self.ok()


class CDRule(MessageRule):
    def __init__(self, cd: int = 8):
        self.cd = cd
        self.ts = 0.

    def check(self, msg: Message) -> Optional[RuleResult]:
        if time.time() - self.ts > self.cd:
            self.ts = time.time()
            return self.ok()


class PeerCDRule(MessageRule):
    def __init__(self, cd: int = 16):
        self.cd = cd
        self.peers: Dict[int, float] = {}

    def check(self, msg: Message) -> Optional[RuleResult]:
        if msg.peer_id in self.peers:
            if time.time() - self.peers[msg.peer_id] > self.cd:
                self.peers[msg.peer_id] = time.time()
                return self.ok()
        else:
            self.peers[msg.peer_id] = time.time()
            return self.ok()


class UserCDRule(MessageRule):
    def __init__(self, cd: int = 32):
        self.cd = cd
        self.users: Dict[int, float] = {}

    def check(self, msg: Message) -> Optional[RuleResult]:
        if msg.from_id in self.users:
            if time.time() - self.users[msg.from_id] > self.cd:
                self.users[msg.from_id] = time.time()
                return self.ok()
        else:
            self.users[msg.from_id] = time.time()
            return self.ok()


class RandomRule(Rule):
    def __init__(self, chance: float) -> None:
        self.chance = chance

    def check(self, obj: Any) -> Optional[RuleResult]:
        if self.chance >= 1:
            return self.ok()
        elif self.chance >= random.random():
            return self.ok()


class CustomRule(Rule):
    """
    Пользовательское правило.
    Принимает единственный аргумент в виде функции или лямбды,
    принимающей как единственный аргумент объект эвента.
    """  # FIXME: докстринг

    _func: Callable

    def __init__(self, func: Callable) -> None:
        self._func = func

    def check(self, obj: Any) -> Optional[RuleResult]:
        if self._func(obj):
            return self.ok()

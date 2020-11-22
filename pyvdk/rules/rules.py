from typing import Union, List, Optional, Callable, Any
import re
import vbml

from ..types import Message
from .abc import ABCRule, RuleResult, ABCRulesBunch
from .bunch import RulesBunch


class Rule(ABCRule):

    def __and__(self, rule: "ABCRule") -> "ABCRulesBunch":
        return RulesBunch(self, rule)

    def __or__(self, rule: "ABCRule") -> "ABCRulesBunch":
        return RulesBunch(self, alternative_rule=rule)


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

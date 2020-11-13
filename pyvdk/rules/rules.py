from typing import Union, List, Optional, Callable, Any
import re
import vbml

from ..types import Message
from .abc import ABCMessageRule, ABCRule, RuleResult


class MessageTextRule(ABCMessageRule):
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


class MessageRegexRule(ABCMessageRule):
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


class MessageVBMLRule(ABCMessageRule):
    """  """

    _patcher = vbml.Patcher()
    _patterns: List[vbml.Pattern]

    def __init__(
        self,
        pattern: Union[str, vbml.Pattern, List[Union[str, vbml.Pattern]]],
        patcher: Optional[vbml.Patcher] = None,
        flags: Optional[re.RegexFlag] = None
    ) -> None:

        if isinstance(pattern, str):
            self._patterns = list(vbml.Pattern(pattern, flags=flags))
        elif isinstance(pattern, (list, tuple)):
            self._patterns = [
                vbml.Pattern(i, flags=flags) if isinstance(i, str) else i
                for i in pattern
            ]
        else:
            self._patterns = list(pattern)

        if patcher is not None:
            self._patcher = patcher

    def check(self, msg: Message) -> Optional[RuleResult]:
        for i in self._patterns:
            result = self._patcher.check(i, msg.text)
            if result:
                return result


class CustomRule(ABCRule):
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
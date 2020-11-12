import re
import vbml

from ..types import Message
from .abc import ABCMessageRule, ABCRule, RuleResult


class MessageTextRule(ABCMessageRule):
    """  """

    _text: str
    _lower: bool
    _toggle_vbml: bool
    _patcher = vbml.Patcher()

    def __init__(
        self,
        text: str,
        lower: bool = True,
        toggle_vbml: bool = False
    ) -> None:

        self._text = text.lower() if lower else text
        self._lower = lower
        self._toggle_vbml = toggle_vbml

    def check(self, msg: Message):
        text = msg.text

        if self._lower:
            text = text.lower()

        if self._toggle_vbml:
            pattern = vbml.Pattern(self._text)
            result = self._patcher.check(pattern, text)
            if result is not None:
                return self.Ok(result)
        
        else:
            if text == self._text:
                return self.Ok()


class MessageRegexRule(ABCMessageRule):
    """  """

    _regex: re.Pattern
    _fullmatch: bool

    def __init__(
        self,
        regex: str,
        fullmatch: bool = False
    ) -> None:

        self._regex = re.compile(regex)
        self._fullmatch = fullmatch

    def check(self, msg: Message):
        if self._fullmatch:
            match = self._regex.fullmatch(msg.text)  # noqa
        else:
            match = self._regex.search(msg.text)
        
        if match is not None:
            return self.Ok(match)

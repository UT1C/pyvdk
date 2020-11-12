from typing import Union, List, Optional
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

    def check(self, msg: Message):
        text = msg.text

        if self._lower:
            text = text.lower()
            
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
    
    def check(self, msg: Message):
        pass  # TODO: check
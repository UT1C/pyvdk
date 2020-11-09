import re

from ..types import Message
from .abc import ABCMessageRule, ABCRule, RuleResult


class MessageTextRule(ABCMessageRule):
    """  """

    def __init__(self, text: str, lower: bool = True):
        self._text = text.lower() if lower else text
        self._lower = lower

    def check(self, msg: Message):
        text = msg.text.lower() if self._lower else msg.text
        if text == self._text:
            return self.Ok()


class RegexRule(ABCMessageRule):
    """  """

    def __init__(self, regex: str):
        self.regex = re.compile(regex)

    def check(self, msg: Message):
        match = self.regex.match(msg.text)  # noqa
        if match is not None:
            return self.Ok(match)

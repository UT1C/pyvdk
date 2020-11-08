from ..types import Message
from abc import ABC, abstractmethod
from typing import Optional, Any
import dataclasses


class RuleResult:
    true: bool = False
    def __init__(self, args: list = None):
        self.args = args

class ABCRule(ABC):

    class Ok(RuleResult):
        true: bool = True

    class No(RuleResult):
        true: bool = False

    @abstractmethod
    def __init__(self) -> None:
        ...

    @abstractmethod
    def check(self, obj: Any) -> Optional[RuleResult]:
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"


class ABCMessageRule(ABCRule):

    def check(self, obj: Message) -> Optional[RuleResult]:
        ...

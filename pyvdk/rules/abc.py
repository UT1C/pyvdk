from typing import Optional, Any, TYPE_CHECKING
from abc import ABC, abstractmethod

from ..types import Message
if TYPE_CHECKING:
    from .bunch import RulesBunch


class RuleResult:

    correct: bool

    def __init__(self, *args, correct: bool = False) -> None:
        self.correct = correct
        self.args = args
    
    def __bool__(self):
        return self.correct
    
    def add_to(self, args: list) -> None:
        """
        Если правило вернуло аргументы, этот метод
        добавляет их в список ``args`` (в конец списка) (in-place)
        """

        args.extend(self.args)


class ABCRule(ABC):

    def __init__(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"

    def __and__(self, rule: "ABCRule") -> "RulesBunch":
        return RulesBunch(self, rule)

    def __or__(self, rule: "ABCRule") -> "RulesBunch":
        return RulesBunch(self, alternative_rule=rule)

    def check(self, obj: Any) -> Optional[RuleResult]:
        return self.ok()

    @staticmethod
    def ok(*args):
        return RuleResult(*args, correct=True)

    @staticmethod
    def no(*args):
        return RuleResult(*args)

class ABCMessageRule(ABCRule):

    def check(self, obj: Message) -> Optional[RuleResult]:
        return self.ok()

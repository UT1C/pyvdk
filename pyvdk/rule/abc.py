from ..types import Message
from abc import ABC, abstractmethod
from typing import Optional, Any


class RuleResult:

    correct: bool

    def __init__(self, *args, correct: bool = False) -> None:
        self.correct = correct
        self.args = args
    
    def insert_to(self, args: list) -> None:
        """
        Если правило вернуло аргументы, этот метод
        добавляет их в список ``args`` (в конец списка) (in-place)
        """

        args.extend(self.args)


class ABCRule(ABC):

    @staticmethod
    def ok(*args):
        return RuleResult(*args, correct=True)

    @staticmethod
    def no(*args):
        return RuleResult(*args)

    def __init__(self) -> None:
        ...

    def check(self, obj: Any) -> Optional[RuleResult]:
        return self.ok()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"


class ABCMessageRule(ABCRule):

    def check(self, obj: Message) -> Optional[RuleResult]:
        return self.ok()

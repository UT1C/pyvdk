from ..types import Message
from abc import ABC, abstractmethod
from typing import Optional, Any
import dataclasses


class RuleResult:
    true: bool = False
    def __init__(self, *args) -> None:
        self.args = args
    def update(self, args: list) -> None:
        """Если правило вернуло аргументы, этот метод
        добавляет их в список ``args`` (в конец списка) (in-place)
        """
        args.extend(self.args)

class ABCRule(ABC):

    class Ok(RuleResult):
        true: bool = True

    class No(RuleResult):
        true: bool = False

    def __init__(self) -> None:
        ...

    def check(self, obj: Any) -> Optional[RuleResult]:
        return self.Ok()

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"


class ABCMessageRule(ABCRule):

    def check(self, obj: Message) -> Optional[RuleResult]:
        return self.Ok()

from abc import ABC
from typing import Any, List, Optional, Type, Union

from ..event import ABCHandler


class RuleResult:
    """  """

    def __init__(
        self,
        *args: Any,
        correct: bool = False
    ) -> None:

        self.correct = correct
        self.args = list(args)

    def __bool__(self):
        return self.correct

    def __iter__(self):
        return iter(self.args)

    def add_to(self, args: list) -> None:
        """
        Если правило вернуло аргументы, этот метод
        добавляет их в список ``args`` (в конец списка) (in-place)
        """

        args.extend(self.args)

    def merge(self, rule_result: "RuleResult"):
        """  """

        self.args.extend(rule_result.args)

    @classmethod
    def from_results(cls, *args: "RuleResult") -> "RuleResult":
        results = list()

        for i in args:
            if i is not None:
                results.extend(i)

        return cls(*results, correct=True)


class ABCRule(ABC):
    def __init__(self) -> None:
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} at {hex(id(self))}>"

    def __and__(self, rule: "ABCRule") -> "ABCRulesBunch":
        ...

    def __or__(self, rule: "ABCRule") -> "ABCRulesBunch":
        ...

    def __xor__(self, rule: "ABCRule") -> "ABCRulesBunch":
        ...

    def __eq__(self, rule: "ABCRule") -> "ABCRulesBunch":
        ...

    def __ne__(self, rule: "ABCRule") -> "ABCRulesBunch":
        ...

    def check(self, obj: Any) -> Optional[RuleResult]:
        return self.ok()

    @staticmethod
    def ok(*args) -> RuleResult:
        return RuleResult(*args, correct=True)

    @staticmethod
    def wrong(*args) -> RuleResult:
        return RuleResult(*args)


class ABCRulesBunch(ABCRule):
    """  """

    rules: List[ABCRule]
    alternative_rule: Optional[ABCRule]
    alternative_operation_type: Optional[str]

    def __init__(
        self,
        *rules: ABCRule,
        alternative_rule: Optional[ABCRule] = None,
        alternative_operation_type: Optional[str] = None
    ) -> None:
        ...

    def __call__(
        self,
        inp: Union[ABCHandler, Type]
    ) -> Union[ABCHandler, Type]:
        ...

    def __and__(self, rule: ABCRule) -> "ABCRulesBunch":
        ...

    def __or__(self, rule: ABCRule) -> "ABCRulesBunch":
        ...

    def __xor__(self, rule: ABCRule) -> "ABCRulesBunch":
        ...

    def __eq__(self, rule: ABCRule) -> "ABCRulesBunch":
        ...

    def __ne__(self, rule: ABCRule) -> "ABCRulesBunch":
        ...

    def check(self, obj: Any) -> Optional[RuleResult]:
        ...

    def _check(self, rules: List[ABCRule], obj: Any) -> RuleResult:
        ...

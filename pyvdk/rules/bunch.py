from typing import List, Union, Type, Optional, Any, Callable

from .abc import ABCRule, RuleResult, ABCRulesBunch
from ..event import ABCHandler


class RulesBunch(ABCRulesBunch):
    """  """

    def __init__(
        self,
        *rules: ABCRule,
        alternative_rule: Optional[ABCRule] = None,
        alternative_operation_type: Optional[str] = None,
        invert: Optional[bool] = False
    ) -> None:

        self.rules = list(rules)
        self.alternative_rule = alternative_rule
        self.alternative_operation_type = alternative_operation_type
        self.invert = invert

    def __call__(
        self,
        inp: Union[ABCHandler, Type]
    ) -> Union[ABCHandler, Type]:

        if isinstance(inp, ABCHandler):
            inp.add_rule(self)
        else:
            for k, v in inp.__dict__.items():
                if not k.startswith("_") and isinstance(v, ABCHandler):
                    v.add_rule(self)

        return inp

    def __and__(self, rule: ABCRule) -> ABCRulesBunch:
        self.rules.append(rule)
        return self

    def __or__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="or"
        )

    def __xor__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="xor"
        )

    def __eq__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="eq"
        )

    def __ne__(self, rule: ABCRule) -> ABCRulesBunch:
        return RulesBunch(
            self,
            alternative_rule=rule,
            alternative_operation_type="ne"
        )

    def __invert__(self) -> ABCRulesBunch:
        return RulesBunch(
            self,
            invert=True
        )

    def check(self, obj: Any) -> Optional[RuleResult]:
        result = self._check(self.rules, obj)
        if self.alternative_operation_type is None and result:
            if self.invert:
                return self.wrong()
            return result

        if self.alternative_rule is not None:
            alt_result = self.alternative_rule.check(obj)
            operation = bool(result).__getattribute__(
                f"__{self.alternative_operation_type}__"
            )

            if not operation(bool(alt_result)):
                if self.invert:
                    return self.ok()
                return self.wrong()

            if self.invert:
                return self.wrong()
            return RuleResult.from_results(result, alt_result)

    def _check(self, rules: List[ABCRule], obj: Any) -> RuleResult:
        """  """

        results = list()

        for rule in rules:
            result = rule.check(obj)
            if not result:
                return self.wrong()
            else:
                results.append(result.args)

        if len(results) > 0:
            return self.ok(results)
        return self.ok()

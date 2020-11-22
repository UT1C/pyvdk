from typing import List, Union, Type, Optional, Any

from .abc import ABCRule, RuleResult
from ..event import ABCHandler


class RulesBunch(ABCRule):
    """  """
    
    rules: List[ABCRule]
    alternative_rule: Optional[ABCRule]

    def __init__(
        self,
        *rules: ABCRule,
        alternative_rule: Optional[ABCRule] = None
    ) -> None:

        self.rules = rules
        self.alternative_rule = alternative_rule

    def __call__(
        self,
        inp: Union[ABCHandler, Type]
    ) -> Union[ABCHandler, Type]:

        if isinstance(inp, ABCHandler):
            inp.add_rule(self)
        
        else:
            for k, v in inp.__dict__.items():
                if not k.startswith('_') and isinstance(v, ABCHandler):
                    v.add_rule(self)

        return inp

    def __and__(self, rule: ABCRule) -> "RulesBunch":
        self.rules.append(rule)
        return self
    
    def check(self, obj: Any) -> Optional[RuleResult]:
        result = self._check(self.rules, obj)
        if result:
            return result

        if self.alternative_rule is not None:
            return self.alternative_rule(obj)
    
    def _check(self, rules: List[ABCRule], obj: Any) -> RuleResult:
        """  """

        results = list()

        for rule in rules:
            result = rule(obj)
            if not result:
                return self.no()
            else:
                results.append(result.args)
        
        return self.ok(results)
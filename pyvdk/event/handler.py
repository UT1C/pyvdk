from typing import Any, Callable, Dict, List, Tuple

from ..logging import log
from ..rules import ABCRule
from .abc import ABCHandler
from .event_types import GroupEventType

logger = log.getLogger("event/handler")


class Handler(ABCHandler):
    """
    Класс, хранящий в себе ссылку на функцию-обработчик события,
    и список правил(Rule), когда следует вызывать эту функцию
    """

    def __init__(
        self,
        function: Callable,
        handler_type: GroupEventType,
        *rules: ABCRule,
        level: int,
        endpoint: bool,
    ) -> None:
        """[summary]

        Args:
            function (Callable): функция-обработчик
            *rules (ABCRule): правила, какие события обрабатывать.
            endpoint (bool, optional): Блокирует ли обработчик событие.
                Стандартное значение - True.
        """

        self.function = function
        self.type = handler_type
        self.rules = list(rules)
        self.level = level
        self.endpoint = endpoint
        logger.debug(f"instantiated {self} with rules {rules}")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"{repr(self.function.__name__)} at {hex(id(self))}>"
        )

    def add_rule(self, rule: ABCRule):
        """Метод добавляющий правило в хендлер

        Args:
            rule (ABCRule): объект правила
        """

        self.rules.append(rule)

    def check_rules(self, obj: Any) -> Tuple[bool, List[Any]]:
        """Метод пропускающий объект через правила
        Не использовать извне

        Args:
            obj (Any): объект события

        Returns:
            Tuple[bool, List[Any]]: флаг, подходит ли объект обработчику,
            и список аргументов из правил
        """

        logger.debug("checking rules")
        flag: bool = True
        args: list = []

        for rule in self.rules:
            result = rule.check(obj)
            logger.debug(f"rule: {rule} result: {result}")

            if result is None or not result:
                flag = False
                break

            if result:
                result.add_to(args)

        logger.debug(f"check result: {flag, args}")
        return flag, args

    def handle(self, obj: Any) -> bool:
        """[summary]

        Args:
            obj (Any): объект события

        Returns:
            bool: было ли событие обработано
        """

        logger.debug(f"called {self}")
        flag, args = self.check_rules(obj)

        if flag:
            try:
                logger.debug(f"processing {obj} with {self}")
                self.function(obj, *args)
            except Exception:
                logger.exception("exception occured in handler!")
            else:
                logger.info(f"{self} processed {obj}")
            finally:
                return True
        else:
            logger.debug("conditions not satisfied")
            return False

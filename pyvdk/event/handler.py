from typing import Any, Callable, List, Tuple, Dict

from ..custom_logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .event_types import GroupEventType
from .abc import ABCHandler


logger = log.getLogger("event/handler")


class Handler(ABCHandler):
    """
        Класс, хранящий в себе ссылку на функцию-обработчик события,
        и список правил(Rule), когда следует вызывать эту функцию
    """

    def __init__(
        self,
        function: Callable,
        *rules: ABCRule,
        endpoint: bool = True
    ) -> None:
        """[summary]

        Args:
            function (Callable): функция-обработчик
            *rules (ABCRule): правила, какие события обрабатывать.
            endpoint (bool, optional): Блокирует ли обработчик событие. 
                Стандартное значение - True.
        """
        self.function = function
        self.rules = rules
        self.endpoint = endpoint
        logger.debug(f"instantiated {self} with rules {rules}")

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"{repr(self.function.__name__)} at {hex(id(self))}>"
        )

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
            logger.debug(f"checking rule {rule}")
            result = rule.check(obj)
            logger.debug(f"result: {result}")
            if result is None or not result.true:
                flag = False
                break
            if result.true:
                result.update(args)
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
                return True  # NOTE: или не тру? я себя захуярил
            else:
                logger.debug("sucessfully processed")
                return True
        else:
            logger.info("conditions not satisfied")
            return False

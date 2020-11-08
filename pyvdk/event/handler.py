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
        self.function = function
        self.rules = rules
        self.endpoint = endpoint

    def __repr__(self) -> str:
        return (
            f"<{self.__class__.__name__} "
            f"{repr(self.function.__name__)} at {hex(id(self))}>"
        )

    def handle(self, obj: Any) -> bool:
        logger.debug(f"called {self}")
        args = list()
        call = False
        logger.debug("checking rules")
        if self.rules:
            for rule in self.rules:
                result = rule.check(obj)
                if result is None:
                    return False
                if result.true:
                    call = True
                    if result.args:
                        args.extend(result.args)
                else:
                    return False
        else:
            call = True
        if call:
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
            logger.info("nope, conditions not satisfied")
            return False

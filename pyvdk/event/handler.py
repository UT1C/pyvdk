from typing import Any, Callable, List, Tuple, Dict

from ..custom_logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .event_types import GroupEventType


logger = log.getLogger("event")


class Handler:
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
        args = list()
        call = False
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
            else:
                logger.debug("sucessfully processed")
                return True
        else:
            logger.info("nah, that event not for me")
            return False


class EventHandler:

    api: ABCAPI
    handlers: Dict[GroupEventType, List[Handler]]

    def __init__(self, api: ABCAPI):
        self.api = api
        self.handlers = {i: [] for i in GroupEventType}

    def process(self, event: dict):
        if event["type"] == GroupEventType.MESSAGE_NEW:
            obj = Message(self.api, **event["object"])
        elif event["type"] == GroupEventType.GROUP_JOIN:
            ... # TODO: сделать больше обрабатываемых типов
            return  # временно
        else:
            ... # если тип не найден
            return

        for handler in self.handlers[GroupEventType.MESSAGE_NEW]:
            handling_successful = handler.handle(obj)
            if handling_successful:
                break

    def message_new(self, *rules, text: str = None):
        def wrapper(function):

            _rules = list(i for i in rules if isinstance(i, ABCRule))
            if text:
                _rules.append(MessageTextRule(text))

            self.handlers[GroupEventType.MESSAGE_NEW]\
                .append(Handler(function, *_rules))

        return wrapper

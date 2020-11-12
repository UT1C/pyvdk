from typing import Any, Callable, Dict, List, Tuple

from ..custom_logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .abc import ABCView, ABCHandler
from .event_types import GroupEventType
from ..custom_logging import log


logger = log.getLogger("event/view")


class View(ABCView):
    """  """

    def __init__(self, api: ABCAPI):
        self.api = api
        self.handlers = {i: [] for i in GroupEventType}

    def process(self, event: dict):

        logger.debug("creating object")
        obj = self.__create_object(event)
        logger.debug(f"obj = {obj}")
        logger.debug(f"{vars(obj)}")

        logger.debug("forwarding obj in handlers")
        for handler in self.handlers[GroupEventType.MESSAGE_NEW]:
            handled = handler.handle(obj)
            if handled and handler.endpoint:
                break
        logger.debug("forwarding done")

    def add(self, etype: GroupEventType, handler: ABCHandler):
        logger.debug(f"registered new handler {handler}")
        self.handlers[etype].append(handler)

    def __create_object(self, event: dict):
        etype = GroupEventType(event["type"])
        if etype == GroupEventType.MESSAGE_NEW:
            return Message(self.api, **event["object"]["message"])
        elif etype == GroupEventType.GROUP_JOIN:
            raise Exception("# TODO: ")
        else:
            raise Exception("# TODO: ")

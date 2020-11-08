from typing import Any, Callable, Dict, List, Tuple

from ..custom_logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .abc import ABCView, ABCHandler
from .event_types import GroupEventType


class View(ABCView):

    def __init__(self, api: ABCAPI):
        self.api = api
        self.handlers = {i: [] for i in GroupEventType}

    def process(self, event: dict):

        obj = self.__create_object(event)

        for handler in self.handlers[GroupEventType.MESSAGE_NEW]:
            handling_successful = handler.handle(obj)
            if handling_successful:
                break

    def __create_object(self, event: dict):
        if event["type"] == GroupEventType.MESSAGE_NEW:
            return Message(self.api, **event["object"])
        elif event["type"] == GroupEventType.GROUP_JOIN:
            ... # TODO: сделать больше обрабатываемых типов
            return  # временно
        else:
            ... # если тип не найден
            return

    def add(self, etype: GroupEventType, handler: ABCHandler):
        self.handlers[etype].append(handler)

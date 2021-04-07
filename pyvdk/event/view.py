from typing import Any, Dict, List, Type, Tuple, Callable

from ..logging import log
from ..types import Message
from ..api import ABCAPI
from .abc import ABCHandler, ABCView
from ..types.events import GroupEventType

logger = log.getLogger("event/view")


class MessageView(ABCView):

    def __init__(self, api: ABCAPI) -> None:
        self.api = api
        self.handlers = []

    def processible(self, event: dict) -> bool:
        if GroupEventType(event["type"]) == GroupEventType.MESSAGE_NEW:
            return True
        return False

    def process(self, event: dict) -> None:
        logger.debug("creating object")

        data = event["object"]["message"]
        obj = Message(api=self.api, raw_data=data, **data)

        logger.debug(f"forwarding {repr(obj)} in handlers")
        self.handlers.sort(key=lambda handler: handler.level)

        for handler in self.handlers:
            handled = handler.handle(obj)
            if handled and handler.endpoint:
                break

        logger.debug("forwarding done")

    def add(self, handler: ABCHandler):
        self.handlers.append(handler)

    def extend(self, other: "MessageView"):
        """ extend self with other """
        self.handlers.extend(other.handlers)


class RawView(ABCView):

    handlers: Dict[GroupEventType, List[Tuple[ABCHandler, Callable]]]

    def __init__(self, api: ABCAPI) -> None:
        self.api = api
        self.handlers = {}

    def processible(self, event: dict) -> bool:
        return GroupEventType(event["type"]) in self.handlers

    def process(self, event: dict) -> None:

        handlers = self.handlers[GroupEventType(event["type"])]

        for handler in handlers:
            obj = handler[1](api=self.api, **event["object"])
            handled = handler[0].handle(obj)
            if handled and handler[0].endpoint:
                break

        logger.debug("forwarding done")

    def add(self, handler: ABCHandler, dataclass: Callable = dict):
        if handler.type not in self.handlers:
            self.handlers[handler.type] = []
        self.handlers[handler.type].append((handler, dataclass))

    def extend(self, other: "RawView"):
        """ extend self with other """
        for k, v in other.handlers.items():
            self.handlers[k].extend(v)


class AnyView(ABCView):

    def __init__(self, api: ABCAPI) -> None:
        self.api = api
        self.handlers = []

    def processible(self, event: dict) -> bool:
        return True

    def process(self, event: dict) -> None:
        logger.debug("creating object")

        obj = event["object"]

        logger.debug(f"forwarding {repr(obj)} in handlers")
        self.handlers.sort(key=lambda handler: handler.level)

        for handler in self.handlers:
            handled = handler.handle(obj)
            if handled and handler.endpoint:
                break

        logger.debug("forwarding done")

    def add(self, handler: ABCHandler):
        self.handlers.append(handler)

    def extend(self, other: "AnyView"):
        """ extend self with other """
        self.handlers.extend(other.handlers)

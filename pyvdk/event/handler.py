from ..vk_api import ABCAPI
from .event_types import GroupEventType
from ..types import Message

class EventHandler:
    def __init__(self, api: ABCAPI):
        self.api = api
        self.handlers = {i: [] for i in GroupEventType}

    def process(self, event: dict):
        if event["type"] == GroupEventType.MESSAGE_NEW:
            message = Message(self.api, **event["object"])
            for handler in self.handlers[GroupEventType.MESSAGE_NEW]:
                r = handler.process(message)
                if r.processed and r.block:
                    break
        elif event["type"] == "group_join":
            ... # TODO: сделать больше обрабатываемых типов

    def message_new(self, *rules, text: str = None):
        def wrapper(function):

            self.handlers[GroupEventType.MESSAGE_NEW].append(
                ... # TODO: сюда хуйнуть хенлдер, и в нём рулзы ещё должны быть
                # всё это перед этим надо написать, ёбанаврот
            )

        return wrapper

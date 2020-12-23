import random
from typing import Any, Dict, Optional

from ..api import ABCAPI
from .objects import MessagesMessage


class Callback:
    type: str
    object: Optional[Dict[str, Any]]
    group_id: int
    secret: Optional[str]
    event_id: Optional[str]

    def __init__(self, **kw):
        for k, v in kw.items():
            if k in self.__annotations__:
                self.__setattr__(k, v)
            else:
                raise Exception(f"{self.__class__.__name__}.{k} not annotated")


class Message(MessagesMessage):

    api: ABCAPI

    def __call__(
        self,
        message: str = None,
        attachment: str = None,
        keyboard: str = None,
        user_id: int = None,
        random_id: int = None,
        peer_id: int = None,
        domain: str = None,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        user_ids: list = None,
        lat: float = None,
        long: float = None,
        reply_to: int = None,
        forward_messages: list = None,
        sticker_id: int = None,
        group_id: int = None,
        payload: str = None,
        dont_parse_links: bool = None,
        disable_mentions: bool = None,
        intent: str = None,
        subscribe_id: int = None,
        # ? <= subscribe_id <= 100
    ):
        if peer_id is None:
            if self.peer_id:
                peer_id = self.peer_id
            else:
                # FIXME: есть ли ситуации когда нет peer_id?
                assert 0
        if random_id is None:
            random_id = random.getrandbits(64)
        return self.api.messages.send(
            **{k: v for k, v in locals().items() if k != "self"}
        )

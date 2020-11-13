from abc import ABC, abstractmethod
from typing import Any, Callable, Dict, List, Tuple

from ..logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .event_types import GroupEventType


class ABCHandler(ABC):

    function: Callable
    rules: Tuple[ABCRule, ...]
    endpoint: bool

    @abstractmethod
    def handle(self, obj: Any) -> bool:
        ...


class ABCView(ABC):

    api: ABCAPI
    handlers: Dict[GroupEventType, List[ABCHandler]]

    @abstractmethod
    def __init__(self, api: ABCAPI):
        ...

    @abstractmethod
    def process(self, event: dict):
        ...

    @abstractmethod
    def add(self, etype: GroupEventType, handler: ABCHandler):
        ...


class ABCLabeler(ABC):

    _view: ABCView
    _endpoint_default: bool

    @abstractmethod
    def __init__(self, view: ABCView):
        ...

    @abstractmethod
    def message_new(self, *rules, **kwargs):
        ...
    # @abstractmethod
    # def message_reply(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def message_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def message_allow(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def message_deny(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def message_typing_state(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def message_event(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def photo_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def photo_comment_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def photo_comment_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def photo_comment_restore(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def photo_comment_delete(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def audio_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def video_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def video_comment_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def video_comment_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def video_comment_restore(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def video_comment_delete(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_post_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_repost(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_reply_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_reply_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_reply_restore(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def wall_reply_delete(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def like_add(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def like_remove(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def board_post_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def board_post_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def board_post_restore(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def board_post_delete(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_comment_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_comment_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_comment_restore(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_comment_delete(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_order_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def market_order_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def group_leave(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def group_join(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def user_block(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def user_unblock(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def poll_vote_new(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def group_officers_edit(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def group_change_settings(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def group_change_photo(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def vkpay_transaction(self, *rules, **kwargs):
    #     ...
    # @abstractmethod
    # def app_payload(self, *rules, **kwargs):
    #     ...
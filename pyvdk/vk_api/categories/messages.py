# -*- coding: utf-8 -*-
#
from typing import Optional, Union

from ..category import Category
from ...tools import Keyboard


class Messages(Category):

    def add_chat_user(
        self,
        chat_id: int = None,
        user_id: Optional[int] = None,
        visible_messages_count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("addChatUser", locals())

    def allow_messages_from_group(
        self,
        group_id: int = None,
        key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("allowMessagesFromGroup", locals())

    def create_chat(
        self,
        user_ids: Optional[list] = None,
        title: Optional[str] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("createChat", locals())

    def delete(
        self,
        message_ids: Optional[list] = None,
        spam: Optional[bool] = None,
        group_id: Optional[int] = None,
        delete_for_all: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_chat_photo(
        self,
        chat_id: int = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("deleteChatPhoto", locals())

    def delete_conversation(
        self,
        user_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("deleteConversation", locals())

    def deny_messages_from_group(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("denyMessagesFromGroup", locals())

    def edit(
        self,
        peer_id: int = None,
        message: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        attachment: Optional[str] = None,
        keep_forward_messages: Optional[bool] = None,
        keep_snippets: Optional[bool] = None,
        group_id: Optional[int] = None,
        dont_parse_links: Optional[bool] = None,
        message_id: Optional[int] = None,
        conversation_message_id: Optional[int] = None,
        template: Optional[str] = None,
        keyboard: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_chat(
        self,
        chat_id: int = None,
        title: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("editChat", locals())

    def get_by_conversation_message_id(
        self,
        peer_id: int = None,
        conversation_message_ids: list = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getByConversationMessageId", locals())

    def get_by_id(
        self,
        message_ids: list = None,
        preview_length: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_chat_preview(
        self,
        peer_id: Optional[int] = None,
        link: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getChatPreview", locals())

    def get_conversation_members(
        self,
        peer_id: int = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getConversationMembers", locals())

    def get_conversations(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        filter: Optional[str] = None,
        extended: Optional[bool] = None,
        start_message_id: Optional[int] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getConversations", locals())

    def get_conversations_by_id(
        self,
        peer_ids: list = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getConversationsById", locals())

    def get_history(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        user_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        start_message_id: Optional[int] = None,
        rev: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getHistory", locals())

    def get_history_attachments(
        self,
        peer_id: int = None,
        media_type: Optional[str] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        preserve_order: Optional[bool] = None,
        max_forwards_level: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getHistoryAttachments", locals())

    def get_invite_link(
        self,
        peer_id: int = None,
        reset: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getInviteLink", locals())

    def get_last_activity(
        self,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getLastActivity", locals())

    def get_long_poll_history(
        self,
        ts: Optional[int] = None,
        pts: Optional[int] = None,
        preview_length: Optional[int] = None,
        onlines: Optional[bool] = None,
        fields: Optional[list] = None,
        events_limit: Optional[int] = None,
        msgs_limit: Optional[int] = None,
        max_msg_id: Optional[int] = None,
        group_id: Optional[int] = None,
        lp_version: Optional[int] = None,
        last_n: Optional[int] = None,
        credentials: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getLongPollHistory", locals())

    def get_long_poll_server(
        self,
        need_pts: Optional[bool] = None,
        group_id: Optional[int] = None,
        lp_version: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getLongPollServer", locals())

    def is_messages_from_group_allowed(
        self,
        group_id: int = None,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("isMessagesFromGroupAllowed", locals())

    def join_chat_by_invite_link(
        self,
        link: str = None,
        **kwargs
    ) -> dict:
        return self._request("joinChatByInviteLink", locals())

    def mark_as_answered_conversation(
        self,
        peer_id: int = None,
        answered: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("markAsAnsweredConversation", locals())

    def mark_as_important(
        self,
        message_ids: Optional[list] = None,
        important: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("markAsImportant", locals())

    def mark_as_important_conversation(
        self,
        peer_id: int = None,
        important: Optional[bool] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("markAsImportantConversation", locals())

    def mark_as_read(
        self,
        message_ids: Optional[list] = None,
        peer_id: Optional[int] = None,
        start_message_id: Optional[int] = None,
        group_id: Optional[int] = None,
        mark_conversation_as_read: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("markAsRead", locals())

    def pin(
        self,
        peer_id: int = None,
        message_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("pin", locals())

    def remove_chat_user(
        self,
        chat_id: int = None,
        user_id: Optional[int] = None,
        member_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("removeChatUser", locals())

    def restore(
        self,
        message_id: int = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("restore", locals())

    def search(
        self,
        q: Optional[str] = None,
        peer_id: Optional[int] = None,
        date: Optional[int] = None,
        preview_length: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

    def search_conversations(
        self,
        q: Optional[str] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("searchConversations", locals())

    def send(
        self,
        user_id: Optional[int] = None,
        random_id: Optional[int] = None,
        peer_id: Optional[int] = None,
        domain: Optional[str] = None,
        chat_id: Optional[int] = None,
        user_ids: Optional[list] = None,
        message: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        attachment: Optional[str] = None,
        reply_to: Optional[int] = None,
        forward_messages: Optional[list] = None,
        sticker_id: Optional[int] = None,
        group_id: Optional[int] = None,
        keyboard: Optional[Union[Keyboard, str]] = None,
        payload: Optional[str] = None,
        dont_parse_links: Optional[bool] = None,
        disable_mentions: Optional[bool] = None,
        intent: Optional[str] = None,
        subscribe_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        if isinstance(keyboard, Keyboard):
            keyboard = keyboard()
        return self._request("send", locals())

    def send_message_event_answer(
        self,
        event_id: str = None,
        user_id: int = None,
        peer_id: int = None,
        event_data: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("sendMessageEventAnswer", locals())

    def set_activity(
        self,
        user_id: Optional[int] = None,
        type: Optional[str] = None,
        peer_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("setActivity", locals())

    def set_chat_photo(
        self,
        file: str = None,
        **kwargs
    ) -> dict:
        return self._request("setChatPhoto", locals())

    def unpin(
        self,
        peer_id: int = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("unpin", locals())

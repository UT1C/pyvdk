from ..category import Category


class Messages(Category):
    def add_chat_user(
        self,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        user_id: int = None,
        visible_messages_count: int = None,
        # ? <= visible_messages_count <= 1000
    ) -> dict:
        """
        Adds a new user to a chat.
        """
        return self.__request__("addChatUser", locals())

    def allow_messages_from_group(
        self,
        group_id: int = None,
        key: str = None,
    ) -> dict:
        """
        Allows sending messages from community to the current user.
        """
        return self.__request__("allowMessagesFromGroup", locals())

    def create_chat(
        self,
        user_ids: list = None,
        title: str = None,
        group_id: int = None,
    ) -> dict:
        """
        Creates a chat with several participants.
        """
        return self.__request__("createChat", locals())

    def delete(
        self,
        message_ids: list = None,
        spam: bool = None,
        group_id: int = None,
        delete_for_all: bool = None,
    ) -> dict:
        """
        Deletes one or more messages.
        """
        return self.__request__("delete", locals())

    def delete_chat_photo(
        self,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        group_id: int = None,
    ) -> dict:
        """
        Deletes a chat's cover picture.
        """
        return self.__request__("deleteChatPhoto", locals())

    def delete_conversation(
        self,
        user_id: int = None,
        peer_id: int = None,
        group_id: int = None,
    ) -> dict:
        """
        Deletes all private messages in a conversation.
        """
        return self.__request__("deleteConversation", locals())

    def deny_messages_from_group(
        self,
        group_id: int = None,
    ) -> dict:
        """
        Denies sending message from community to the current user.
        """
        return self.__request__("denyMessagesFromGroup", locals())

    def edit(
        self,
        peer_id: int = None,
        message: str = None,
        lat: float = None,
        long: float = None,
        attachment: str = None,
        keep_forward_messages: bool = None,
        keep_snippets: bool = None,
        group_id: int = None,
        dont_parse_links: bool = None,
        message_id: int = None,
        conversation_message_id: int = None,
        template: str = None,
        keyboard: str = None,
    ) -> dict:
        """
        Edits the message.
        """
        return self.__request__("edit", locals())

    def edit_chat(
        self,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        title: str = None,
    ) -> dict:
        """
        Edits the title of a chat.
        """
        return self.__request__("editChat", locals())

    def get_by_conversation_message_id(
        self,
        peer_id: int = None,
        conversation_message_ids: list = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns messages by their IDs within the conversation.
        """
        return self.__request__("getByConversationMessageId", locals())

    def get_by_id(
        self,
        message_ids: list = None,
        preview_length: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns messages by their IDs.
        """
        return self.__request__("getById", locals())

    def get_chat_preview(
        self,
        peer_id: int = None,
        link: str = None,
        fields: list = None,
    ) -> dict:
        """
        <null>
        """
        return self.__request__("getChatPreview", locals())

    def get_conversation_members(
        self,
        peer_id: int = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns a list of IDs of users participating in a chat.
        """
        return self.__request__("getConversationMembers", locals())

    def get_conversations(
        self,
        offset: int = None,
        count: int = None,
        # ? <= count <= 200
        filter: str = None,
        extended: bool = None,
        start_message_id: int = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns a list of the current user's conversations.
        """
        return self.__request__("getConversations", locals())

    def get_conversations_by_id(
        self,
        peer_ids: list = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns conversations by their IDs
        """
        return self.__request__("getConversationsById", locals())

    def get_history(
        self,
        offset: int = None,
        count: int = None,
        # ? <= count <= 200
        user_id: int = None,
        peer_id: int = None,
        start_message_id: int = None,
        rev: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns message history for the specified user or group chat.
        """
        return self.__request__("getHistory", locals())

    def get_history_attachments(
        self,
        peer_id: int = None,
        media_type: str = None,
        start_from: str = None,
        count: int = None,
        # ? <= count <= 200
        photo_sizes: bool = None,
        fields: list = None,
        group_id: int = None,
        preserve_order: bool = None,
        max_forwards_level: int = None,
        # ? <= max_forwards_level <= 45
    ) -> dict:
        """
        Returns media files from the dialog or group chat.
        """
        return self.__request__("getHistoryAttachments", locals())

    def get_invite_link(
        self,
        peer_id: int = None,
        reset: bool = None,
        group_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self.__request__("getInviteLink", locals())

    def get_last_activity(
        self,
        user_id: int = None,
    ) -> dict:
        """
        Returns a user's current status and date of last activity.
        """
        return self.__request__("getLastActivity", locals())

    def get_long_poll_history(
        self,
        ts: int = None,
        pts: int = None,
        preview_length: int = None,
        onlines: bool = None,
        fields: list = None,
        events_limit: int = None,
        # 1000 <= events_limit <= ?
        msgs_limit: int = None,
        # 200 <= msgs_limit <= ?
        max_msg_id: int = None,
        group_id: int = None,
        lp_version: int = None,
        last_n: int = None,
        # ? <= last_n <= 2000
        credentials: bool = None,
    ) -> dict:
        """
        Returns updates in user's private messages.
        """
        return self.__request__("getLongPollHistory", locals())

    def get_long_poll_server(
        self,
        need_pts: bool = None,
        group_id: int = None,
        lp_version: int = None,
    ) -> dict:
        """
        Returns data required for connection to a Long Poll server.
        """
        return self.__request__("getLongPollServer", locals())

    def is_messages_from_group_allowed(
        self,
        group_id: int = None,
        user_id: int = None,
    ) -> dict:
        """
        Returns information whether sending messages from the community to current user is allowed.
        """
        return self.__request__("isMessagesFromGroupAllowed", locals())

    def join_chat_by_invite_link(
        self,
        link: str = None,
    ) -> dict:
        """
        <null>
        """
        return self.__request__("joinChatByInviteLink", locals())

    def mark_as_answered_conversation(
        self,
        peer_id: int = None,
        answered: bool = None,
        group_id: int = None,
    ) -> dict:
        """
        Marks and unmarks conversations as unanswered.
        """
        return self.__request__("markAsAnsweredConversation", locals())

    def mark_as_important(
        self,
        message_ids: list = None,
        important: int = None,
    ) -> dict:
        """
        Marks and unmarks messages as important (starred).
        """
        return self.__request__("markAsImportant", locals())

    def mark_as_important_conversation(
        self,
        peer_id: int = None,
        important: bool = None,
        group_id: int = None,
    ) -> dict:
        """
        Marks and unmarks conversations as important.
        """
        return self.__request__("markAsImportantConversation", locals())

    def mark_as_read(
        self,
        message_ids: list = None,
        peer_id: int = None,
        start_message_id: int = None,
        group_id: int = None,
        mark_conversation_as_read: bool = None,
    ) -> dict:
        """
        Marks messages as read.
        """
        return self.__request__("markAsRead", locals())

    def pin(
        self,
        peer_id: int = None,
        message_id: int = None,
    ) -> dict:
        """
        Pin a message.
        """
        return self.__request__("pin", locals())

    def remove_chat_user(
        self,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        user_id: int = None,
        member_id: int = None,
    ) -> dict:
        """
        Allows the current user to leave a chat or, if the current user started the chat, allows the user to remove another user from the chat.
        """
        return self.__request__("removeChatUser", locals())

    def restore(
        self,
        message_id: int = None,
        group_id: int = None,
    ) -> dict:
        """
        Restores a deleted message.
        """
        return self.__request__("restore", locals())

    def search(
        self,
        q: str = None,
        peer_id: int = None,
        date: int = None,
        preview_length: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 100
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns a list of the current user's private messages that match search criteria.
        """
        return self.__request__("search", locals())

    def search_conversations(
        self,
        q: str = None,
        count: int = None,
        extended: bool = None,
        fields: list = None,
        group_id: int = None,
    ) -> dict:
        """
        Returns a list of the current user's conversations that match search criteria.
        """
        return self.__request__("searchConversations", locals())

    def send(
        self,
        user_id: int = None,
        random_id: int = None,
        peer_id: int = None,
        domain: str = None,
        chat_id: int = None,
        # ? <= chat_id <= 100000000
        user_ids: list = None,
        message: str = None,
        lat: float = None,
        long: float = None,
        attachment: str = None,
        reply_to: int = None,
        forward_messages: list = None,
        sticker_id: int = None,
        group_id: int = None,
        keyboard: str = None,
        payload: str = None,
        dont_parse_links: bool = None,
        disable_mentions: bool = None,
        intent: str = None,
        subscribe_id: int = None,
        # ? <= subscribe_id <= 100
    ) -> dict:
        """
        Sends a message.
        """
        return self.__request__("send", locals())

    def send_message_event_answer(
        self,
        event_id: str = None,
        user_id: int = None,
        peer_id: int = None,
        event_data: str = None,
    ) -> dict:
        """
        <null>
        """
        return self.__request__("sendMessageEventAnswer", locals())

    def set_activity(
        self,
        user_id: int = None,
        type: str = None,
        peer_id: int = None,
        group_id: int = None,
    ) -> dict:
        """
        Changes the status of a user as typing in a conversation.
        """
        return self.__request__("setActivity", locals())

    def set_chat_photo(
        self,
        file: str = None,
    ) -> dict:
        """
        Sets a previously-uploaded picture as the cover picture of a chat.
        """
        return self.__request__("setChatPhoto", locals())

    def unpin(
        self,
        peer_id: int = None,
        group_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self.__request__("unpin", locals())


# generated at 2020.11.08 08:32:23

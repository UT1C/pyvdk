# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Groups(Category):

    def add_address(
        self,
        group_id: int = None,
        title: str = None,
        address: str = None,
        additional_address: Optional[str] = None,
        country_id: int = None,
        city_id: int = None,
        metro_id: Optional[int] = None,
        latitude: float = None,
        longitude: float = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("addAddress", locals())

    def add_callback_server(
        self,
        group_id: int = None,
        url: str = None,
        title: str = None,
        secret_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addCallbackServer", locals())

    def add_link(
        self,
        group_id: int = None,
        link: str = None,
        text: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addLink", locals())

    def approve_request(
        self,
        group_id: int = None,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("approveRequest", locals())

    def ban(
        self,
        group_id: int = None,
        owner_id: Optional[int] = None,
        end_date: Optional[int] = None,
        reason: Optional[int] = None,
        comment: Optional[str] = None,
        comment_visible: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("ban", locals())

    def create(
        self,
        title: str = None,
        description: Optional[str] = None,
        type: Optional[str] = None,
        public_category: Optional[int] = None,
        subtype: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("create", locals())

    def delete_callback_server(
        self,
        group_id: int = None,
        server_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteCallbackServer", locals())

    def delete_link(
        self,
        group_id: int = None,
        link_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteLink", locals())

    def disable_online(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("disableOnline", locals())

    def edit(
        self,
        group_id: int = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        screen_name: Optional[str] = None,
        access: Optional[int] = None,
        website: Optional[str] = None,
        subject: Optional[str] = None,
        email: Optional[str] = None,
        phone: Optional[str] = None,
        rss: Optional[str] = None,
        event_start_date: Optional[int] = None,
        event_finish_date: Optional[int] = None,
        event_group_id: Optional[int] = None,
        public_category: Optional[int] = None,
        public_subcategory: Optional[int] = None,
        public_date: Optional[str] = None,
        wall: Optional[int] = None,
        topics: Optional[int] = None,
        photos: Optional[int] = None,
        video: Optional[int] = None,
        audio: Optional[int] = None,
        links: Optional[bool] = None,
        events: Optional[bool] = None,
        places: Optional[bool] = None,
        contacts: Optional[bool] = None,
        docs: Optional[int] = None,
        wiki: Optional[int] = None,
        messages: Optional[bool] = None,
        articles: Optional[bool] = None,
        addresses: Optional[bool] = None,
        age_limits: Optional[int] = None,
        market: Optional[bool] = None,
        market_comments: Optional[bool] = None,
        market_country: Optional[list] = None,
        market_city: Optional[list] = None,
        market_currency: Optional[int] = None,
        market_contact: Optional[int] = None,
        market_wiki: Optional[int] = None,
        obscene_filter: Optional[bool] = None,
        obscene_stopwords: Optional[bool] = None,
        obscene_words: Optional[list] = None,
        main_section: Optional[int] = None,
        secondary_section: Optional[int] = None,
        country: Optional[int] = None,
        city: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_address(
        self,
        group_id: int = None,
        address_id: int = None,
        title: Optional[str] = None,
        address: Optional[str] = None,
        additional_address: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        metro_id: Optional[int] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        phone: Optional[str] = None,
        work_info_status: Optional[str] = None,
        timetable: Optional[str] = None,
        is_main_address: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("editAddress", locals())

    def edit_callback_server(
        self,
        group_id: int = None,
        server_id: int = None,
        url: str = None,
        title: str = None,
        secret_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("editCallbackServer", locals())

    def edit_link(
        self,
        group_id: int = None,
        link_id: int = None,
        text: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("editLink", locals())

    def edit_manager(
        self,
        group_id: int = None,
        user_id: int = None,
        role: Optional[str] = None,
        is_contact: Optional[bool] = None,
        contact_position: Optional[str] = None,
        contact_phone: Optional[str] = None,
        contact_email: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("editManager", locals())

    def enable_online(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("enableOnline", locals())

    def get(
        self,
        user_id: Optional[int] = None,
        extended: Optional[bool] = None,
        filter: Optional[list] = None,
        fields: Optional[list] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_addresses(
        self,
        group_id: int = None,
        address_ids: Optional[list] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getAddresses", locals())

    def get_banned(
        self,
        group_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getBanned", locals())

    def get_by_id(
        self,
        group_ids: Optional[list] = None,
        group_id: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_callback_confirmation_code(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getCallbackConfirmationCode", locals())

    def get_callback_servers(
        self,
        group_id: int = None,
        server_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getCallbackServers", locals())

    def get_callback_settings(
        self,
        group_id: int = None,
        server_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getCallbackSettings", locals())

    def get_catalog(
        self,
        category_id: Optional[int] = None,
        subcategory_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getCatalog", locals())

    def get_catalog_info(
        self,
        extended: Optional[bool] = None,
        subcategories: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getCatalogInfo", locals())

    def get_invited_users(
        self,
        group_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getInvitedUsers", locals())

    def get_invites(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getInvites", locals())

    def get_long_poll_server(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getLongPollServer", locals())

    def get_long_poll_settings(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getLongPollSettings", locals())

    def get_members(
        self,
        group_id: Optional[str] = None,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        filter: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getMembers", locals())

    def get_requests(
        self,
        group_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getRequests", locals())

    def get_settings(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getSettings", locals())

    def get_token_permissions(
        self,
        **kwargs
    ) -> dict:
        return self._request("getTokenPermissions", locals())

    def invite(
        self,
        group_id: int = None,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("invite", locals())

    def is_member(
        self,
        group_id: str = None,
        user_id: Optional[int] = None,
        user_ids: Optional[list] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("isMember", locals())

    def join(
        self,
        group_id: Optional[int] = None,
        not_sure: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("join", locals())

    def leave(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("leave", locals())

    def remove_user(
        self,
        group_id: int = None,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeUser", locals())

    def reorder_link(
        self,
        group_id: int = None,
        link_id: int = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderLink", locals())

    def search(
        self,
        q: str = None,
        type: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        future: Optional[bool] = None,
        market: Optional[bool] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

    def set_callback_settings(
        self,
        group_id: int = None,
        server_id: Optional[int] = None,
        api_version: Optional[str] = None,
        message_new: Optional[bool] = None,
        message_reply: Optional[bool] = None,
        message_allow: Optional[bool] = None,
        message_edit: Optional[bool] = None,
        message_deny: Optional[bool] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[bool] = None,
        audio_new: Optional[bool] = None,
        video_new: Optional[bool] = None,
        wall_reply_new: Optional[bool] = None,
        wall_reply_edit: Optional[bool] = None,
        wall_reply_delete: Optional[bool] = None,
        wall_reply_restore: Optional[bool] = None,
        wall_post_new: Optional[bool] = None,
        wall_repost: Optional[bool] = None,
        board_post_new: Optional[bool] = None,
        board_post_edit: Optional[bool] = None,
        board_post_restore: Optional[bool] = None,
        board_post_delete: Optional[bool] = None,
        photo_comment_new: Optional[bool] = None,
        photo_comment_edit: Optional[bool] = None,
        photo_comment_delete: Optional[bool] = None,
        photo_comment_restore: Optional[bool] = None,
        video_comment_new: Optional[bool] = None,
        video_comment_edit: Optional[bool] = None,
        video_comment_delete: Optional[bool] = None,
        video_comment_restore: Optional[bool] = None,
        market_comment_new: Optional[bool] = None,
        market_comment_edit: Optional[bool] = None,
        market_comment_delete: Optional[bool] = None,
        market_comment_restore: Optional[bool] = None,
        poll_vote_new: Optional[bool] = None,
        group_join: Optional[bool] = None,
        group_leave: Optional[bool] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        lead_forms_new: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("setCallbackSettings", locals())

    def set_long_poll_settings(
        self,
        group_id: int = None,
        enabled: Optional[bool] = None,
        api_version: Optional[str] = None,
        message_new: Optional[bool] = None,
        message_reply: Optional[bool] = None,
        message_allow: Optional[bool] = None,
        message_deny: Optional[bool] = None,
        message_edit: Optional[bool] = None,
        message_typing_state: Optional[bool] = None,
        photo_new: Optional[bool] = None,
        audio_new: Optional[bool] = None,
        video_new: Optional[bool] = None,
        wall_reply_new: Optional[bool] = None,
        wall_reply_edit: Optional[bool] = None,
        wall_reply_delete: Optional[bool] = None,
        wall_reply_restore: Optional[bool] = None,
        wall_post_new: Optional[bool] = None,
        wall_repost: Optional[bool] = None,
        board_post_new: Optional[bool] = None,
        board_post_edit: Optional[bool] = None,
        board_post_restore: Optional[bool] = None,
        board_post_delete: Optional[bool] = None,
        photo_comment_new: Optional[bool] = None,
        photo_comment_edit: Optional[bool] = None,
        photo_comment_delete: Optional[bool] = None,
        photo_comment_restore: Optional[bool] = None,
        video_comment_new: Optional[bool] = None,
        video_comment_edit: Optional[bool] = None,
        video_comment_delete: Optional[bool] = None,
        video_comment_restore: Optional[bool] = None,
        market_comment_new: Optional[bool] = None,
        market_comment_edit: Optional[bool] = None,
        market_comment_delete: Optional[bool] = None,
        market_comment_restore: Optional[bool] = None,
        poll_vote_new: Optional[bool] = None,
        group_join: Optional[bool] = None,
        group_leave: Optional[bool] = None,
        group_change_settings: Optional[bool] = None,
        group_change_photo: Optional[bool] = None,
        group_officers_edit: Optional[bool] = None,
        user_block: Optional[bool] = None,
        user_unblock: Optional[bool] = None,
        like_add: Optional[bool] = None,
        like_remove: Optional[bool] = None,
        message_event: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("setLongPollSettings", locals())

    def unban(
        self,
        group_id: int = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("unban", locals())

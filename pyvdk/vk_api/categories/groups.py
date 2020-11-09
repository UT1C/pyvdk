from ..category import Category


class Groups(Category):
    def add_address(
        self,
        group_id: int = None,
        title: str = None,
        address: str = None,
        additional_address: str = None,
        country_id: int = None,
        # 1 <= country_id <= ?
        city_id: int = None,
        # 1 <= city_id <= ?
        metro_id: int = None,
        latitude: float = None,
        # -90 <= latitude <= 90
        longitude: float = None,
        # -180 <= longitude <= 180
        phone: str = None,
        work_info_status: str = None,
        timetable: str = None,
        is_main_address: bool = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("addAddress", locals())

    def add_callback_server(
        self,
        group_id: int = None,
        url: str = None,
        title: str = None,
        secret_key: str = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("addCallbackServer", locals())

    def add_link(
        self,
        group_id: int = None,
        link: str = None,
        text: str = None,
    ) -> dict:
        """
        Allows to add a link to the community.
        """
        return self._request("addLink", locals())

    def approve_request(
        self,
        group_id: int = None,
        user_id: int = None,
    ) -> dict:
        """
        Allows to approve join request to the community.
        """
        return self._request("approveRequest", locals())

    def ban(
        self,
        group_id: int = None,
        owner_id: int = None,
        end_date: int = None,
        reason: int = None,
        comment: str = None,
        comment_visible: bool = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("ban", locals())

    def create(
        self,
        title: str = None,
        description: str = None,
        type: str = None,
        public_category: int = None,
        subtype: int = None,
    ) -> dict:
        """
        Creates a new community.
        """
        return self._request("create", locals())

    def delete_callback_server(
        self,
        group_id: int = None,
        server_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("deleteCallbackServer", locals())

    def delete_link(
        self,
        group_id: int = None,
        link_id: int = None,
    ) -> dict:
        """
        Allows to delete a link from the community.
        """
        return self._request("deleteLink", locals())

    def disable_online(
        self,
        group_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("disableOnline", locals())

    def edit(
        self,
        group_id: int = None,
        title: str = None,
        description: str = None,
        screen_name: str = None,
        access: int = None,
        website: str = None,
        subject: str = None,
        email: str = None,
        phone: str = None,
        rss: str = None,
        event_start_date: int = None,
        event_finish_date: int = None,
        event_group_id: int = None,
        public_category: int = None,
        public_subcategory: int = None,
        public_date: str = None,
        wall: int = None,
        topics: int = None,
        photos: int = None,
        video: int = None,
        audio: int = None,
        links: bool = None,
        events: bool = None,
        places: bool = None,
        contacts: bool = None,
        docs: int = None,
        wiki: int = None,
        messages: bool = None,
        articles: bool = None,
        addresses: bool = None,
        age_limits: int = None,
        market: bool = None,
        market_comments: bool = None,
        market_country: list = None,
        market_city: list = None,
        market_currency: int = None,
        market_contact: int = None,
        market_wiki: int = None,
        obscene_filter: bool = None,
        obscene_stopwords: bool = None,
        obscene_words: list = None,
        main_section: int = None,
        secondary_section: int = None,
        country: int = None,
        city: int = None,
    ) -> dict:
        """
        Edits a community.
        """
        return self._request("edit", locals())

    def edit_address(
        self,
        group_id: int = None,
        address_id: int = None,
        title: str = None,
        address: str = None,
        additional_address: str = None,
        country_id: int = None,
        city_id: int = None,
        metro_id: int = None,
        latitude: float = None,
        # -90 <= latitude <= 90
        longitude: float = None,
        # -180 <= longitude <= 180
        phone: str = None,
        work_info_status: str = None,
        timetable: str = None,
        is_main_address: bool = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("editAddress", locals())

    def edit_callback_server(
        self,
        group_id: int = None,
        server_id: int = None,
        url: str = None,
        title: str = None,
        secret_key: str = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("editCallbackServer", locals())

    def edit_link(
        self,
        group_id: int = None,
        link_id: int = None,
        text: str = None,
    ) -> dict:
        """
        Allows to edit a link in the community.
        """
        return self._request("editLink", locals())

    def edit_manager(
        self,
        group_id: int = None,
        user_id: int = None,
        role: str = None,
        is_contact: bool = None,
        contact_position: str = None,
        contact_phone: str = None,
        contact_email: str = None,
    ) -> dict:
        """
        Allows to add, remove or edit the community manager.
        """
        return self._request("editManager", locals())

    def enable_online(
        self,
        group_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("enableOnline", locals())

    def get(
        self,
        user_id: int = None,
        extended: bool = None,
        filter: list = None,
        fields: list = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 1000
    ) -> dict:
        """
        Returns a list of the communities to which a user belongs.
        """
        return self._request("get", locals())

    def get_addresses(
        self,
        group_id: int = None,
        address_ids: list = None,
        latitude: float = None,
        # -90 <= latitude <= 90
        longitude: float = None,
        # -180 <= longitude <= 180
        offset: int = None,
        count: int = None,
        fields: list = None,
    ) -> dict:
        """
        Returns a list of community addresses.
        """
        return self._request("getAddresses", locals())

    def get_banned(
        self,
        group_id: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 200
        fields: list = None,
        owner_id: int = None,
    ) -> dict:
        """
        Returns a list of users on a community blacklist.
        """
        return self._request("getBanned", locals())

    def get_by_id(
        self,
        group_ids: list = None,
        group_id: str = None,
        fields: list = None,
    ) -> dict:
        """
        Returns information about communities by their IDs.
        """
        return self._request("getById", locals())

    def get_callback_confirmation_code(
        self,
        group_id: int = None,
    ) -> dict:
        """
        Returns Callback API confirmation code for the community.
        """
        return self._request("getCallbackConfirmationCode", locals())

    def get_callback_servers(
        self,
        group_id: int = None,
        server_ids: list = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("getCallbackServers", locals())

    def get_callback_settings(
        self,
        group_id: int = None,
        server_id: int = None,
    ) -> dict:
        """
        Returns [vk.com/dev/callback_api|Callback API] notifications settings.
        """
        return self._request("getCallbackSettings", locals())

    def get_catalog(
        self,
        category_id: int = None,
        subcategory_id: int = None,
        # ? <= subcategory_id <= 99
    ) -> dict:
        """
        Returns communities list for a catalog category.
        """
        return self._request("getCatalog", locals())

    def get_catalog_info(
        self,
        extended: bool = None,
        subcategories: bool = None,
    ) -> dict:
        """
        Returns categories list for communities catalog
        """
        return self._request("getCatalogInfo", locals())

    def get_invited_users(
        self,
        group_id: int = None,
        offset: int = None,
        count: int = None,
        fields: list = None,
        name_case: str = None,
    ) -> dict:
        """
        Returns invited users list of a community
        """
        return self._request("getInvitedUsers", locals())

    def get_invites(
        self,
        offset: int = None,
        count: int = None,
        extended: bool = None,
    ) -> dict:
        """
        Returns a list of invitations to join communities and events.
        """
        return self._request("getInvites", locals())

    def get_long_poll_server(
        self,
        group_id: int = None,
    ) -> dict:
        """
        Returns the data needed to query a Long Poll server for events
        """
        return self._request("getLongPollServer", locals())

    def get_long_poll_settings(
        self,
        group_id: int = None,
    ) -> dict:
        """
        Returns Long Poll notification settings
        """
        return self._request("getLongPollSettings", locals())

    def get_members(
        self,
        group_id: str = None,
        sort: str = None,
        offset: int = None,
        count: int = None,
        fields: list = None,
        filter: str = None,
    ) -> dict:
        """
        Returns a list of community members.
        """
        return self._request("getMembers", locals())

    def get_requests(
        self,
        group_id: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 200
        fields: list = None,
    ) -> dict:
        """
        Returns a list of requests to the community.
        """
        return self._request("getRequests", locals())

    def get_settings(
        self,
        group_id: int = None,
    ) -> dict:
        """
        Returns community settings.
        """
        return self._request("getSettings", locals())

    def get_token_permissions(
        self,
    ) -> dict:
        """
        <null>
        """
        return self._request("getTokenPermissions", locals())

    def invite(
        self,
        group_id: int = None,
        user_id: int = None,
    ) -> dict:
        """
        Allows to invite friends to the community.
        """
        return self._request("invite", locals())

    def is_member(
        self,
        group_id: str = None,
        user_id: int = None,
        user_ids: list = None,
        extended: bool = None,
    ) -> dict:
        """
        Returns information specifying whether a user is a member of a community.
        """
        return self._request("isMember", locals())

    def join(
        self,
        group_id: int = None,
        not_sure: str = None,
    ) -> dict:
        """
        With this method you can join the group or public page, and also confirm your participation in an event.
        """
        return self._request("join", locals())

    def leave(
        self,
        group_id: int = None,
    ) -> dict:
        """
        With this method you can leave a group, public page, or event.
        """
        return self._request("leave", locals())

    def remove_user(
        self,
        group_id: int = None,
        user_id: int = None,
    ) -> dict:
        """
        Removes a user from the community.
        """
        return self._request("removeUser", locals())

    def reorder_link(
        self,
        group_id: int = None,
        link_id: int = None,
        after: int = None,
    ) -> dict:
        """
        Allows to reorder links in the community.
        """
        return self._request("reorderLink", locals())

    def search(
        self,
        q: str = None,
        type: str = None,
        country_id: int = None,
        city_id: int = None,
        future: bool = None,
        market: bool = None,
        sort: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 1000
    ) -> dict:
        """
        Returns a list of communities matching the search criteria.
        """
        return self._request("search", locals())

    def set_callback_settings(
        self,
        group_id: int = None,
        server_id: int = None,
        api_version: str = None,
        message_new: bool = None,
        message_reply: bool = None,
        message_allow: bool = None,
        message_edit: bool = None,
        message_deny: bool = None,
        message_typing_state: bool = None,
        photo_new: bool = None,
        audio_new: bool = None,
        video_new: bool = None,
        wall_reply_new: bool = None,
        wall_reply_edit: bool = None,
        wall_reply_delete: bool = None,
        wall_reply_restore: bool = None,
        wall_post_new: bool = None,
        wall_repost: bool = None,
        board_post_new: bool = None,
        board_post_edit: bool = None,
        board_post_restore: bool = None,
        board_post_delete: bool = None,
        photo_comment_new: bool = None,
        photo_comment_edit: bool = None,
        photo_comment_delete: bool = None,
        photo_comment_restore: bool = None,
        video_comment_new: bool = None,
        video_comment_edit: bool = None,
        video_comment_delete: bool = None,
        video_comment_restore: bool = None,
        market_comment_new: bool = None,
        market_comment_edit: bool = None,
        market_comment_delete: bool = None,
        market_comment_restore: bool = None,
        poll_vote_new: bool = None,
        group_join: bool = None,
        group_leave: bool = None,
        group_change_settings: bool = None,
        group_change_photo: bool = None,
        group_officers_edit: bool = None,
        user_block: bool = None,
        user_unblock: bool = None,
        lead_forms_new: bool = None,
        like_add: bool = None,
        like_remove: bool = None,
        message_event: bool = None,
    ) -> dict:
        """
        Allow to set notifications settings for group.
        """
        return self._request("setCallbackSettings", locals())

    def set_long_poll_settings(
        self,
        group_id: int = None,
        enabled: bool = None,
        api_version: str = None,
        message_new: bool = None,
        message_reply: bool = None,
        message_allow: bool = None,
        message_deny: bool = None,
        message_edit: bool = None,
        message_typing_state: bool = None,
        photo_new: bool = None,
        audio_new: bool = None,
        video_new: bool = None,
        wall_reply_new: bool = None,
        wall_reply_edit: bool = None,
        wall_reply_delete: bool = None,
        wall_reply_restore: bool = None,
        wall_post_new: bool = None,
        wall_repost: bool = None,
        board_post_new: bool = None,
        board_post_edit: bool = None,
        board_post_restore: bool = None,
        board_post_delete: bool = None,
        photo_comment_new: bool = None,
        photo_comment_edit: bool = None,
        photo_comment_delete: bool = None,
        photo_comment_restore: bool = None,
        video_comment_new: bool = None,
        video_comment_edit: bool = None,
        video_comment_delete: bool = None,
        video_comment_restore: bool = None,
        market_comment_new: bool = None,
        market_comment_edit: bool = None,
        market_comment_delete: bool = None,
        market_comment_restore: bool = None,
        poll_vote_new: bool = None,
        group_join: bool = None,
        group_leave: bool = None,
        group_change_settings: bool = None,
        group_change_photo: bool = None,
        group_officers_edit: bool = None,
        user_block: bool = None,
        user_unblock: bool = None,
        like_add: bool = None,
        like_remove: bool = None,
        message_event: bool = None,
    ) -> dict:
        """
        Sets Long Poll notification settings
        """
        return self._request("setLongPollSettings", locals())

    def unban(
        self,
        group_id: int = None,
        owner_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("unban", locals())


# generated at 2020.11.08 08:32:23

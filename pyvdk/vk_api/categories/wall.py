from ..category import Category


class Wall(Category):
    def close_comments(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("closeComments", locals())

    def create_comment(
        self,
        owner_id: int = None,
        post_id: int = None,
        from_group: int = None,
        message: str = None,
        reply_to_comment: int = None,
        attachments: list = None,
        sticker_id: int = None,
        guid: str = None,
    ) -> dict:
        """
        Adds a comment to a post on a user wall or community wall.
        """
        return self._request("createComment", locals())

    def delete(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        Deletes a post from a user wall or community wall.
        """
        return self._request("delete", locals())

    def delete_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
    ) -> dict:
        """
        Deletes a comment on a post on a user wall or community wall.
        """
        return self._request("deleteComment", locals())

    def edit(
        self,
        owner_id: int = None,
        post_id: int = None,
        friends_only: bool = None,
        message: str = None,
        attachments: list = None,
        services: str = None,
        signed: bool = None,
        publish_date: int = None,
        lat: float = None,
        long: float = None,
        place_id: int = None,
        mark_as_ads: bool = None,
        close_comments: bool = None,
        poster_bkg_id: int = None,
        poster_bkg_owner_id: int = None,
        poster_bkg_access_hash: str = None,
        copyright: str = None,
    ) -> dict:
        """
        Edits a post on a user wall or community wall.
        """
        return self._request("edit", locals())

    def edit_ads_stealth(
        self,
        owner_id: int = None,
        post_id: int = None,
        message: str = None,
        attachments: list = None,
        signed: bool = None,
        lat: float = None,
        long: float = None,
        place_id: int = None,
        link_button: str = None,
        link_title: str = None,
        link_image: str = None,
        link_video: str = None,
    ) -> dict:
        """
        Allows to edit hidden post.
        """
        return self._request("editAdsStealth", locals())

    def edit_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        message: str = None,
        attachments: list = None,
    ) -> dict:
        """
        Edits a comment on a user wall or community wall.
        """
        return self._request("editComment", locals())

    def get(
        self,
        owner_id: int = None,
        domain: str = None,
        offset: int = None,
        count: int = None,
        filter: str = None,
        extended: bool = None,
        fields: list = None,
    ) -> dict:
        """
        Returns a list of posts on a user wall or community wall.
        """
        return self._request("get", locals())

    def get_by_id(
        self,
        posts: list = None,
        extended: bool = None,
        copy_history_depth: int = None,
        fields: list = None,
    ) -> dict:
        """
        Returns a list of posts from user or community walls by their IDs.
        """
        return self._request("getById", locals())

    def get_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        extended: bool = None,
        fields: list = None,
    ) -> dict:
        """
        Returns a comment on a post on a user wall or community wall.
        """
        return self._request("getComment", locals())

    def get_comments(
        self,
        owner_id: int = None,
        post_id: int = None,
        need_likes: bool = None,
        start_comment_id: int = None,
        offset: int = None,
        count: int = None,
        sort: str = None,
        preview_length: int = None,
        extended: bool = None,
        fields: list = None,
        comment_id: int = None,
        thread_items_count: int = None,
        # ? <= thread_items_count <= 10
    ) -> dict:
        """
        Returns a list of comments on a post on a user wall or community wall.
        """
        return self._request("getComments", locals())

    def get_reposts(
        self,
        owner_id: int = None,
        post_id: int = None,
        offset: int = None,
        count: int = None,
        # ? <= count <= 1000
    ) -> dict:
        """
        Returns information about reposts of a post on user wall or community wall.
        """
        return self._request("getReposts", locals())

    def open_comments(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        <null>
        """
        return self._request("openComments", locals())

    def pin(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        Pins the post on wall.
        """
        return self._request("pin", locals())

    def post(
        self,
        owner_id: int = None,
        friends_only: bool = None,
        from_group: bool = None,
        message: str = None,
        attachments: list = None,
        services: str = None,
        signed: bool = None,
        publish_date: int = None,
        lat: float = None,
        long: float = None,
        place_id: int = None,
        post_id: int = None,
        guid: str = None,
        mark_as_ads: bool = None,
        close_comments: bool = None,
        mute_notifications: bool = None,
        copyright: str = None,
    ) -> dict:
        """
        Adds a new post on a user wall or community wall. Can also be used to publish suggested or scheduled posts.
        """
        return self._request("post", locals())

    def post_ads_stealth(
        self,
        owner_id: int = None,
        message: str = None,
        attachments: list = None,
        signed: bool = None,
        lat: float = None,
        long: float = None,
        place_id: int = None,
        guid: str = None,
        link_button: str = None,
        link_title: str = None,
        link_image: str = None,
        link_video: str = None,
    ) -> dict:
        """
        Allows to create hidden post which will not be shown on the community's wall and can be used for creating an ad with type "Community post".
        """
        return self._request("postAdsStealth", locals())

    def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: int = None,
    ) -> dict:
        """
        Reports (submits a complaint about) a comment on a post on a user wall or community wall.
        """
        return self._request("reportComment", locals())

    def report_post(
        self,
        owner_id: int = None,
        post_id: int = None,
        reason: int = None,
    ) -> dict:
        """
        Reports (submits a complaint about) a post on a user wall or community wall.
        """
        return self._request("reportPost", locals())

    def repost(
        self,
        object: str = None,
        message: str = None,
        group_id: int = None,
        mark_as_ads: bool = None,
        mute_notifications: bool = None,
    ) -> dict:
        """
        Reposts (copies) an object to a user wall or community wall.
        """
        return self._request("repost", locals())

    def restore(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        Restores a post deleted from a user wall or community wall.
        """
        return self._request("restore", locals())

    def restore_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
    ) -> dict:
        """
        Restores a comment deleted from a user wall or community wall.
        """
        return self._request("restoreComment", locals())

    def search(
        self,
        owner_id: int = None,
        domain: str = None,
        query: str = None,
        owners_only: bool = None,
        count: int = None,
        # ? <= count <= 100
        offset: int = None,
        extended: bool = None,
        fields: list = None,
    ) -> dict:
        """
        Allows to search posts on user or community walls.
        """
        return self._request("search", locals())

    def unpin(
        self,
        owner_id: int = None,
        post_id: int = None,
    ) -> dict:
        """
        Unpins the post on wall.
        """
        return self._request("unpin", locals())


# generated at 2020.11.08 08:32:23

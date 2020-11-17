# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Wall(Category):

    def close_comments(
        self,
        owner_id: int = None,
        post_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("closeComments", locals())

    def create_comment(
        self,
        owner_id: Optional[int] = None,
        post_id: int = None,
        from_group: Optional[int] = None,
        message: Optional[str] = None,
        reply_to_comment: Optional[int] = None,
        attachments: Optional[list] = None,
        sticker_id: Optional[int] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createComment", locals())

    def delete(
        self,
        owner_id: Optional[int] = None,
        post_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteComment", locals())

    def edit(
        self,
        owner_id: Optional[int] = None,
        post_id: int = None,
        friends_only: Optional[bool] = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        services: Optional[str] = None,
        signed: Optional[bool] = None,
        publish_date: Optional[int] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        place_id: Optional[int] = None,
        mark_as_ads: Optional[bool] = None,
        close_comments: Optional[bool] = None,
        poster_bkg_id: Optional[int] = None,
        poster_bkg_owner_id: Optional[int] = None,
        poster_bkg_access_hash: Optional[str] = None,
        copyright: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_ads_stealth(
        self,
        owner_id: Optional[int] = None,
        post_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        signed: Optional[bool] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        place_id: Optional[int] = None,
        link_button: Optional[str] = None,
        link_title: Optional[str] = None,
        link_image: Optional[str] = None,
        link_video: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("editAdsStealth", locals())

    def edit_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editComment", locals())

    def get(
        self,
        owner_id: Optional[int] = None,
        domain: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        filter: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_by_id(
        self,
        posts: list = None,
        extended: Optional[bool] = None,
        copy_history_depth: Optional[int] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getComment", locals())

    def get_comments(
        self,
        owner_id: Optional[int] = None,
        post_id: Optional[int] = None,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[str] = None,
        preview_length: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        comment_id: Optional[int] = None,
        thread_items_count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def get_reposts(
        self,
        owner_id: Optional[int] = None,
        post_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getReposts", locals())

    def open_comments(
        self,
        owner_id: int = None,
        post_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("openComments", locals())

    def pin(
        self,
        owner_id: Optional[int] = None,
        post_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("pin", locals())

    def post(
        self,
        owner_id: Optional[int] = None,
        friends_only: Optional[bool] = None,
        from_group: Optional[bool] = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        services: Optional[str] = None,
        signed: Optional[bool] = None,
        publish_date: Optional[int] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        place_id: Optional[int] = None,
        post_id: Optional[int] = None,
        guid: Optional[str] = None,
        mark_as_ads: Optional[bool] = None,
        close_comments: Optional[bool] = None,
        mute_notifications: Optional[bool] = None,
        copyright: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("post", locals())

    def post_ads_stealth(
        self,
        owner_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        signed: Optional[bool] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        place_id: Optional[int] = None,
        guid: Optional[str] = None,
        link_button: Optional[str] = None,
        link_title: Optional[str] = None,
        link_image: Optional[str] = None,
        link_video: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("postAdsStealth", locals())

    def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reportComment", locals())

    def report_post(
        self,
        owner_id: int = None,
        post_id: int = None,
        reason: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reportPost", locals())

    def repost(
        self,
        object: str = None,
        message: Optional[str] = None,
        group_id: Optional[int] = None,
        mark_as_ads: Optional[bool] = None,
        mute_notifications: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("repost", locals())

    def restore(
        self,
        owner_id: Optional[int] = None,
        post_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("restore", locals())

    def restore_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("restoreComment", locals())

    def search(
        self,
        owner_id: Optional[int] = None,
        domain: Optional[str] = None,
        query: Optional[str] = None,
        owners_only: Optional[bool] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

    def unpin(
        self,
        owner_id: Optional[int] = None,
        post_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("unpin", locals())

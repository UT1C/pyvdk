# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Stories(Category):

    def ban_owner(
        self,
        owners_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("banOwner", locals())

    def delete(
        self,
        owner_id: int = None,
        story_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def get(
        self,
        owner_id: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_banned(
        self,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getBanned", locals())

    def get_by_id(
        self,
        stories: list = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_photo_upload_server(
        self,
        add_to_news: Optional[bool] = None,
        user_ids: Optional[list] = None,
        reply_to_story: Optional[str] = None,
        link_text: Optional[str] = None,
        link_url: Optional[str] = None,
        group_id: Optional[int] = None,
        clickable_stickers: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getPhotoUploadServer", locals())

    def get_replies(
        self,
        owner_id: int = None,
        story_id: int = None,
        access_key: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getReplies", locals())

    def get_stats(
        self,
        owner_id: int = None,
        story_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getStats", locals())

    def get_video_upload_server(
        self,
        add_to_news: Optional[bool] = None,
        user_ids: Optional[list] = None,
        reply_to_story: Optional[str] = None,
        link_text: Optional[str] = None,
        link_url: Optional[str] = None,
        group_id: Optional[int] = None,
        clickable_stickers: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getVideoUploadServer", locals())

    def get_viewers(
        self,
        owner_id: int = None,
        story_id: int = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getViewers", locals())

    def hide_all_replies(
        self,
        owner_id: int = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("hideAllReplies", locals())

    def hide_reply(
        self,
        owner_id: int = None,
        story_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("hideReply", locals())

    def search(
        self,
        q: Optional[str] = None,
        place_id: Optional[int] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        radius: Optional[int] = None,
        mentioned_id: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

    def unban_owner(
        self,
        owners_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("unbanOwner", locals())

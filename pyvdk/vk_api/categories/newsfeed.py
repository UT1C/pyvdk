# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Newsfeed(Category):

    def add_ban(
        self,
        user_ids: Optional[list] = None,
        group_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("addBan", locals())

    def delete_ban(
        self,
        user_ids: Optional[list] = None,
        group_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("deleteBan", locals())

    def delete_list(
        self,
        list_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteList", locals())

    def get(
        self,
        filters: Optional[list] = None,
        return_banned: Optional[bool] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        max_photos: Optional[int] = None,
        source_ids: Optional[str] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        section: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_banned(
        self,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getBanned", locals())

    def get_comments(
        self,
        count: Optional[int] = None,
        filters: Optional[list] = None,
        reposts: Optional[str] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        last_comments_count: Optional[int] = None,
        start_from: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def get_lists(
        self,
        list_ids: Optional[list] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getLists", locals())

    def get_mentions(
        self,
        owner_id: Optional[int] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getMentions", locals())

    def get_recommended(
        self,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        max_photos: Optional[int] = None,
        start_from: Optional[str] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getRecommended", locals())

    def get_suggested_sources(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        shuffle: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getSuggestedSources", locals())

    def ignore_item(
        self,
        type: str = None,
        owner_id: int = None,
        item_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("ignoreItem", locals())

    def save_list(
        self,
        list_id: Optional[int] = None,
        title: str = None,
        source_ids: Optional[list] = None,
        no_reposts: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("saveList", locals())

    def search(
        self,
        q: Optional[str] = None,
        extended: Optional[bool] = None,
        count: Optional[int] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        start_from: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

    def unignore_item(
        self,
        type: str = None,
        owner_id: int = None,
        item_id: int = None,
        track_code: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("unignoreItem", locals())

    def unsubscribe(
        self,
        type: str = None,
        owner_id: Optional[int] = None,
        item_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("unsubscribe", locals())

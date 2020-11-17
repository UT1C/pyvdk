# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Likes(Category):

    def add(
        self,
        type: str = None,
        owner_id: Optional[int] = None,
        item_id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def delete(
        self,
        type: str = None,
        owner_id: Optional[int] = None,
        item_id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def get_list(
        self,
        type: str = None,
        owner_id: Optional[int] = None,
        item_id: Optional[int] = None,
        page_url: Optional[str] = None,
        filter: Optional[str] = None,
        friends_only: Optional[int] = None,
        extended: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        skip_own: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getList", locals())

    def is_liked(
        self,
        user_id: Optional[int] = None,
        type: str = None,
        owner_id: Optional[int] = None,
        item_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("isLiked", locals())

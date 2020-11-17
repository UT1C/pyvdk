# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Apps(Category):

    def delete_app_requests(
        self,
        **kwargs
    ) -> dict:
        return self._request("deleteAppRequests", locals())

    def get(
        self,
        app_id: Optional[int] = None,
        app_ids: Optional[list] = None,
        platform: Optional[str] = None,
        extended: Optional[bool] = None,
        return_friends: Optional[bool] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_catalog(
        self,
        sort: Optional[str] = None,
        offset: Optional[int] = None,
        count: int = None,
        platform: Optional[str] = None,
        extended: Optional[bool] = None,
        return_friends: Optional[bool] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        q: Optional[str] = None,
        genre_id: Optional[int] = None,
        filter: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getCatalog", locals())

    def get_friends_list(
        self,
        extended: Optional[bool] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        type: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getFriendsList", locals())

    def get_leaderboard(
        self,
        type: str = None,
        global_: Optional[bool] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getLeaderboard", locals())

    def get_scopes(
        self,
        type: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getScopes", locals())

    def get_score(
        self,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getScore", locals())

    def promo_has_active_gift(
        self,
        promo_id: int = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("promoHasActiveGift", locals())

    def promo_use_gift(
        self,
        promo_id: int = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("promoUseGift", locals())

    def send_request(
        self,
        user_id: int = None,
        text: Optional[str] = None,
        type: Optional[str] = None,
        name: Optional[str] = None,
        key: Optional[str] = None,
        separate: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("sendRequest", locals())

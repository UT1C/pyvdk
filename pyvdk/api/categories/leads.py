# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Leads(Category):

    def check_user(
        self,
        lead_id: int = None,
        test_result: Optional[int] = None,
        test_mode: Optional[bool] = None,
        auto_start: Optional[bool] = None,
        age: Optional[int] = None,
        country: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("checkUser", locals())

    def complete(
        self,
        vk_sid: str = None,
        secret: str = None,
        comment: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("complete", locals())

    def get_stats(
        self,
        lead_id: int = None,
        secret: Optional[str] = None,
        date_start: Optional[str] = None,
        date_end: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getStats", locals())

    def get_users(
        self,
        offer_id: int = None,
        secret: str = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        status: Optional[int] = None,
        reverse: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getUsers", locals())

    def metric_hit(
        self,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("metricHit", locals())

    def start(
        self,
        lead_id: int = None,
        secret: str = None,
        uid: Optional[int] = None,
        aid: Optional[int] = None,
        test_mode: Optional[bool] = None,
        force: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("start", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Notifications(Category):

    def get(
        self,
        count: Optional[int] = None,
        start_from: Optional[str] = None,
        filters: Optional[list] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def mark_as_viewed(
        self,
        **kwargs
    ) -> dict:
        return self._request("markAsViewed", locals())

    def send_message(
        self,
        user_ids: list = None,
        message: str = None,
        fragment: Optional[str] = None,
        group_id: Optional[int] = None,
        random_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("sendMessage", locals())

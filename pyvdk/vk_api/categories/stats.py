# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Stats(Category):

    def get(
        self,
        group_id: Optional[int] = None,
        app_id: Optional[int] = None,
        timestamp_from: Optional[int] = None,
        timestamp_to: Optional[int] = None,
        interval: Optional[str] = None,
        intervals_count: Optional[int] = None,
        filters: Optional[list] = None,
        stats_groups: Optional[list] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_post_reach(
        self,
        owner_id: str = None,
        post_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("getPostReach", locals())

    def track_visitor(
        self,
        id: str = None,
        **kwargs
    ) -> dict:
        return self._request("trackVisitor", locals())

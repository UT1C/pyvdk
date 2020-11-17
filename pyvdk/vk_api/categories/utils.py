# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Utils(Category):

    def check_link(
        self,
        url: str = None,
        **kwargs
    ) -> dict:
        return self._request("checkLink", locals())

    def delete_from_last_shortened(
        self,
        key: str = None,
        **kwargs
    ) -> dict:
        return self._request("deleteFromLastShortened", locals())

    def get_last_shortened_links(
        self,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getLastShortenedLinks", locals())

    def get_link_stats(
        self,
        key: str = None,
        source: Optional[str] = None,
        access_key: Optional[str] = None,
        interval: Optional[str] = None,
        intervals_count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getLinkStats", locals())

    def get_server_time(
        self,
        **kwargs
    ) -> dict:
        return self._request("getServerTime", locals())

    def get_short_link(
        self,
        url: str = None,
        private: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getShortLink", locals())

    def resolve_screen_name(
        self,
        screen_name: str = None,
        **kwargs
    ) -> dict:
        return self._request("resolveScreenName", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Pages(Category):

    def clear_cache(
        self,
        url: str = None,
        **kwargs
    ) -> dict:
        return self._request("clearCache", locals())

    def get(
        self,
        owner_id: Optional[int] = None,
        page_id: Optional[int] = None,
        global_: Optional[bool] = None,
        site_preview: Optional[bool] = None,
        title: Optional[str] = None,
        need_source: Optional[bool] = None,
        need_html: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_history(
        self,
        page_id: int = None,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getHistory", locals())

    def get_titles(
        self,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getTitles", locals())

    def get_version(
        self,
        version_id: int = None,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        need_html: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getVersion", locals())

    def parse_wiki(
        self,
        text: str = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("parseWiki", locals())

    def save(
        self,
        text: Optional[str] = None,
        page_id: Optional[int] = None,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        title: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("save", locals())

    def save_access(
        self,
        page_id: int = None,
        group_id: Optional[int] = None,
        user_id: Optional[int] = None,
        view: Optional[int] = None,
        edit: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("saveAccess", locals())

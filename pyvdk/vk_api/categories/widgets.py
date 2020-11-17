# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Widgets(Category):

    def get_comments(
        self,
        widget_api_id: Optional[int] = None,
        url: Optional[str] = None,
        page_id: Optional[str] = None,
        order: Optional[str] = None,
        fields: Optional[list] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def get_pages(
        self,
        widget_api_id: Optional[int] = None,
        order: Optional[str] = None,
        period: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getPages", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Search(Category):

    def get_hints(
        self,
        q: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        filters: Optional[list] = None,
        fields: Optional[list] = None,
        search_global: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getHints", locals())

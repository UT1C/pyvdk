# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class AppWidgets(Category):
    __name__: str = "appWidgets"


    def update(
        self,
        code: str = None,
        type: str = None,
        **kwargs
    ) -> dict:
        return self._request("update", locals())

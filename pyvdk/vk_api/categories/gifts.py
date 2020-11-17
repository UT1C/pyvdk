# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Gifts(Category):

    def get(
        self,
        user_id: Optional[int] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

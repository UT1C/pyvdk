# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Status(Category):

    def get(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def set(
        self,
        text: Optional[str] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("set", locals())

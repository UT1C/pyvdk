# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Storage(Category):

    def get(
        self,
        key: Optional[str] = None,
        keys: Optional[list] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_keys(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getKeys", locals())

    def set(
        self,
        key: str = None,
        value: Optional[str] = None,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("set", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Auth(Category):

    def check_phone(
        self,
        phone: str = None,
        client_id: Optional[int] = None,
        client_secret: Optional[str] = None,
        auth_by_phone: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("checkPhone", locals())

    def restore(
        self,
        phone: str = None,
        last_name: str = None,
        **kwargs
    ) -> dict:
        return self._request("restore", locals())

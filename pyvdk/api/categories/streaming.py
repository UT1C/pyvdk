# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Streaming(Category):

    def get_server_url(
        self,
        **kwargs
    ) -> dict:
        return self._request("getServerUrl", locals())

    def set_settings(
        self,
        monthly_tier: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("setSettings", locals())

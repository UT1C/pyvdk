# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class DownloadedGames(Category):
    __name__: str = "downloadedGames"


    def get_paid_status(
        self,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getPaidStatus", locals())

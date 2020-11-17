# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class PrettyCards(Category):
    __name__: str = "prettyCards"


    def create(
        self,
        owner_id: int = None,
        photo: str = None,
        title: str = None,
        link: str = None,
        price: Optional[str] = None,
        price_old: Optional[str] = None,
        button: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("create", locals())

    def delete(
        self,
        owner_id: int = None,
        card_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def edit(
        self,
        owner_id: int = None,
        card_id: int = None,
        photo: Optional[str] = None,
        title: Optional[str] = None,
        link: Optional[str] = None,
        price: Optional[str] = None,
        price_old: Optional[str] = None,
        button: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def get(
        self,
        owner_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_by_id(
        self,
        owner_id: int = None,
        card_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_upload_u_r_l(
        self,
        **kwargs
    ) -> dict:
        return self._request("getUploadURL", locals())

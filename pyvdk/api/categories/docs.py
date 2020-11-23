# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Docs(Category):

    def add(
        self,
        owner_id: int = None,
        doc_id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def delete(
        self,
        owner_id: int = None,
        doc_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def edit(
        self,
        owner_id: int = None,
        doc_id: int = None,
        title: Optional[str] = None,
        tags: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def get(
        self,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        type: Optional[int] = None,
        owner_id: Optional[int] = None,
        return_tags: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_by_id(
        self,
        docs: list = None,
        return_tags: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_messages_upload_server(
        self,
        type: Optional[str] = None,
        peer_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getMessagesUploadServer", locals())

    def get_types(
        self,
        owner_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getTypes", locals())

    def get_upload_server(
        self,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getUploadServer", locals())

    def get_wall_upload_server(
        self,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getWallUploadServer", locals())

    def save(
        self,
        file: str = None,
        title: Optional[str] = None,
        tags: Optional[str] = None,
        return_tags: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("save", locals())

    def search(
        self,
        q: str = None,
        search_own: Optional[bool] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        return_tags: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Notes(Category):

    def add(
        self,
        title: str = None,
        text: str = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def create_comment(
        self,
        note_id: int = None,
        owner_id: Optional[int] = None,
        reply_to: Optional[int] = None,
        message: str = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createComment", locals())

    def delete(
        self,
        note_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_comment(
        self,
        comment_id: int = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("deleteComment", locals())

    def edit(
        self,
        note_id: int = None,
        title: str = None,
        text: str = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_comment(
        self,
        comment_id: int = None,
        owner_id: Optional[int] = None,
        message: str = None,
        **kwargs
    ) -> dict:
        return self._request("editComment", locals())

    def get(
        self,
        note_ids: Optional[list] = None,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_by_id(
        self,
        note_id: int = None,
        owner_id: Optional[int] = None,
        need_wiki: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_comments(
        self,
        note_id: int = None,
        owner_id: Optional[int] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def restore_comment(
        self,
        comment_id: int = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("restoreComment", locals())

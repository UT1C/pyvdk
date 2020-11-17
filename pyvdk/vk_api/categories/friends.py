# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Friends(Category):

    def add(
        self,
        user_id: Optional[int] = None,
        text: Optional[str] = None,
        follow: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def add_list(
        self,
        name: str = None,
        user_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("addList", locals())

    def are_friends(
        self,
        user_ids: list = None,
        need_sign: Optional[bool] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("areFriends", locals())

    def delete(
        self,
        user_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_all_requests(
        self,
        **kwargs
    ) -> dict:
        return self._request("deleteAllRequests", locals())

    def delete_list(
        self,
        list_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteList", locals())

    def edit(
        self,
        user_id: int = None,
        list_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_list(
        self,
        name: Optional[str] = None,
        list_id: int = None,
        user_ids: Optional[list] = None,
        add_user_ids: Optional[list] = None,
        delete_user_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editList", locals())

    def get(
        self,
        user_id: Optional[int] = None,
        order: Optional[str] = None,
        list_id: Optional[int] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        ref: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_app_users(
        self,
        **kwargs
    ) -> dict:
        return self._request("getAppUsers", locals())

    def get_by_phones(
        self,
        phones: Optional[list] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getByPhones", locals())

    def get_lists(
        self,
        user_id: Optional[int] = None,
        return_system: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getLists", locals())

    def get_mutual(
        self,
        source_uid: Optional[int] = None,
        target_uid: Optional[int] = None,
        target_uids: Optional[list] = None,
        order: Optional[str] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getMutual", locals())

    def get_online(
        self,
        user_id: Optional[int] = None,
        list_id: Optional[int] = None,
        online_mobile: Optional[bool] = None,
        order: Optional[str] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getOnline", locals())

    def get_recent(
        self,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getRecent", locals())

    def get_requests(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        need_mutual: Optional[bool] = None,
        out: Optional[bool] = None,
        sort: Optional[int] = None,
        need_viewed: Optional[bool] = None,
        suggested: Optional[bool] = None,
        ref: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getRequests", locals())

    def get_suggestions(
        self,
        filter: Optional[list] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getSuggestions", locals())

    def search(
        self,
        user_id: int = None,
        q: Optional[str] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

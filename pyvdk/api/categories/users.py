# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Users(Category):

    def get(
        self,
        user_ids: Optional[list] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_followers(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getFollowers", locals())

    def get_subscriptions(
        self,
        user_id: Optional[int] = None,
        extended: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getSubscriptions", locals())

    def report(
        self,
        user_id: int = None,
        type: str = None,
        comment: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("report", locals())

    def search(
        self,
        q: Optional[str] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        city: Optional[int] = None,
        country: Optional[int] = None,
        hometown: Optional[str] = None,
        university_country: Optional[int] = None,
        university: Optional[int] = None,
        university_year: Optional[int] = None,
        university_faculty: Optional[int] = None,
        university_chair: Optional[int] = None,
        sex: Optional[int] = None,
        status: Optional[int] = None,
        age_from: Optional[int] = None,
        age_to: Optional[int] = None,
        birth_day: Optional[int] = None,
        birth_month: Optional[int] = None,
        birth_year: Optional[int] = None,
        online: Optional[bool] = None,
        has_photo: Optional[bool] = None,
        school_country: Optional[int] = None,
        school_city: Optional[int] = None,
        school_class: Optional[int] = None,
        school: Optional[int] = None,
        school_year: Optional[int] = None,
        religion: Optional[str] = None,
        company: Optional[str] = None,
        position: Optional[str] = None,
        group_id: Optional[int] = None,
        from_list: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Polls(Category):

    def add_vote(
        self,
        owner_id: Optional[int] = None,
        poll_id: int = None,
        answer_ids: list = None,
        is_board: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("addVote", locals())

    def create(
        self,
        question: Optional[str] = None,
        is_anonymous: Optional[bool] = None,
        is_multiple: Optional[bool] = None,
        end_date: Optional[int] = None,
        owner_id: Optional[int] = None,
        add_answers: Optional[str] = None,
        photo_id: Optional[int] = None,
        background_id: Optional[str] = None,
        disable_unvote: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("create", locals())

    def delete_vote(
        self,
        owner_id: Optional[int] = None,
        poll_id: int = None,
        answer_id: int = None,
        is_board: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("deleteVote", locals())

    def edit(
        self,
        owner_id: Optional[int] = None,
        poll_id: int = None,
        question: Optional[str] = None,
        add_answers: Optional[str] = None,
        edit_answers: Optional[str] = None,
        delete_answers: Optional[str] = None,
        end_date: Optional[int] = None,
        photo_id: Optional[int] = None,
        background_id: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def get_by_id(
        self,
        owner_id: Optional[int] = None,
        is_board: Optional[bool] = None,
        poll_id: int = None,
        extended: Optional[bool] = None,
        friends_count: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_voters(
        self,
        owner_id: Optional[int] = None,
        poll_id: int = None,
        answer_ids: list = None,
        is_board: Optional[bool] = None,
        friends_only: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[list] = None,
        name_case: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getVoters", locals())

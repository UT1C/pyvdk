# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Board(Category):

    def add_topic(
        self,
        group_id: int = None,
        title: str = None,
        text: Optional[str] = None,
        from_group: Optional[bool] = None,
        attachments: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("addTopic", locals())

    def close_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("closeTopic", locals())

    def create_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        from_group: Optional[bool] = None,
        sticker_id: Optional[int] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createComment", locals())

    def delete_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteComment", locals())

    def delete_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteTopic", locals())

    def edit_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editComment", locals())

    def edit_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        title: str = None,
        **kwargs
    ) -> dict:
        return self._request("editTopic", locals())

    def fix_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("fixTopic", locals())

    def get_comments(
        self,
        group_id: int = None,
        topic_id: int = None,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        sort: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def get_topics(
        self,
        group_id: int = None,
        topic_ids: Optional[list] = None,
        order: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        preview: Optional[int] = None,
        preview_length: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getTopics", locals())

    def open_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("openTopic", locals())

    def restore_comment(
        self,
        group_id: int = None,
        topic_id: int = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("restoreComment", locals())

    def unfix_topic(
        self,
        group_id: int = None,
        topic_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("unfixTopic", locals())

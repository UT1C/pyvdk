# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Fave(Category):

    def add_article(
        self,
        url: str = None,
        **kwargs
    ) -> dict:
        return self._request("addArticle", locals())

    def add_link(
        self,
        link: str = None,
        **kwargs
    ) -> dict:
        return self._request("addLink", locals())

    def add_page(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("addPage", locals())

    def add_post(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addPost", locals())

    def add_product(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addProduct", locals())

    def add_tag(
        self,
        name: Optional[str] = None,
        position: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addTag", locals())

    def add_video(
        self,
        owner_id: int = None,
        id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("addVideo", locals())

    def edit_tag(
        self,
        id: int = None,
        name: str = None,
        **kwargs
    ) -> dict:
        return self._request("editTag", locals())

    def get(
        self,
        extended: Optional[bool] = None,
        item_type: Optional[str] = None,
        tag_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        fields: Optional[str] = None,
        is_from_snackbar: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_pages(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        type: Optional[str] = None,
        fields: Optional[list] = None,
        tag_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getPages", locals())

    def get_tags(
        self,
        **kwargs
    ) -> dict:
        return self._request("getTags", locals())

    def mark_seen(
        self,
        **kwargs
    ) -> dict:
        return self._request("markSeen", locals())

    def remove_article(
        self,
        owner_id: int = None,
        article_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeArticle", locals())

    def remove_link(
        self,
        link_id: Optional[str] = None,
        link: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("removeLink", locals())

    def remove_page(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("removePage", locals())

    def remove_post(
        self,
        owner_id: int = None,
        id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removePost", locals())

    def remove_product(
        self,
        owner_id: int = None,
        id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeProduct", locals())

    def remove_tag(
        self,
        id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeTag", locals())

    def reorder_tags(
        self,
        ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("reorderTags", locals())

    def set_page_tags(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        tag_ids: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("setPageTags", locals())

    def set_tags(
        self,
        item_type: Optional[str] = None,
        item_owner_id: Optional[int] = None,
        item_id: Optional[int] = None,
        tag_ids: Optional[list] = None,
        link_id: Optional[str] = None,
        link_url: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("setTags", locals())

    def track_page_interaction(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("trackPageInteraction", locals())

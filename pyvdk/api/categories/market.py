# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Market(Category):

    def add(
        self,
        owner_id: int = None,
        name: str = None,
        description: str = None,
        category_id: int = None,
        price: Optional[float] = None,
        old_price: Optional[float] = None,
        deleted: Optional[bool] = None,
        main_photo_id: int = None,
        photo_ids: Optional[list] = None,
        url: Optional[str] = None,
        dimension_width: Optional[int] = None,
        dimension_height: Optional[int] = None,
        dimension_length: Optional[int] = None,
        weight: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def add_album(
        self,
        owner_id: int = None,
        title: str = None,
        photo_id: Optional[int] = None,
        main_album: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("addAlbum", locals())

    def add_to_album(
        self,
        owner_id: int = None,
        item_id: int = None,
        album_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("addToAlbum", locals())

    def create_comment(
        self,
        owner_id: int = None,
        item_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        from_group: Optional[bool] = None,
        reply_to_comment: Optional[int] = None,
        sticker_id: Optional[int] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createComment", locals())

    def delete(
        self,
        owner_id: int = None,
        item_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_album(
        self,
        owner_id: int = None,
        album_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteAlbum", locals())

    def delete_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteComment", locals())

    def edit(
        self,
        owner_id: int = None,
        item_id: int = None,
        name: str = None,
        description: str = None,
        category_id: int = None,
        price: float = None,
        deleted: Optional[bool] = None,
        main_photo_id: int = None,
        photo_ids: Optional[list] = None,
        url: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_album(
        self,
        owner_id: int = None,
        album_id: int = None,
        title: str = None,
        photo_id: Optional[int] = None,
        main_album: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("editAlbum", locals())

    def edit_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editComment", locals())

    def get(
        self,
        owner_id: int = None,
        album_id: Optional[int] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_album_by_id(
        self,
        owner_id: int = None,
        album_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbumById", locals())

    def get_albums(
        self,
        owner_id: int = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbums", locals())

    def get_by_id(
        self,
        item_ids: list = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_categories(
        self,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getCategories", locals())

    def get_comments(
        self,
        owner_id: int = None,
        item_id: int = None,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def remove_from_album(
        self,
        owner_id: int = None,
        item_id: int = None,
        album_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("removeFromAlbum", locals())

    def reorder_albums(
        self,
        owner_id: int = None,
        album_id: int = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderAlbums", locals())

    def reorder_items(
        self,
        owner_id: int = None,
        album_id: Optional[int] = None,
        item_id: int = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderItems", locals())

    def report(
        self,
        owner_id: int = None,
        item_id: int = None,
        reason: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("report", locals())

    def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: int = None,
        **kwargs
    ) -> dict:
        return self._request("reportComment", locals())

    def restore(
        self,
        owner_id: int = None,
        item_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("restore", locals())

    def restore_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("restoreComment", locals())

    def search(
        self,
        owner_id: int = None,
        album_id: Optional[int] = None,
        q: Optional[str] = None,
        price_from: Optional[int] = None,
        price_to: Optional[int] = None,
        sort: Optional[int] = None,
        rev: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        status: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

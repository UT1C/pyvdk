# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Video(Category):

    def add(
        self,
        target_id: Optional[int] = None,
        video_id: int = None,
        owner_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("add", locals())

    def add_album(
        self,
        group_id: Optional[int] = None,
        title: Optional[str] = None,
        privacy: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("addAlbum", locals())

    def add_to_album(
        self,
        target_id: Optional[int] = None,
        album_id: Optional[int] = None,
        album_ids: Optional[list] = None,
        owner_id: int = None,
        video_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("addToAlbum", locals())

    def create_comment(
        self,
        owner_id: Optional[int] = None,
        video_id: int = None,
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
        video_id: int = None,
        owner_id: Optional[int] = None,
        target_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_album(
        self,
        group_id: Optional[int] = None,
        album_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteAlbum", locals())

    def delete_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteComment", locals())

    def edit(
        self,
        owner_id: Optional[int] = None,
        video_id: int = None,
        name: Optional[str] = None,
        desc: Optional[str] = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        no_comments: Optional[bool] = None,
        repeat: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_album(
        self,
        group_id: Optional[int] = None,
        album_id: int = None,
        title: str = None,
        privacy: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editAlbum", locals())

    def edit_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("editComment", locals())

    def get(
        self,
        owner_id: Optional[int] = None,
        videos: Optional[list] = None,
        album_id: Optional[int] = None,
        count: Optional[int] = None,
        offset: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_album_by_id(
        self,
        owner_id: Optional[int] = None,
        album_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbumById", locals())

    def get_albums(
        self,
        owner_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        need_system: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbums", locals())

    def get_albums_by_video(
        self,
        target_id: Optional[int] = None,
        owner_id: int = None,
        video_id: int = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbumsByVideo", locals())

    def get_comments(
        self,
        owner_id: Optional[int] = None,
        video_id: int = None,
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
        target_id: Optional[int] = None,
        album_id: Optional[int] = None,
        album_ids: Optional[list] = None,
        owner_id: int = None,
        video_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeFromAlbum", locals())

    def reorder_albums(
        self,
        owner_id: Optional[int] = None,
        album_id: int = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderAlbums", locals())

    def reorder_videos(
        self,
        target_id: Optional[int] = None,
        album_id: Optional[int] = None,
        owner_id: int = None,
        video_id: int = None,
        before_owner_id: Optional[int] = None,
        before_video_id: Optional[int] = None,
        after_owner_id: Optional[int] = None,
        after_video_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderVideos", locals())

    def report(
        self,
        owner_id: int = None,
        video_id: int = None,
        reason: Optional[int] = None,
        comment: Optional[str] = None,
        search_query: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("report", locals())

    def report_comment(
        self,
        owner_id: int = None,
        comment_id: int = None,
        reason: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reportComment", locals())

    def restore(
        self,
        video_id: int = None,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("restore", locals())

    def restore_comment(
        self,
        owner_id: Optional[int] = None,
        comment_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("restoreComment", locals())

    def save(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        is_private: Optional[bool] = None,
        wallpost: Optional[bool] = None,
        link: Optional[str] = None,
        group_id: Optional[int] = None,
        album_id: Optional[int] = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        no_comments: Optional[bool] = None,
        repeat: Optional[bool] = None,
        compression: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("save", locals())

    def search(
        self,
        q: str = None,
        sort: Optional[int] = None,
        hd: Optional[int] = None,
        adult: Optional[bool] = None,
        filters: Optional[list] = None,
        search_own: Optional[bool] = None,
        offset: Optional[int] = None,
        longer: Optional[int] = None,
        shorter: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

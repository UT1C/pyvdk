# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Photos(Category):

    def confirm_tag(
        self,
        owner_id: Optional[int] = None,
        photo_id: str = None,
        tag_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("confirmTag", locals())

    def copy(
        self,
        owner_id: int = None,
        photo_id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("copy", locals())

    def create_album(
        self,
        title: str = None,
        group_id: Optional[int] = None,
        description: Optional[str] = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        upload_by_admins_only: Optional[bool] = None,
        comments_disabled: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("createAlbum", locals())

    def create_comment(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        message: Optional[str] = None,
        attachments: Optional[list] = None,
        from_group: Optional[bool] = None,
        reply_to_comment: Optional[int] = None,
        sticker_id: Optional[int] = None,
        access_key: Optional[str] = None,
        guid: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createComment", locals())

    def delete(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("delete", locals())

    def delete_album(
        self,
        album_id: int = None,
        group_id: Optional[int] = None,
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
        photo_id: int = None,
        caption: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        place_str: Optional[str] = None,
        foursquare_id: Optional[str] = None,
        delete_place: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("edit", locals())

    def edit_album(
        self,
        album_id: int = None,
        title: Optional[str] = None,
        description: Optional[str] = None,
        owner_id: Optional[int] = None,
        privacy_view: Optional[list] = None,
        privacy_comment: Optional[list] = None,
        upload_by_admins_only: Optional[bool] = None,
        comments_disabled: Optional[bool] = None,
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
        album_id: Optional[str] = None,
        photo_ids: Optional[list] = None,
        rev: Optional[bool] = None,
        extended: Optional[bool] = None,
        feed_type: Optional[str] = None,
        feed: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_albums(
        self,
        owner_id: Optional[int] = None,
        album_ids: Optional[list] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        need_system: Optional[bool] = None,
        need_covers: Optional[bool] = None,
        photo_sizes: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbums", locals())

    def get_albums_count(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAlbumsCount", locals())

    def get_all(
        self,
        owner_id: Optional[int] = None,
        extended: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        photo_sizes: Optional[bool] = None,
        no_service_albums: Optional[bool] = None,
        need_hidden: Optional[bool] = None,
        skip_hidden: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getAll", locals())

    def get_all_comments(
        self,
        owner_id: Optional[int] = None,
        album_id: Optional[int] = None,
        need_likes: Optional[bool] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAllComments", locals())

    def get_by_id(
        self,
        photos: list = None,
        extended: Optional[bool] = None,
        photo_sizes: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_chat_upload_server(
        self,
        chat_id: int = None,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getChatUploadServer", locals())

    def get_comments(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        need_likes: Optional[bool] = None,
        start_comment_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        sort: Optional[str] = None,
        access_key: Optional[str] = None,
        extended: Optional[bool] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getComments", locals())

    def get_market_album_upload_server(
        self,
        group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getMarketAlbumUploadServer", locals())

    def get_market_upload_server(
        self,
        group_id: int = None,
        main_photo: Optional[bool] = None,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_width: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getMarketUploadServer", locals())

    def get_messages_upload_server(
        self,
        peer_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getMessagesUploadServer", locals())

    def get_new_tags(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getNewTags", locals())

    def get_owner_cover_photo_upload_server(
        self,
        group_id: int = None,
        crop_x: Optional[int] = None,
        crop_y: Optional[int] = None,
        crop_x2: Optional[int] = None,
        crop_y2: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getOwnerCoverPhotoUploadServer", locals())

    def get_owner_photo_upload_server(
        self,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getOwnerPhotoUploadServer", locals())

    def get_tags(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        access_key: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getTags", locals())

    def get_upload_server(
        self,
        group_id: Optional[int] = None,
        album_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getUploadServer", locals())

    def get_user_photos(
        self,
        user_id: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        extended: Optional[bool] = None,
        sort: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getUserPhotos", locals())

    def get_wall_upload_server(
        self,
        group_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getWallUploadServer", locals())

    def make_cover(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        album_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("makeCover", locals())

    def move(
        self,
        owner_id: Optional[int] = None,
        target_album_id: int = None,
        photo_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("move", locals())

    def put_tag(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        user_id: int = None,
        x: Optional[float] = None,
        y: Optional[float] = None,
        x2: Optional[float] = None,
        y2: Optional[float] = None,
        **kwargs
    ) -> dict:
        return self._request("putTag", locals())

    def remove_tag(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        tag_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("removeTag", locals())

    def reorder_albums(
        self,
        owner_id: Optional[int] = None,
        album_id: int = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderAlbums", locals())

    def reorder_photos(
        self,
        owner_id: Optional[int] = None,
        photo_id: int = None,
        before: Optional[int] = None,
        after: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("reorderPhotos", locals())

    def report(
        self,
        owner_id: int = None,
        photo_id: int = None,
        reason: Optional[int] = None,
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
        owner_id: Optional[int] = None,
        photo_id: int = None,
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
        album_id: Optional[int] = None,
        group_id: Optional[int] = None,
        server: Optional[int] = None,
        photos_list: Optional[str] = None,
        hash: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        caption: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("save", locals())

    def save_market_album_photo(
        self,
        group_id: int = None,
        photo: str = None,
        server: int = None,
        hash: str = None,
        **kwargs
    ) -> dict:
        return self._request("saveMarketAlbumPhoto", locals())

    def save_market_photo(
        self,
        group_id: Optional[int] = None,
        photo: str = None,
        server: int = None,
        hash: str = None,
        crop_data: Optional[str] = None,
        crop_hash: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("saveMarketPhoto", locals())

    def save_messages_photo(
        self,
        photo: str = None,
        server: Optional[int] = None,
        hash: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("saveMessagesPhoto", locals())

    def save_owner_cover_photo(
        self,
        hash: str = None,
        photo: str = None,
        **kwargs
    ) -> dict:
        return self._request("saveOwnerCoverPhoto", locals())

    def save_owner_photo(
        self,
        server: Optional[str] = None,
        hash: Optional[str] = None,
        photo: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("saveOwnerPhoto", locals())

    def save_wall_photo(
        self,
        user_id: Optional[int] = None,
        group_id: Optional[int] = None,
        photo: str = None,
        server: Optional[int] = None,
        hash: Optional[str] = None,
        latitude: Optional[float] = None,
        longitude: Optional[float] = None,
        caption: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("saveWallPhoto", locals())

    def search(
        self,
        q: Optional[str] = None,
        lat: Optional[float] = None,
        long: Optional[float] = None,
        start_time: Optional[int] = None,
        end_time: Optional[int] = None,
        sort: Optional[int] = None,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        radius: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("search", locals())

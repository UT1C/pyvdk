from abc import ABC
from io import BytesIO
from pathlib import Path
from typing import Union

from .abc import ABCUploader


class PhotoUploader(ABCUploader, ABC):
    NAME = "picture.jpg"


class PhotoToAlbumUploader(PhotoUploader):
    def upload(self, *args, **kwargs):
        # TODO
        raise NotImplementedError()


class PhotoWallUploader(PhotoUploader):
    def upload(self, *args, **kwargs):
        # TODO
        raise NotImplementedError()


class PhotoFaviconUploader(PhotoUploader):
    def upload(self, *args, **kwargs):
        # TODO
        raise NotImplementedError()


class PhotoMessageUploader(PhotoUploader):

    def get_server(self, **kwargs) -> dict:
        return self.api.request(
            "photos.getMessagesUploadServer",
            kwargs
        )["response"]

    def upload(self, thing: Union[str, Path, BytesIO], **params):
        server = self.get_server(**params)
        uploaded = self._upload(thing, server["upload_url"])

        result = self.api.request(
            "photos.saveMessagesPhoto",
            {**uploaded, **params}
        )["response"]

        return self.Result("photo", result)


class PhotoChatFaviconUploader(PhotoUploader):
    def upload(self, *args, **kwargs):
        # TODO
        raise NotImplementedError()


class PhotoMarketUploader(PhotoUploader):
    def upload(self, *args, **kwargs):
        # TODO
        raise NotImplementedError()


__all__ = (
    "PhotoUploader",
    "PhotoToAlbumUploader",
    "PhotoWallUploader",
    "PhotoFaviconUploader",
    "PhotoMessageUploader",
    "PhotoChatFaviconUploader",
    "PhotoMarketUploader",
)

from abc import ABC, abstractmethod
from typing import Optional, Union
from pathlib import Path
from io import BytesIO

from ..api import ABCAPI


class Result:
    type: str
    attachstr: Optional[str]
    json: dict

    def __init__(self, type: str, json: dict):
        self.type = type
        self.json = json

        try:
            self.attachstr = (
                f"{self.type}{self.json['owner_id']}"
                f"_{self.json['id']}"
            )
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            self.attachstr = None


class ABCUploader(ABC):

    # to make `Result` visible to inherited classes without imports
    Result = Result

    api: ABCAPI
    filename: Optional[str] = None

    def __init__(self, api: ABCAPI, filename: Optional[str] = None) -> None:
        self.api = api
        if filename is not None:
            self.filename = filename

    @abstractmethod
    def get_server(self, **kwargs):
        ...
    # method to get server url for file uploading

    @abstractmethod
    def upload(self, thing: Union[str, Path, BytesIO], **kwargs):
        ...
    # main public method

    def _post(self, url: str, **kwargs) -> dict:
        with self.api.session.post(url, **kwargs) as res:
            uploaded = res.json()
        return uploaded

    def _upload(self, thing: Union[str, Path, BytesIO], url: str):

        if isinstance(thing, (str, Path)):
            with Path(thing).open("rb") as fp:
                uploaded = self._post(url, files={"photo": fp})

        elif isinstance(thing, BytesIO):
            if thing.seekable():
                thing.seek(0)
            if getattr(thing, "name", None) is None and self.filename:
                thing.name = self.filename
            uploaded = self._post(url, files={"photo": thing})

        else:
            raise Exception(f"unexpected {thing!r} with type {thing.__class__}")

        return uploaded

    def __repr__(self) -> str:
        return f"<Uploader {self.__class__.__name__} with api {self.api!r}"


__all__ = (
    "Result",
    "ABCUploader",
)

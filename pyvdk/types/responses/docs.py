from typing import Optional, List

from ..objects import (
    DocsDocTypes,
    MessagesAudioMessage,
    MessagesGraffiti,
    DocsDocAttachmentType,
    DocsDoc,
    BaseUploadServer,
)
from ..abc import Model


class AddResponse(Model):
    response: Optional["AddResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetTypesResponse(Model):
    response: Optional["GetTypesResponseModel"] = None


class GetUploadServer(Model):
    response: Optional["GetUploadServerModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class SaveResponse(Model):
    response: Optional["SaveResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class AddResponseModel(Model):
    id: Optional[int] = None


GetByIdResponseModel = List[DocsDoc]


class GetTypesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DocsDocTypes"]] = None


GetUploadServerModel = Optional[BaseUploadServer]


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DocsDoc"]] = None


class SaveResponseModel(Model):
    type: Optional["DocsDocAttachmentType"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    graffiti: Optional["MessagesGraffiti"] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["DocsDoc"]] = None


AddResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetTypesResponse.update_forward_refs()
GetUploadServer.update_forward_refs()
GetResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()

from typing import Optional, List

from ..objects import (
    GroupsGroupFull,
    VideoSaveResult,
    UsersUserMin,
    WallWallComment,
    VideoVideo,
    VideoVideoFull,
    BaseBoolInt,
    VideoVideoAlbumFull,
)
from ..abc import Model


class AddAlbumResponse(Model):
    response: Optional["AddAlbumResponseModel"] = None


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class GetAlbumByIdResponse(Model):
    response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsByVideoExtendedResponse(Model):
    response: Optional["GetAlbumsByVideoExtendedResponseModel"] = None


class GetAlbumsByVideoResponse(Model):
    response: Optional["GetAlbumsByVideoResponseModel"] = None


class GetAlbumsExtendedResponse(Model):
    response: Optional["GetAlbumsExtendedResponseModel"] = None


class GetAlbumsResponse(Model):
    response: Optional["GetAlbumsResponseModel"] = None


class GetCommentsExtendedResponse(Model):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(Model):
    response: Optional["RestoreCommentResponseModel"] = None


class SaveResponse(Model):
    response: Optional["SaveResponseModel"] = None


class SearchExtendedResponse(Model):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(Model):
    album_id: Optional[int] = None


CreateCommentResponseModel = int

GetAlbumByIdResponseModel = Optional[VideoVideoAlbumFull]


class GetAlbumsByVideoExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideoAlbumFull"]] = None


GetAlbumsByVideoResponseModel = List[int]


class GetAlbumsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideoAlbumFull"]] = None


class GetAlbumsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideoAlbumFull"]] = None


class GetCommentsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideoFull"]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideo"]] = None


RestoreCommentResponseModel = Optional[BaseBoolInt]

SaveResponseModel = Optional[VideoSaveResult]


class SearchExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideo"]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["VideoVideo"]] = None


AddAlbumResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetAlbumByIdResponse.update_forward_refs()
GetAlbumsByVideoExtendedResponse.update_forward_refs()
GetAlbumsByVideoResponse.update_forward_refs()
GetAlbumsExtendedResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()

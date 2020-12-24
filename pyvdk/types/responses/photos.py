from typing import Optional, List

from ..objects import (
    PhotosPhotoTag,
    PhotosPhotoXtrTagInfo,
    GroupsGroupFull,
    PhotosCommentXtrPid,
    PhotosPhotoXtrRealOffset,
    WallWallComment,
    PhotosPhotoUpload,
    PhotosPhoto,
    PhotosPhotoFullXtrRealOffset,
    UsersUserFull,
    PhotosPhotoAlbumFull,
    PhotosPhotoFull,
    BaseBoolInt,
    BaseImage,
    BaseUploadServer,
)
from ..abc import Model


class CopyResponse(Model):
    response: Optional["CopyResponseModel"] = None


class CreateAlbumResponse(Model):
    response: Optional["CreateAlbumResponseModel"] = None


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(Model):
    response: Optional["DeleteCommentResponseModel"] = None


class GetAlbumsCountResponse(Model):
    response: Optional["GetAlbumsCountResponseModel"] = None


class GetAlbumsResponse(Model):
    response: Optional["GetAlbumsResponseModel"] = None


class GetAllCommentsResponse(Model):
    response: Optional["GetAllCommentsResponseModel"] = None


class GetAllExtendedResponse(Model):
    response: Optional["GetAllExtendedResponseModel"] = None


class GetAllResponse(Model):
    response: Optional["GetAllResponseModel"] = None


class GetByIdExtendedResponse(Model):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetCommentsExtendedResponse(Model):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetMarketUploadServerResponse(Model):
    response: Optional["GetMarketUploadServerResponseModel"] = None


class GetMessagesUploadServerResponse(Model):
    response: Optional["GetMessagesUploadServerResponseModel"] = None


class GetNewTagsResponse(Model):
    response: Optional["GetNewTagsResponseModel"] = None


class GetTagsResponse(Model):
    response: Optional["GetTagsResponseModel"] = None


class GetUploadServerResponse(Model):
    response: Optional["GetUploadServerResponseModel"] = None


class GetUserPhotosExtendedResponse(Model):
    response: Optional["GetUserPhotosExtendedResponseModel"] = None


class GetUserPhotosResponse(Model):
    response: Optional["GetUserPhotosResponseModel"] = None


class GetWallUploadServerResponse(Model):
    response: Optional["GetWallUploadServerResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class PutTagResponse(Model):
    response: Optional["PutTagResponseModel"] = None


class RestoreCommentResponse(Model):
    response: Optional["RestoreCommentResponseModel"] = None


class SaveMarketAlbumPhotoResponse(Model):
    response: Optional["SaveMarketAlbumPhotoResponseModel"] = None


class SaveMarketPhotoResponse(Model):
    response: Optional["SaveMarketPhotoResponseModel"] = None


class SaveMessagesPhotoResponse(Model):
    response: Optional["SaveMessagesPhotoResponseModel"] = None


class SaveOwnerCoverPhotoResponse(Model):
    response: Optional["SaveOwnerCoverPhotoResponseModel"] = None


class SaveOwnerPhotoResponse(Model):
    response: Optional["SaveOwnerPhotoResponseModel"] = None


class SaveWallPhotoResponse(Model):
    response: Optional["SaveWallPhotoResponseModel"] = None


class SaveResponse(Model):
    response: Optional["SaveResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


CopyResponseModel = int

CreateAlbumResponseModel = Optional[PhotosPhotoAlbumFull]

CreateCommentResponseModel = int

DeleteCommentResponseModel = Optional[BaseBoolInt]


GetAlbumsCountResponseModel = int


class GetAlbumsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoAlbumFull"]] = None


class GetAllCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosCommentXtrPid"]] = None


class GetAllExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFullXtrRealOffset"]] = None
    more: Optional["BaseBoolInt"] = None


class GetAllResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoXtrRealOffset"]] = None
    more: Optional["BaseBoolInt"] = None


GetByIdExtendedResponseModel = List[PhotosPhotoFull]

GetByIdResponseModel = List[PhotosPhoto]


class GetCommentsExtendedResponseModel(Model):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    real_offset: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None


GetMarketUploadServerResponseModel = Optional[BaseUploadServer]

GetMessagesUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetNewTagsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoXtrTagInfo"]] = None


GetTagsResponseModel = List[PhotosPhotoTag]

GetUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetUserPhotosExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFull"]] = None


class GetUserPhotosResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


GetWallUploadServerResponseModel = Optional[PhotosPhotoUpload]


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhotoFull"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


PutTagResponseModel = int

RestoreCommentResponseModel = Optional[BaseBoolInt]

SaveMarketAlbumPhotoResponseModel = List[PhotosPhoto]

SaveMarketPhotoResponseModel = List[PhotosPhoto]

SaveMessagesPhotoResponseModel = List[PhotosPhoto]

SaveOwnerCoverPhotoResponseModel = List[BaseImage]


class SaveOwnerPhotoResponseModel(Model):
    photo_hash: Optional[str] = None
    photo_src: Optional[str] = None
    photo_src_big: Optional[str] = None
    photo_src_small: Optional[str] = None
    saved: Optional[int] = None
    post_id: Optional[int] = None


SaveWallPhotoResponseModel = List[PhotosPhoto]

SaveResponseModel = List[PhotosPhoto]


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PhotosPhoto"]] = None


CopyResponse.update_forward_refs()
CreateAlbumResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumsCountResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetAllCommentsResponse.update_forward_refs()
GetAllExtendedResponse.update_forward_refs()
GetAllResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetMarketUploadServerResponse.update_forward_refs()
GetMessagesUploadServerResponse.update_forward_refs()
GetNewTagsResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
GetUserPhotosExtendedResponse.update_forward_refs()
GetUserPhotosResponse.update_forward_refs()
GetWallUploadServerResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
PutTagResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SaveMarketAlbumPhotoResponse.update_forward_refs()
SaveMarketPhotoResponse.update_forward_refs()
SaveMessagesPhotoResponse.update_forward_refs()
SaveOwnerCoverPhotoResponse.update_forward_refs()
SaveOwnerPhotoResponse.update_forward_refs()
SaveWallPhotoResponse.update_forward_refs()
SaveResponse.update_forward_refs()
SearchResponse.update_forward_refs()

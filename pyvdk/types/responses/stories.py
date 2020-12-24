from typing import Optional, List

from ..objects import (
    GroupsGroupFull,
    StoriesViewersItem,
    StoriesStoryStats,
    UsersUser,
    UsersUserFull,
    GroupsGroup,
    StoriesStory,
    StoriesFeedItem,
    StoriesPromoBlock,
)
from ..abc import Model


class GetBannedExtendedResponse(Model):
    response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(Model):
    response: Optional["GetBannedResponseModel"] = None


class GetByIdExtendedResponse(Model):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetPhotoUploadServerResponse(Model):
    response: Optional["GetPhotoUploadServerResponseModel"] = None


class GetStatsResponse(Model):
    response: Optional["GetStatsResponseModel"] = None


class GetVideoUploadServerResponse(Model):
    response: Optional["GetVideoUploadServerResponseModel"] = None


class GetViewersExtendedV5115Response(Model):
    response: Optional["GetViewersExtendedV5115ResponseModel"] = None


class GetViewersExtendedResponse(Model):
    response: Optional["GetViewersExtendedResponseModel"] = None


class GetV5113Response(Model):
    response: Optional["GetV5113ResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class UploadResponse(Model):
    response: Optional["UploadResponseModel"] = None


class GetBannedExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetBannedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetByIdExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["StoriesStory"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetByIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["StoriesStory"]] = None


class GetPhotoUploadServerResponseModel(Model):
    upload_url: Optional[str] = None
    user_ids: Optional[List[int]] = None


GetStatsResponseModel = Optional[StoriesStoryStats]


class GetVideoUploadServerResponseModel(Model):
    upload_url: Optional[str] = None
    user_ids: Optional[List[int]] = None


class GetViewersExtendedV5115ResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["StoriesViewersItem"]] = None
    hidden_reason: Optional[str] = None


class GetViewersExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetV5113ResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["StoriesFeedItem"]] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None
    need_upload_screen: Optional[bool] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[List["StoriesStory"]]] = None
    promo_data: Optional["StoriesPromoBlock"] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None
    need_upload_screen: Optional[bool] = None


class UploadResponseModel(Model):
    upload_result: Optional[str] = None


GetBannedExtendedResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetPhotoUploadServerResponse.update_forward_refs()
GetStatsResponse.update_forward_refs()
GetVideoUploadServerResponse.update_forward_refs()
GetViewersExtendedV5115Response.update_forward_refs()
GetViewersExtendedResponse.update_forward_refs()
GetV5113Response.update_forward_refs()
GetResponse.update_forward_refs()
UploadResponse.update_forward_refs()

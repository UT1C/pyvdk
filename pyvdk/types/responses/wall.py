from typing import Optional, List

from ..objects import (
    GroupsGroupFull,
    WallWallComment,
    UsersUser,
    UsersUserFull,
    GroupsGroup,
    WallWallpostFull,
)
from ..abc import Model


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class EditResponse(Model):
    response: Optional["EditResponseModel"] = None


class GetByIdExtendedResponse(Model):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetCommentExtendedResponse(Model):
    response: Optional["GetCommentExtendedResponseModel"] = None


class GetCommentResponse(Model):
    response: Optional["GetCommentResponseModel"] = None


class GetCommentsExtendedResponse(Model):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetRepostsResponse(Model):
    response: Optional["GetRepostsResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class PostAdsStealthResponse(Model):
    response: Optional["PostAdsStealthResponseModel"] = None


class PostResponse(Model):
    response: Optional["PostResponseModel"] = None


class RepostResponse(Model):
    response: Optional["RepostResponseModel"] = None


class SearchExtendedResponse(Model):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class CreateCommentResponseModel(Model):
    comment_id: Optional[int] = None


class EditResponseModel(Model):
    post_id: Optional[int] = None


class GetByIdExtendedResponseModel(Model):
    items: Optional[List["WallWallpostFull"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


GetByIdResponseModel = List[WallWallpostFull]


class GetCommentExtendedResponseModel(Model):
    items: Optional[List["WallWallComment"]] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetCommentResponseModel(Model):
    items: Optional[List["WallWallComment"]] = None


class GetCommentsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None
    show_reply_button: Optional[bool] = None
    can_post: Optional[bool] = None
    groups_can_post: Optional[bool] = None
    current_level_count: Optional[int] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None
    can_post: Optional[bool] = None
    groups_can_post: Optional[bool] = None
    current_level_count: Optional[int] = None


class GetRepostsResponseModel(Model):
    items: Optional[List["WallWallpostFull"]] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallpostFull"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallpostFull"]] = None


class PostAdsStealthResponseModel(Model):
    post_id: Optional[int] = None


class PostResponseModel(Model):
    post_id: Optional[int] = None


class RepostResponseModel(Model):
    success: Optional[int] = None
    post_id: Optional[int] = None
    reposts_count: Optional[int] = None
    likes_count: Optional[int] = None


class SearchExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallpostFull"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallpostFull"]] = None


CreateCommentResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentExtendedResponse.update_forward_refs()
GetCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetRepostsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
PostAdsStealthResponse.update_forward_refs()
PostResponse.update_forward_refs()
RepostResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()

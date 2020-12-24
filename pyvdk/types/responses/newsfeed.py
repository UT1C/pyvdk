from typing import Optional, List, Union

from ..objects import (
    GroupsGroupFull,
    NewsfeedNewsfeedItem,
    WallWallpostToId,
    UsersUserFull,
    UsersUserXtrType,
    WallWallpostFull,
    NewsfeedListFull,
    NewsfeedList,
)
from ..abc import Model


class GetBannedExtendedResponse(Model):
    response: Optional["GetBannedExtendedResponseModel"] = None


class GetBannedResponse(Model):
    response: Optional["GetBannedResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetListsExtendedResponse(Model):
    response: Optional["GetListsExtendedResponseModel"] = None


class GetListsResponse(Model):
    response: Optional["GetListsResponseModel"] = None


class GetMentionsResponse(Model):
    response: Optional["GetMentionsResponseModel"] = None


class GetRecommendedResponse(Model):
    response: Optional["GetRecommendedResponseModel"] = None


class GetSuggestedSourcesResponse(Model):
    response: Optional["GetSuggestedSourcesResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class SaveListResponse(Model):
    response: Optional["SaveListResponseModel"] = None


class SearchExtendedResponse(Model):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class GetBannedExtendedResponseModel(Model):
    groups: Optional[List["UsersUserFull"]] = None
    profiles: Optional[List["GroupsGroupFull"]] = None


class GetBannedResponseModel(Model):
    groups: Optional[List[int]] = None
    members: Optional[List[int]] = None


class GetCommentsResponseModel(Model):
    items: Optional[List["NewsfeedNewsfeedItem"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None
    next_from: Optional[str] = None


class GetListsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["NewsfeedListFull"]] = None


class GetListsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["NewsfeedList"]] = None


class GetMentionsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallpostToId"]] = None


class GetRecommendedResponseModel(Model):
    items: Optional[List["NewsfeedNewsfeedItem"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None
    new_offset: Optional[str] = None
    next_from: Optional[str] = None


class GetSuggestedSourcesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[Union["GroupsGroupFull", "UsersUserXtrType"]] = None


class GetResponseModel(Model):
    items: Optional[List["NewsfeedNewsfeedItem"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None
    next_from: Optional[str] = None


SaveListResponseModel = int


class SearchExtendedResponseModel(Model):
    items: Optional[List["WallWallpostFull"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None
    suggested_queries: Optional[List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None


class SearchResponseModel(Model):
    items: Optional[List["WallWallpostFull"]] = None
    suggested_queries: Optional[List[str]] = None
    next_from: Optional[str] = None
    count: Optional[int] = None
    total_count: Optional[int] = None


GetBannedExtendedResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetListsExtendedResponse.update_forward_refs()
GetListsResponse.update_forward_refs()
GetMentionsResponse.update_forward_refs()
GetRecommendedResponse.update_forward_refs()
GetSuggestedSourcesResponse.update_forward_refs()
GetResponse.update_forward_refs()
SaveListResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()

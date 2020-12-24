from typing import Optional, List

from ..objects import (
    FaveBookmark,
    UsersUserFull,
    GroupsGroup,
    FaveTag,
    FavePage,
)
from ..abc import Model


class AddTagResponse(Model):
    response: Optional["AddTagResponseModel"] = None


class GetPagesResponse(Model):
    response: Optional["GetPagesResponseModel"] = None


class GetTagsResponse(Model):
    response: Optional["GetTagsResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


AddTagResponseModel = Optional[FaveTag]


class GetPagesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FavePage"]] = None


class GetTagsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FaveTag"]] = None


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FaveBookmark"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FaveBookmark"]] = None


AddTagResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()
GetTagsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()

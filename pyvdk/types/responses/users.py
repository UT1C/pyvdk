from typing import Optional, List

from ..objects import (
    UsersUserXtrCounters,
    UsersUsersArray,
    UsersUserFull,
    GroupsGroupsArray,
    UsersSubscriptionsItem,
)
from ..abc import Model


class GetFollowersFieldsResponse(Model):
    response: Optional["GetFollowersFieldsResponseModel"] = None


class GetFollowersResponse(Model):
    response: Optional["GetFollowersResponseModel"] = None


class GetSubscriptionsExtendedResponse(Model):
    response: Optional["GetSubscriptionsExtendedResponseModel"] = None


class GetSubscriptionsResponse(Model):
    response: Optional["GetSubscriptionsResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class GetFollowersFieldsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetFollowersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSubscriptionsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersSubscriptionsItem"]] = None


class GetSubscriptionsResponseModel(Model):
    users: Optional["UsersUsersArray"] = None
    groups: Optional["GroupsGroupsArray"] = None


GetResponseModel = List[UsersUserXtrCounters]


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


GetFollowersFieldsResponse.update_forward_refs()
GetFollowersResponse.update_forward_refs()
GetSubscriptionsExtendedResponse.update_forward_refs()
GetSubscriptionsResponse.update_forward_refs()
GetResponse.update_forward_refs()
SearchResponse.update_forward_refs()

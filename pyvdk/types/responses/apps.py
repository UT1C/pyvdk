from typing import Optional, List

from ..objects import (
    AppsLeaderboard,
    UsersUserMin,
    AppsScope,
    UsersUserFull,
    AppsApp,
)
from ..abc import Model


class GetCatalogResponse(Model):
    response: Optional["GetCatalogResponseModel"] = None


class GetFriendsListResponse(Model):
    response: Optional["GetFriendsListResponseModel"] = None


class GetLeaderboardExtendedResponse(Model):
    response: Optional["GetLeaderboardExtendedResponseModel"] = None


class GetLeaderboardResponse(Model):
    response: Optional["GetLeaderboardResponseModel"] = None


class GetScopesResponse(Model):
    response: Optional["GetScopesResponseModel"] = None


class GetScoreResponse(Model):
    response: Optional["GetScoreResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class SendRequestResponse(Model):
    response: Optional["SendRequestResponseModel"] = None


class GetCatalogResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AppsApp"]] = None


class GetFriendsListResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetLeaderboardExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AppsLeaderboard"]] = None
    profiles: Optional[List["UsersUserMin"]] = None


class GetLeaderboardResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AppsLeaderboard"]] = None


class GetScopesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AppsScope"]] = None


GetScoreResponseModel = int


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AppsApp"]] = None


SendRequestResponseModel = int

GetCatalogResponse.update_forward_refs()
GetFriendsListResponse.update_forward_refs()
GetLeaderboardExtendedResponse.update_forward_refs()
GetLeaderboardResponse.update_forward_refs()
GetScopesResponse.update_forward_refs()
GetScoreResponse.update_forward_refs()
GetResponse.update_forward_refs()
SendRequestResponse.update_forward_refs()

from typing import Optional, List

from ..objects import (
    UtilsLinkStatsExtended,
    UtilsLinkChecked,
    UtilsShortLink,
    UtilsLinkStats,
    UtilsLastShortenedLink,
    UtilsDomainResolved,
)
from ..abc import Model


class CheckLinkResponse(Model):
    response: Optional["CheckLinkResponseModel"] = None


class GetLastShortenedLinksResponse(Model):
    response: Optional["GetLastShortenedLinksResponseModel"] = None


class GetLinkStatsExtendedResponse(Model):
    response: Optional["GetLinkStatsExtendedResponseModel"] = None


class GetLinkStatsResponse(Model):
    response: Optional["GetLinkStatsResponseModel"] = None


class GetServerTimeResponse(Model):
    response: Optional["GetServerTimeResponseModel"] = None


class GetShortLinkResponse(Model):
    response: Optional["GetShortLinkResponseModel"] = None


class ResolveScreenNameResponse(Model):
    response: Optional["ResolveScreenNameResponseModel"] = None


CheckLinkResponseModel = Optional[UtilsLinkChecked]


class GetLastShortenedLinksResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UtilsLastShortenedLink"]] = None


GetLinkStatsExtendedResponseModel = Optional[UtilsLinkStatsExtended]

GetLinkStatsResponseModel = Optional[UtilsLinkStats]


GetServerTimeResponseModel = int

GetShortLinkResponseModel = Optional[UtilsShortLink]

ResolveScreenNameResponseModel = Optional[UtilsDomainResolved]

CheckLinkResponse.update_forward_refs()
GetLastShortenedLinksResponse.update_forward_refs()
GetLinkStatsExtendedResponse.update_forward_refs()
GetLinkStatsResponse.update_forward_refs()
GetServerTimeResponse.update_forward_refs()
GetShortLinkResponse.update_forward_refs()
ResolveScreenNameResponse.update_forward_refs()

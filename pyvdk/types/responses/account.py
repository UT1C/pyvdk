from typing import Optional, List

from ..objects import (
    AccountNameRequest,
    AccountOffer,
    UsersUserMin,
    AccountPushSettings,
    AccountInfo,
    AccountUserSettings,
    GroupsGroup,
    BaseBoolInt,
    AccountAccountCounters,
)
from ..abc import Model


class ChangePasswordResponse(Model):
    response: Optional["ChangePasswordResponseModel"] = None


class GetActiveOffersResponse(Model):
    response: Optional["GetActiveOffersResponseModel"] = None


class GetAppPermissionsResponse(Model):
    response: Optional["GetAppPermissionsResponseModel"] = None


class GetBannedResponse(Model):
    response: Optional["GetBannedResponseModel"] = None


class GetCountersResponse(Model):
    response: Optional["GetCountersResponseModel"] = None


class GetInfoResponse(Model):
    response: Optional["GetInfoResponseModel"] = None


class GetProfileInfoResponse(Model):
    response: Optional["GetProfileInfoResponseModel"] = None


class GetPushSettingsResponse(Model):
    response: Optional["GetPushSettingsResponseModel"] = None


class SaveProfileInfoResponse(Model):
    response: Optional["SaveProfileInfoResponseModel"] = None


class ChangePasswordResponseModel(Model):
    token: Optional[str] = None
    secret: Optional[str] = None


class GetActiveOffersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AccountOffer"]] = None


GetAppPermissionsResponseModel = int


class GetBannedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroup"]] = None


GetCountersResponseModel = Optional[AccountAccountCounters]

GetInfoResponseModel = Optional[AccountInfo]

GetProfileInfoResponseModel = Optional[AccountUserSettings]

GetPushSettingsResponseModel = Optional[AccountPushSettings]


class SaveProfileInfoResponseModel(Model):
    changed: Optional["BaseBoolInt"] = None
    name_request: Optional["AccountNameRequest"] = None


ChangePasswordResponse.update_forward_refs()
GetActiveOffersResponse.update_forward_refs()
GetAppPermissionsResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetCountersResponse.update_forward_refs()
GetInfoResponse.update_forward_refs()
GetProfileInfoResponse.update_forward_refs()
GetPushSettingsResponse.update_forward_refs()
SaveProfileInfoResponse.update_forward_refs()

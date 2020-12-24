from typing import Optional, List

from ..objects import (
    SecureTokenChecked,
    SecureTransaction,
    SecureLevel,
    SecureSmsNotification,
)
from ..abc import Model


class CheckTokenResponse(Model):
    response: Optional["CheckTokenResponseModel"] = None


class GetAppBalanceResponse(Model):
    response: Optional["GetAppBalanceResponseModel"] = None


class GetSMSHistoryResponse(Model):
    response: Optional["GetSMSHistoryResponseModel"] = None


class GetTransactionsHistoryResponse(Model):
    response: Optional["GetTransactionsHistoryResponseModel"] = None


class GetUserLevelResponse(Model):
    response: Optional["GetUserLevelResponseModel"] = None


class GiveEventStickerResponse(Model):
    response: Optional["GiveEventStickerResponseModel"] = None


class SendNotificationResponse(Model):
    response: Optional["SendNotificationResponseModel"] = None


CheckTokenResponseModel = Optional[SecureTokenChecked]

GetAppBalanceResponseModel = int

GetSMSHistoryResponseModel = List[SecureSmsNotification]

GetTransactionsHistoryResponseModel = List[SecureTransaction]

GetUserLevelResponseModel = List[SecureLevel]


class GiveEventStickerResponseModel(Model):
    user_id: Optional[int] = None
    status: Optional[str] = None


SendNotificationResponseModel = List[int]


CheckTokenResponse.update_forward_refs()
GetAppBalanceResponse.update_forward_refs()
GetSMSHistoryResponse.update_forward_refs()
GetTransactionsHistoryResponse.update_forward_refs()
GetUserLevelResponse.update_forward_refs()
GiveEventStickerResponse.update_forward_refs()
SendNotificationResponse.update_forward_refs()

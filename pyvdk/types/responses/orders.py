from typing import Optional, List

from ..objects import (
    OrdersAmount,
    OrdersOrder,
    OrdersSubscription,
    BaseBoolInt,
)
from ..abc import Model


class CancelSubscriptionResponse(Model):
    response: Optional["CancelSubscriptionResponseModel"] = None


class ChangeStateResponse(Model):
    response: Optional["ChangeStateResponseModel"] = None


class GetAmountResponse(Model):
    response: Optional["GetAmountResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetUserSubscriptionByIdResponse(Model):
    response: Optional["GetUserSubscriptionByIdResponseModel"] = None


class GetUserSubscriptionsResponse(Model):
    response: Optional["GetUserSubscriptionsResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class UpdateSubscriptionResponse(Model):
    response: Optional["UpdateSubscriptionResponseModel"] = None


CancelSubscriptionResponseModel = Optional[BaseBoolInt]

ChangeStateResponseModel = str

GetAmountResponseModel = Optional[OrdersAmount]

GetByIdResponseModel = List[OrdersOrder]

GetUserSubscriptionByIdResponseModel = Optional[OrdersSubscription]


class GetUserSubscriptionsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["OrdersSubscription"]] = None


GetResponseModel = List[OrdersOrder]

UpdateSubscriptionResponseModel = Optional[BaseBoolInt]


CancelSubscriptionResponse.update_forward_refs()
ChangeStateResponse.update_forward_refs()
GetAmountResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetUserSubscriptionByIdResponse.update_forward_refs()
GetUserSubscriptionsResponse.update_forward_refs()
GetResponse.update_forward_refs()
UpdateSubscriptionResponse.update_forward_refs()

from typing import Optional, List

from ..objects import (
    LeadsChecked,
    LeadsComplete,
    LeadsStart,
    LeadsLead,
    LeadsEntry,
)
from ..abc import Model


class CheckUserResponse(Model):
    response: Optional["CheckUserResponseModel"] = None


class CompleteResponse(Model):
    response: Optional["CompleteResponseModel"] = None


class GetStatsResponse(Model):
    response: Optional["GetStatsResponseModel"] = None


class GetUsersResponse(Model):
    response: Optional["GetUsersResponseModel"] = None


class MetricHitResponse(Model):
    response: Optional["MetricHitResponseModel"] = None


class StartResponse(Model):
    response: Optional["StartResponseModel"] = None


CheckUserResponseModel = Optional[LeadsChecked]

CompleteResponseModel = Optional[LeadsComplete]

GetStatsResponseModel = Optional[LeadsLead]

GetUsersResponseModel = List[LeadsEntry]


class MetricHitResponseModel(Model):
    result: Optional[bool] = None
    redirect_link: Optional[str] = None


StartResponseModel = Optional[LeadsStart]

CheckUserResponse.update_forward_refs()
CompleteResponse.update_forward_refs()
GetStatsResponse.update_forward_refs()
GetUsersResponse.update_forward_refs()
MetricHitResponse.update_forward_refs()
StartResponse.update_forward_refs()

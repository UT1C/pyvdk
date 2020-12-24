from typing import Optional, List

from ..objects import StatsWallpostStat, StatsPeriod
from ..abc import Model


class GetPostReachResponse(Model):
    response: Optional["GetPostReachResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


GetPostReachResponseModel = List[StatsWallpostStat]

GetResponseModel = List[StatsPeriod]

GetPostReachResponse.update_forward_refs()
GetResponse.update_forward_refs()

from typing import Optional, List

from ..objects import SearchHint
from ..abc import Model


class GetHintsResponse(Model):
    response: Optional["GetHintsResponseModel"] = None


class GetHintsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["SearchHint"]] = None
    suggested_queries: Optional[List[str]] = None


GetHintsResponse.update_forward_refs()

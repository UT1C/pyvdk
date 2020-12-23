from typing import Optional, List

from ..objects import GiftsGift
from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


class GetResponseModel(BaseResponse):
    count: Optional[int] = None
    items: Optional[List["GiftsGift"]] = None


GetResponse.update_forward_refs()

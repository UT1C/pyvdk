from typing import Optional, List

from ..objects import GiftsGift
from ..abc import Model


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GiftsGift"]] = None


GetResponse.update_forward_refs()

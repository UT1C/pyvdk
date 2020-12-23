from typing import Optional

from ..objects import StatusStatus
from .base_response import BaseResponse


class GetResponse(BaseResponse):
    response: Optional["GetResponseModel"] = None


GetResponseModel = Optional[StatusStatus]

GetResponse.update_forward_refs()

from typing import Optional

from ..objects import StatusStatus
from ..abc import Model


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


GetResponseModel = Optional[StatusStatus]

GetResponse.update_forward_refs()

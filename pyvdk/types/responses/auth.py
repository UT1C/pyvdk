from typing import Optional

from ..abc import Model


class RestoreResponse(Model):
    response: Optional["RestoreResponseModel"] = None


class RestoreResponseModel(Model):
    success: Optional[int] = None
    sid: Optional[str] = None


RestoreResponse.update_forward_refs()

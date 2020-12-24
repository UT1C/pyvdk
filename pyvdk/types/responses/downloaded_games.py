from typing import Optional

from ..abc import Model


class PaidStatusResponse(Model):
    response: Optional["PaidStatusResponseModel"] = None


class PaidStatusResponseModel(Model):
    is_paid: Optional[bool] = None


PaidStatusResponse.update_forward_refs()

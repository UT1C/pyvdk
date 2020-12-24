from typing import Optional

from ..abc import Model


class GetServerUrlResponse(Model):
    response: Optional["GetServerUrlResponseModel"] = None


class GetServerUrlResponseModel(Model):
    endpoint: Optional[str] = None
    key: Optional[str] = None


GetServerUrlResponse.update_forward_refs()

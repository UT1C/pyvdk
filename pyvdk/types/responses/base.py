from typing import Optional

from ..objects import BaseUploadServer, BaseBoolInt
from ..abc import Model


class BoolResponse(Model):
    response: Optional["BoolResponseModel"] = None


class GetUploadServerResponse(Model):
    response: Optional["GetUploadServerResponseModel"] = None


class OkResponse(Model):
    response: Optional["OkResponseModel"] = None


BoolResponseModel = Optional[BaseBoolInt]

GetUploadServerResponseModel = Optional[BaseUploadServer]

OkResponseModel = int

BoolResponse.update_forward_refs()
GetUploadServerResponse.update_forward_refs()
OkResponse.update_forward_refs()

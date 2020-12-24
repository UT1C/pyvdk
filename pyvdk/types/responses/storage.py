from typing import Optional, List

from ..objects import StorageValue
from ..abc import Model


class GetKeysResponse(Model):
    response: Optional["GetKeysResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class GetV5110Response(Model):
    response: Optional["GetV5110ResponseModel"] = None


class GetWithKeysResponse(Model):
    response: Optional["GetWithKeysResponseModel"] = None


GetKeysResponseModel = List[str]

GetResponseModel = str

GetV5110ResponseModel = List[StorageValue]

GetWithKeysResponseModel = List[StorageValue]

GetKeysResponse.update_forward_refs()
GetResponse.update_forward_refs()
GetV5110Response.update_forward_refs()
GetWithKeysResponse.update_forward_refs()

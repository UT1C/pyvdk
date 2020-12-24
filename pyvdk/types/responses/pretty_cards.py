from typing import Optional, List

from ..objects import PrettyCardsPrettyCard
from ..abc import Model


class CreateResponse(Model):
    response: Optional["CreateResponseModel"] = None


class DeleteResponse(Model):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(Model):
    response: Optional["EditResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetUploadURLResponse(Model):
    response: Optional["GetUploadURLResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class CreateResponseModel(Model):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None


class DeleteResponseModel(Model):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None
    error: Optional[str] = None


class EditResponseModel(Model):
    owner_id: Optional[int] = None
    card_id: Optional[str] = None


GetByIdResponseModel = List[PrettyCardsPrettyCard]


GetUploadURLResponseModel = str


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["PrettyCardsPrettyCard"]] = None


CreateResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetUploadURLResponse.update_forward_refs()
GetResponse.update_forward_refs()

from typing import Optional, List

from ..objects import UsersUserMin, BaseBoolInt
from ..abc import Model


class AddResponse(Model):
    response: Optional["AddResponseModel"] = None


class DeleteResponse(Model):
    response: Optional["DeleteResponseModel"] = None


class GetListExtendedResponse(Model):
    response: Optional["GetListExtendedResponseModel"] = None


class GetListResponse(Model):
    response: Optional["GetListResponseModel"] = None


class IsLikedResponse(Model):
    response: Optional["IsLikedResponseModel"] = None


class AddResponseModel(Model):
    likes: Optional[int] = None


class DeleteResponseModel(Model):
    likes: Optional[int] = None


class GetListExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserMin"]] = None


class GetListResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsLikedResponseModel(Model):
    liked: Optional["BaseBoolInt"] = None
    copied: Optional["BaseBoolInt"] = None


AddResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
GetListExtendedResponse.update_forward_refs()
GetListResponse.update_forward_refs()
IsLikedResponse.update_forward_refs()

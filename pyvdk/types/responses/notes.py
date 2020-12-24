from typing import Optional, List

from ..objects import NotesNoteComment, NotesNote
from ..abc import Model


class AddResponse(Model):
    response: Optional["AddResponseModel"] = None


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


AddResponseModel = int

CreateCommentResponseModel = int

GetByIdResponseModel = Optional[NotesNote]


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["NotesNoteComment"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["NotesNote"]] = None


AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetResponse.update_forward_refs()

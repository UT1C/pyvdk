from typing import Optional, List

from ..objects import (
    BoardTopicComment,
    UsersUserMin,
    UsersUser,
    GroupsGroup,
    BaseBoolInt,
    BoardTopicPoll,
    BoardDefaultOrder,
    BoardTopic,
)
from ..abc import Model


class AddTopicResponse(Model):
    response: Optional["AddTopicResponseModel"] = None


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class GetCommentsExtendedResponse(Model):
    response: Optional["GetCommentsExtendedResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetTopicsExtendedResponse(Model):
    response: Optional["GetTopicsExtendedResponseModel"] = None


class GetTopicsResponse(Model):
    response: Optional["GetTopicsResponseModel"] = None


AddTopicResponseModel = int

CreateCommentResponseModel = int


class GetCommentsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BoardTopicComment"]] = None
    poll: Optional["BoardTopicPoll"] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BoardTopicComment"]] = None
    poll: Optional["BoardTopicPoll"] = None


class GetTopicsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BoardTopic"]] = None
    default_order: Optional["BoardDefaultOrder"] = None
    can_add_topics: Optional["BaseBoolInt"] = None
    profiles: Optional[List["UsersUserMin"]] = None


class GetTopicsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["BoardTopic"]] = None
    default_order: Optional["BoardDefaultOrder"] = None
    can_add_topics: Optional["BaseBoolInt"] = None


AddTopicResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
GetCommentsExtendedResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetTopicsExtendedResponse.update_forward_refs()
GetTopicsResponse.update_forward_refs()

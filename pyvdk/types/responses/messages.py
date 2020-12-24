import typing
from typing import Optional, List, Union

from ..objects import (
    GroupsGroupFull,
    GroupsGroup,
    MessagesMessage,
    MessagesPinnedMessage,
    MessagesHistoryAttachment,
    MessagesChatFull,
    MessageChatPreview,
    MessagesLongpollParams,
    MessagesLastActivity,
    MessagesConversation,
    BaseMessageError,
    MessagesConversationWithMessage,
    BaseBoolInt,
    MessagesChatRestrictions,
    MessagesChat,
    UsersUser,
    UsersUserFull,
    MessagesLongpollMessages,
    MessagesConversationMember,
)
from ..abc import Model


class CreateChatResponse(Model):
    response: Optional["CreateChatResponseModel"] = None


class DeleteChatPhotoResponse(Model):
    response: Optional["DeleteChatPhotoResponseModel"] = None


class DeleteConversationResponse(Model):
    response: Optional["DeleteConversationResponseModel"] = None


class DeleteResponse(Model):
    response: Optional["DeleteResponseModel"] = None


class EditResponse(Model):
    response: Optional["EditResponseModel"] = None


class GetByConversationMessageIdResponse(Model):
    response: Optional["GetByConversationMessageIdResponseModel"] = None


class GetByIdExtendedResponse(Model):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetChatPreviewResponse(Model):
    response: Optional["GetChatPreviewResponseModel"] = None


class GetChatChatIdsFieldsResponse(Model):
    response: Optional["GetChatChatIdsFieldsResponseModel"] = None


class GetChatChatIdsResponse(Model):
    response: Optional["GetChatChatIdsResponseModel"] = None


class GetChatFieldsResponse(Model):
    response: Optional["GetChatFieldsResponseModel"] = None


class GetChatResponse(Model):
    response: Optional["GetChatResponseModel"] = None


class GetConversationMembersResponse(Model):
    response: Optional["GetConversationMembersResponseModel"] = None


class GetConversationsByIdExtendedResponse(Model):
    response: Optional["GetConversationsByIdExtendedResponseModel"] = None


class GetConversationsByIdResponse(Model):
    response: Optional["GetConversationsByIdResponseModel"] = None


class GetConversationsResponse(Model):
    response: Optional["GetConversationsResponseModel"] = None


class GetHistoryAttachmentsResponse(Model):
    response: Optional["GetHistoryAttachmentsResponseModel"] = None


class GetHistoryResponse(Model):
    response: Optional["GetHistoryResponseModel"] = None


class GetInviteLinkResponse(Model):
    response: Optional["GetInviteLinkResponseModel"] = None


class GetLastActivityResponse(Model):
    response: Optional["GetLastActivityResponseModel"] = None


class GetLongPollHistoryResponse(Model):
    response: Optional["GetLongPollHistoryResponseModel"] = None


class GetLongPollServerResponse(Model):
    response: Optional["GetLongPollServerResponseModel"] = None


class IsMessagesFromGroupAllowedResponse(Model):
    response: Optional["IsMessagesFromGroupAllowedResponseModel"] = None


class JoinChatByInviteLinkResponse(Model):
    response: Optional["JoinChatByInviteLinkResponseModel"] = None


class MarkAsImportantResponse(Model):
    response: Optional["MarkAsImportantResponseModel"] = None


class PinResponse(Model):
    response: Optional["PinResponseModel"] = None


class SearchConversationsResponse(Model):
    response: Optional["SearchConversationsResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class SendResponse(Model):
    response: Optional["SendResponseModel"] = None


class SendUserIdsResponse(Model):
    response: Optional["SendUserIdsResponseModel"] = None


class SetChatPhotoResponse(Model):
    response: Optional["SetChatPhotoResponseModel"] = None


CreateChatResponseModel = int


class DeleteChatPhotoResponseModel(Model):
    message_id: Optional[int] = None
    chat: Optional["MessagesChat"] = None


class DeleteConversationResponseModel(Model):
    last_deleted_id: Optional[int] = None


DeleteResponseModel = typing.Dict[str, int]

EditResponseModel = Optional[BaseBoolInt]


class GetByConversationMessageIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class GetByIdExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetByIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


class GetChatPreviewResponseModel(Model):
    preview: Optional["MessageChatPreview"] = None
    profiles: Optional[List["UsersUserFull"]] = None


GetChatChatIdsFieldsResponseModel = List[MessagesChatFull]

GetChatChatIdsResponseModel = List[MessagesChat]

GetChatFieldsResponseModel = Optional[MessagesChatFull]

GetChatResponseModel = Optional[MessagesChat]


class GetConversationMembersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesConversationMember"]] = None
    chat_restrictions: Optional["MessagesChatRestrictions"] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetConversationsByIdExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None
    profiles: Optional[List["UsersUser"]] = None


class GetConversationsByIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None


class GetConversationsResponseModel(Model):
    count: Optional[int] = None
    unread_count: Optional[int] = None
    items: Optional[List["MessagesConversationWithMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetHistoryAttachmentsResponseModel(Model):
    items: Optional[List["MessagesHistoryAttachment"]] = None
    next_from: Optional[str] = None


class GetHistoryResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetInviteLinkResponseModel(Model):
    link: Optional[str] = None


GetLastActivityResponseModel = Optional[MessagesLastActivity]


class GetLongPollHistoryResponseModel(Model):
    history: Optional[List[List[int]]] = None
    groups: Optional[List["GroupsGroup"]] = None
    messages: Optional["MessagesLongpollMessages"] = None
    profiles: Optional[List["UsersUserFull"]] = None
    chats: Optional[List["MessagesChat"]] = None
    new_pts: Optional[int] = None
    more: Optional[bool] = None
    conversations: Optional[List["MessagesConversation"]] = None


GetLongPollServerResponseModel = Optional[MessagesLongpollParams]


class IsMessagesFromGroupAllowedResponseModel(Model):
    is_allowed: Optional["BaseBoolInt"] = None


class JoinChatByInviteLinkResponseModel(Model):
    chat_id: Optional[int] = None


MarkAsImportantResponseModel = List[int]

PinResponseModel = Optional[MessagesPinnedMessage]


class SearchConversationsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesConversation"]] = None
    profiles: Optional[List["UsersUserFull"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MessagesMessage"]] = None


SendResponseModel = Union[int, SendUserIdsResponse]


class SendResponsePeerIdsModel(Model):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    conversation_message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None


class SendUserIdsResponseModel(Model):
    peer_id: Optional[int] = None
    message_id: Optional[int] = None
    error: Optional["BaseMessageError"] = None


class SetChatPhotoResponseModel(Model):
    message_id: Optional[int] = None
    chat: Optional["MessagesChat"] = None


CreateChatResponse.update_forward_refs()
DeleteChatPhotoResponse.update_forward_refs()
DeleteConversationResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
EditResponse.update_forward_refs()
GetByConversationMessageIdResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetChatPreviewResponse.update_forward_refs()
GetChatChatIdsFieldsResponse.update_forward_refs()
GetChatChatIdsResponse.update_forward_refs()
GetChatFieldsResponse.update_forward_refs()
GetChatResponse.update_forward_refs()
GetConversationMembersResponse.update_forward_refs()
GetConversationsByIdExtendedResponse.update_forward_refs()
GetConversationsByIdResponse.update_forward_refs()
GetConversationsResponse.update_forward_refs()
GetHistoryAttachmentsResponse.update_forward_refs()
GetHistoryResponse.update_forward_refs()
GetInviteLinkResponse.update_forward_refs()
GetLastActivityResponse.update_forward_refs()
GetLongPollHistoryResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
IsMessagesFromGroupAllowedResponse.update_forward_refs()
JoinChatByInviteLinkResponse.update_forward_refs()
MarkAsImportantResponse.update_forward_refs()
PinResponse.update_forward_refs()
SearchConversationsResponse.update_forward_refs()
SearchResponse.update_forward_refs()
SendResponse.update_forward_refs()
SendUserIdsResponse.update_forward_refs()
SetChatPhotoResponse.update_forward_refs()

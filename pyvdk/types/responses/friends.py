from typing import Optional, List

from ..objects import (
    FriendsMutualFriend,
    FriendsUserXtrPhone,
    FriendsFriendStatus,
    FriendsUserXtrLists,
    UsersUserFull,
    FriendsFriendExtendedStatus,
    FriendsRequestsXtrMessage,
    FriendsFriendsList,
    FriendsRequests,
)
from ..abc import Model


class AddListResponse(Model):
    response: Optional["AddListResponseModel"] = None


class AddResponse(Model):
    response: Optional["AddResponseModel"] = None


class AreFriendsExtendedResponse(Model):
    response: Optional["AreFriendsExtendedResponseModel"] = None


class AreFriendsResponse(Model):
    response: Optional["AreFriendsResponseModel"] = None


class DeleteResponse(Model):
    response: Optional["DeleteResponseModel"] = None


class GetAppUsersResponse(Model):
    response: Optional["GetAppUsersResponseModel"] = None


class GetByPhonesResponse(Model):
    response: Optional["GetByPhonesResponseModel"] = None


class GetListsResponse(Model):
    response: Optional["GetListsResponseModel"] = None


class GetMutualResponse(Model):
    response: Optional["GetMutualResponseModel"] = None


class GetMutualTargetUidsResponse(Model):
    response: Optional["GetMutualTargetUidsResponseModel"] = None


class GetOnlineOnlineMobileResponse(Model):
    response: Optional["GetOnlineOnlineMobileResponseModel"] = None


class GetOnlineResponse(Model):
    response: Optional["GetOnlineResponseModel"] = None


class GetRecentResponse(Model):
    response: Optional["GetRecentResponseModel"] = None


class GetRequestsExtendedResponse(Model):
    response: Optional["GetRequestsExtendedResponseModel"] = None


class GetRequestsNeedMutualResponse(Model):
    response: Optional["GetRequestsNeedMutualResponseModel"] = None


class GetRequestsResponse(Model):
    response: Optional["GetRequestsResponseModel"] = None


class GetSuggestionsResponse(Model):
    response: Optional["GetSuggestionsResponseModel"] = None


class GetFieldsResponse(Model):
    response: Optional["GetFieldsResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class AddListResponseModel(Model):
    list_id: Optional[int] = None


AddResponseModel = int

AreFriendsExtendedResponseModel = List[FriendsFriendExtendedStatus]

AreFriendsResponseModel = List[FriendsFriendStatus]


class DeleteResponseModel(Model):
    success: Optional[int] = None
    friend_deleted: Optional[int] = None
    out_request_deleted: Optional[int] = None
    in_request_deleted: Optional[int] = None
    suggestion_deleted: Optional[int] = None


GetAppUsersResponseModel = List[int]

GetByPhonesResponseModel = List[FriendsUserXtrPhone]


class GetListsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FriendsFriendsList"]] = None


GetMutualResponseModel = List[int]

GetMutualTargetUidsResponseModel = List[FriendsMutualFriend]


class GetOnlineOnlineMobileResponseModel(Model):
    online: Optional[List[int]] = None
    online_mobile: Optional[List[int]] = None


GetOnlineResponseModel = List[int]


GetRecentResponseModel = List[int]


class GetRequestsExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FriendsRequestsXtrMessage"]] = None


class GetRequestsNeedMutualResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FriendsRequests"]] = None


class GetRequestsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None
    count_unread: Optional[int] = None


class GetSuggestionsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetFieldsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["FriendsUserXtrLists"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


AddListResponse.update_forward_refs()
AddResponse.update_forward_refs()
AreFriendsExtendedResponse.update_forward_refs()
AreFriendsResponse.update_forward_refs()
DeleteResponse.update_forward_refs()
GetAppUsersResponse.update_forward_refs()
GetByPhonesResponse.update_forward_refs()
GetListsResponse.update_forward_refs()
GetMutualResponse.update_forward_refs()
GetMutualTargetUidsResponse.update_forward_refs()
GetOnlineOnlineMobileResponse.update_forward_refs()
GetOnlineResponse.update_forward_refs()
GetRecentResponse.update_forward_refs()
GetRequestsExtendedResponse.update_forward_refs()
GetRequestsNeedMutualResponse.update_forward_refs()
GetRequestsResponse.update_forward_refs()
GetSuggestionsResponse.update_forward_refs()
GetFieldsResponse.update_forward_refs()
GetResponse.update_forward_refs()
SearchResponse.update_forward_refs()

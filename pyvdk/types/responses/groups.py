import typing
from typing import Optional, Any, List, Union

from ..objects import (
    GroupsCallbackSettings,
    GroupsGroupFull,
    GroupsGroupDocs,
    GroupsGroupAudio,
    GroupsSettingsTwitter,
    GroupsMemberStatus,
    GroupsGroupPublicCategoryList,
    GroupsGroupLink,
    GroupsGroup,
    GroupsMemberRole,
    GroupsGroupVideo,
    GroupsLongPollServer,
    GroupsLongPollSettings,
    GroupsGroupAccess,
    GroupsGroupTopics,
    GroupsMemberStatusFull,
    GroupsGroupFullMainSection,
    GroupsGroupCategoryFull,
    GroupsSubjectItem,
    GroupsBannedItem,
    GroupsCallbackServer,
    BaseBoolInt,
    GroupsGroupCategory,
    GroupsAddress,
    UsersUserMin,
    GroupsTokenPermissionSetting,
    GroupsGroupWall,
    UsersUserFull,
    GroupsGroupXtrInvitedBy,
    GroupsGroupWiki,
    GroupsUserXtrRole,
)
from ..abc import Model


class AddAddressResponse(Model):
    response: Optional["AddAddressResponseModel"] = None


class AddCallbackServerResponse(Model):
    response: Optional["AddCallbackServerResponseModel"] = None


class AddLinkResponse(Model):
    response: Optional["AddLinkResponseModel"] = None


class CreateResponse(Model):
    response: Optional["CreateResponseModel"] = None


class EditAddressResponse(Model):
    response: Optional["EditAddressResponseModel"] = None


class GetAddressesResponse(Model):
    response: Optional["GetAddressesResponseModel"] = None


class GetBannedResponse(Model):
    response: Optional["GetBannedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetCallbackConfirmationCodeResponse(Model):
    response: Optional["GetCallbackConfirmationCodeResponseModel"] = None


class GetCallbackServersResponse(Model):
    response: Optional["GetCallbackServersResponseModel"] = None


class GetCallbackSettingsResponse(Model):
    response: Optional["GetCallbackSettingsResponseModel"] = None


class GetCatalogInfoExtendedResponse(Model):
    response: Optional["GetCatalogInfoExtendedResponseModel"] = None


class GetCatalogInfoResponse(Model):
    response: Optional["GetCatalogInfoResponseModel"] = None


class GetCatalogResponse(Model):
    response: Optional["GetCatalogResponseModel"] = None


class GetInvitedUsersResponse(Model):
    response: Optional["GetInvitedUsersResponseModel"] = None


class GetInvitesExtendedResponse(Model):
    response: Optional["GetInvitesExtendedResponseModel"] = None


class GetInvitesResponse(Model):
    response: Optional["GetInvitesResponseModel"] = None


class GetLongPollServerResponse(Model):
    response: Optional["GetLongPollServerResponseModel"] = None


class GetLongPollSettingsResponse(Model):
    response: Optional["GetLongPollSettingsResponseModel"] = None


class GetMembersFieldsResponse(Model):
    response: Optional["GetMembersFieldsResponseModel"] = None


class GetMembersFilterResponse(Model):
    response: Optional["GetMembersFilterResponseModel"] = None


class GetMembersResponse(Model):
    response: Optional["GetMembersResponseModel"] = None


class GetRequestsFieldsResponse(Model):
    response: Optional["GetRequestsFieldsResponseModel"] = None


class GetRequestsResponse(Model):
    response: Optional["GetRequestsResponseModel"] = None


class GetSettingsResponse(Model):
    response: Optional["GetSettingsResponseModel"] = None


class GetTokenPermissionsResponse(Model):
    response: Optional["GetTokenPermissionsResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class IsMemberExtendedResponse(Model):
    response: Optional["IsMemberExtendedResponseModel"] = None


class IsMemberResponse(Model):
    response: Optional["IsMemberResponseModel"] = None


class IsMemberUserIdsExtendedResponse(Model):
    response: Optional["IsMemberUserIdsExtendedResponseModel"] = None


class IsMemberUserIdsResponse(Model):
    response: Optional["IsMemberUserIdsResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


AddAddressResponseModel = Optional[GroupsAddress]


class AddCallbackServerResponseModel(Model):
    server_id: Optional[int] = None


AddLinkResponseModel = Optional[GroupsGroupLink]

CreateResponseModel = Optional[GroupsGroup]

EditAddressResponseModel = Optional[GroupsAddress]


class GetAddressesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsAddress"]] = None


class GetBannedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsBannedItem"]] = None


GetByIdResponseModel = List[GroupsGroupFull]


class GetCallbackConfirmationCodeResponseModel(Model):
    code: Optional[str] = None


class GetCallbackServersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsCallbackServer"]] = None


GetCallbackSettingsResponseModel = Optional[GroupsCallbackSettings]


class GetCatalogInfoExtendedResponseModel(Model):
    enabled: Optional[int] = None
    categories: Optional[List["GroupsGroupCategoryFull"]] = None


class GetCatalogInfoResponseModel(Model):
    enabled: Optional[int] = None
    categories: Optional[List["GroupsGroupCategory"]] = None


class GetCatalogResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsGroup"]] = None


class GetInvitedUsersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetInvitesExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupXtrInvitedBy"]] = None
    profiles: Optional[List["UsersUserMin"]] = None
    groups: Optional[List["GroupsGroupFull"]] = None


class GetInvitesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupXtrInvitedBy"]] = None


GetLongPollServerResponseModel = Optional[GroupsLongPollServer]

GetLongPollSettingsResponseModel = Optional[GroupsLongPollSettings]


class GetMembersFieldsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsUserXtrRole"]] = None


class GetMembersFilterResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[Union["GroupsMemberRole", int]]] = None


class GetMembersResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetRequestsFieldsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["UsersUserFull"]] = None


class GetRequestsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class GetSettingsResponseModel(Model):
    access: Optional["GroupsGroupAccess"] = None
    address: Optional[str] = None
    audio: Optional["GroupsGroupAudio"] = None
    articles: Optional[int] = None
    city_id: Optional[int] = None
    contacts: Optional["BaseBoolInt"] = None
    links: Optional["BaseBoolInt"] = None
    sections_list: Optional[typing.Dict[Any, Any]] = None
    main_section: Optional["GroupsGroupFullMainSection"] = None
    secondary_section: Optional[int] = None
    age_limits: Optional[int] = None
    country_id: Optional[int] = None
    description: Optional[str] = None
    docs: Optional["GroupsGroupDocs"] = None
    events: Optional["BaseBoolInt"] = None
    obscene_filter: Optional["BaseBoolInt"] = None
    obscene_stopwords: Optional["BaseBoolInt"] = None
    obscene_words: Optional[List[str]] = None
    event_group_id: Optional[int] = None
    photos: Optional[int] = None
    public_category: Optional[int] = None
    public_category_list: Optional[List["GroupsGroupPublicCategoryList"]] = None
    public_date: Optional[str] = None
    public_date_label: Optional[str] = None
    public_subcategory: Optional[int] = None
    rss: Optional[str] = None
    start_date: Optional[int] = None
    finish_date: Optional[int] = None
    subject: Optional[int] = None
    subject_list: Optional[List["GroupsSubjectItem"]] = None
    suggested_privacy: Optional[int] = None
    title: Optional[str] = None
    topics: Optional["GroupsGroupTopics"] = None
    twitter: Optional["GroupsSettingsTwitter"] = None
    video: Optional["GroupsGroupVideo"] = None
    wall: Optional["GroupsGroupWall"] = None
    website: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    wiki: Optional["GroupsGroupWiki"] = None


class GetTokenPermissionsResponseModel(Model):
    mask: Optional[int] = None
    permissions: Optional[List["GroupsTokenPermissionSetting"]] = None


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsGroupFull"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List[int]] = None


class IsMemberExtendedResponseModel(Model):
    member: Optional["BaseBoolInt"] = None
    invitation: Optional["BaseBoolInt"] = None
    can_invite: Optional["BaseBoolInt"] = None
    can_recall: Optional["BaseBoolInt"] = None
    request: Optional["BaseBoolInt"] = None


IsMemberResponseModel = Optional[BaseBoolInt]

IsMemberUserIdsExtendedResponseModel = List[GroupsMemberStatusFull]

IsMemberUserIdsResponseModel = List[GroupsMemberStatus]


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["GroupsGroup"]] = None


AddAddressResponse.update_forward_refs()
AddCallbackServerResponse.update_forward_refs()
AddLinkResponse.update_forward_refs()
CreateResponse.update_forward_refs()
EditAddressResponse.update_forward_refs()
GetAddressesResponse.update_forward_refs()
GetBannedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCallbackConfirmationCodeResponse.update_forward_refs()
GetCallbackServersResponse.update_forward_refs()
GetCallbackSettingsResponse.update_forward_refs()
GetCatalogInfoExtendedResponse.update_forward_refs()
GetCatalogInfoResponse.update_forward_refs()
GetCatalogResponse.update_forward_refs()
GetInvitedUsersResponse.update_forward_refs()
GetInvitesExtendedResponse.update_forward_refs()
GetInvitesResponse.update_forward_refs()
GetLongPollServerResponse.update_forward_refs()
GetLongPollSettingsResponse.update_forward_refs()
GetMembersFieldsResponse.update_forward_refs()
GetMembersFilterResponse.update_forward_refs()
GetMembersResponse.update_forward_refs()
GetRequestsFieldsResponse.update_forward_refs()
GetRequestsResponse.update_forward_refs()
GetSettingsResponse.update_forward_refs()
GetTokenPermissionsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
IsMemberExtendedResponse.update_forward_refs()
IsMemberResponse.update_forward_refs()
IsMemberUserIdsExtendedResponse.update_forward_refs()
IsMemberUserIdsResponse.update_forward_refs()
SearchResponse.update_forward_refs()

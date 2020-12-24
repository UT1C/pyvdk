from typing import Optional, List

from ..objects import (
    AdsTargSettings,
    AdsTargStats,
    AdsRejectReason,
    AdsFloodStats,
    AdsCampaign,
    AdsTargSuggestions,
    AdsDemoStats,
    AdsCategory,
    AdsStats,
    AdsUsers,
    AdsTargSuggestionsRegions,
    AdsAccount,
    AdsAd,
    AdsTargSuggestionsSchools,
    AdsLookalikeRequest,
    AdsPromotedPostReach,
    AdsAdLayout,
    AdsMusician,
    AdsTargetGroup,
    AdsTargSuggestionsCities,
    AdsLinkStatus,
    AdsClient,
)
from ..abc import Model


class AddOfficeUsersResponse(Model):
    response: Optional["AddOfficeUsersResponseModel"] = None


class CheckLinkResponse(Model):
    response: Optional["CheckLinkResponseModel"] = None


class CreateAdsResponse(Model):
    response: Optional["CreateAdsResponseModel"] = None


class CreateCampaignsResponse(Model):
    response: Optional["CreateCampaignsResponseModel"] = None


class CreateClientsResponse(Model):
    response: Optional["CreateClientsResponseModel"] = None


class CreateTargetGroupResponse(Model):
    response: Optional["CreateTargetGroupResponseModel"] = None


class DeleteAdsResponse(Model):
    response: Optional["DeleteAdsResponseModel"] = None


class DeleteCampaignsResponse(Model):
    response: Optional["DeleteCampaignsResponseModel"] = None


class DeleteClientsResponse(Model):
    response: Optional["DeleteClientsResponseModel"] = None


class GetAccountsResponse(Model):
    response: Optional["GetAccountsResponseModel"] = None


class GetAdsLayoutResponse(Model):
    response: Optional["GetAdsLayoutResponseModel"] = None


class GetAdsTargetingResponse(Model):
    response: Optional["GetAdsTargetingResponseModel"] = None


class GetAdsResponse(Model):
    response: Optional["GetAdsResponseModel"] = None


class GetBudgetResponse(Model):
    response: Optional["GetBudgetResponseModel"] = None


class GetCampaignsResponse(Model):
    response: Optional["GetCampaignsResponseModel"] = None


class GetCategoriesResponse(Model):
    response: Optional["GetCategoriesResponseModel"] = None


class GetClientsResponse(Model):
    response: Optional["GetClientsResponseModel"] = None


class GetDemographicsResponse(Model):
    response: Optional["GetDemographicsResponseModel"] = None


class GetFloodStatsResponse(Model):
    response: Optional["GetFloodStatsResponseModel"] = None


class GetLookalikeRequestsResponse(Model):
    response: Optional["GetLookalikeRequestsResponseModel"] = None


class GetMusiciansResponse(Model):
    response: Optional["GetMusiciansResponseModel"] = None


class GetOfficeUsersResponse(Model):
    response: Optional["GetOfficeUsersResponseModel"] = None


class GetPostsReachResponse(Model):
    response: Optional["GetPostsReachResponseModel"] = None


class GetRejectionReasonResponse(Model):
    response: Optional["GetRejectionReasonResponseModel"] = None


class GetStatisticsResponse(Model):
    response: Optional["GetStatisticsResponseModel"] = None


class GetSuggestionsCitiesResponse(Model):
    response: Optional["GetSuggestionsCitiesResponseModel"] = None


class GetSuggestionsRegionsResponse(Model):
    response: Optional["GetSuggestionsRegionsResponseModel"] = None


class GetSuggestionsResponse(Model):
    response: Optional["GetSuggestionsResponseModel"] = None


class GetSuggestionsSchoolsResponse(Model):
    response: Optional["GetSuggestionsSchoolsResponseModel"] = None


class GetTargetGroupsResponse(Model):
    response: Optional["GetTargetGroupsResponseModel"] = None


class GetTargetingStatsResponse(Model):
    response: Optional["GetTargetingStatsResponseModel"] = None


class GetUploadURLResponse(Model):
    response: Optional["GetUploadURLResponseModel"] = None


class GetVideoUploadURLResponse(Model):
    response: Optional["GetVideoUploadURLResponseModel"] = None


class ImportTargetContactsResponse(Model):
    response: Optional["ImportTargetContactsResponseModel"] = None


class RemoveOfficeUsersResponse(Model):
    response: Optional["RemoveOfficeUsersResponseModel"] = None


class UpdateAdsResponse(Model):
    response: Optional["UpdateAdsResponseModel"] = None


class UpdateCampaignsResponse(Model):
    response: Optional["UpdateCampaignsResponseModel"] = None


class UpdateClientsResponse(Model):
    response: Optional["UpdateClientsResponseModel"] = None


AddOfficeUsersResponseModel = bool

CheckLinkResponseModel = Optional[AdsLinkStatus]

CreateAdsResponseModel = List[int]

CreateCampaignsResponseModel = List[int]


CreateClientsResponseModel = List[int]


class CreateTargetGroupResponseModel(Model):
    id: Optional[int] = None
    pixel: Optional[str] = None


DeleteAdsResponseModel = List[int]


DeleteCampaignsResponseModel = int


DeleteClientsResponseModel = int

GetAccountsResponseModel = List[AdsAccount]

GetAdsLayoutResponseModel = List[AdsAdLayout]

GetAdsTargetingResponseModel = List[AdsTargSettings]

GetAdsResponseModel = List[AdsAd]


GetBudgetResponseModel = int

GetCampaignsResponseModel = List[AdsCampaign]


class GetCategoriesResponseModel(Model):
    v1: Optional[List["AdsCategory"]] = None
    v2: Optional[List["AdsCategory"]] = None


GetClientsResponseModel = List[AdsClient]

GetDemographicsResponseModel = List[AdsDemoStats]

GetFloodStatsResponseModel = Optional[AdsFloodStats]


class GetLookalikeRequestsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["AdsLookalikeRequest"]] = None


class GetMusiciansResponseModel(Model):
    items: Optional[List["AdsMusician"]] = None


GetOfficeUsersResponseModel = List[AdsUsers]

GetPostsReachResponseModel = List[AdsPromotedPostReach]

GetRejectionReasonResponseModel = Optional[AdsRejectReason]

GetStatisticsResponseModel = List[AdsStats]

GetSuggestionsCitiesResponseModel = List[AdsTargSuggestionsCities]

GetSuggestionsRegionsResponseModel = List[AdsTargSuggestionsRegions]

GetSuggestionsResponseModel = List[AdsTargSuggestions]

GetSuggestionsSchoolsResponseModel = List[AdsTargSuggestionsSchools]

GetTargetGroupsResponseModel = List[AdsTargetGroup]

GetTargetingStatsResponseModel = Optional[AdsTargStats]


GetUploadURLResponseModel = str


GetVideoUploadURLResponseModel = str


ImportTargetContactsResponseModel = int


RemoveOfficeUsersResponseModel = bool


UpdateAdsResponseModel = List[int]


UpdateCampaignsResponseModel = int


UpdateClientsResponseModel = int

AddOfficeUsersResponse.update_forward_refs()
CheckLinkResponse.update_forward_refs()
CreateAdsResponse.update_forward_refs()
CreateCampaignsResponse.update_forward_refs()
CreateClientsResponse.update_forward_refs()
CreateTargetGroupResponse.update_forward_refs()
DeleteAdsResponse.update_forward_refs()
DeleteCampaignsResponse.update_forward_refs()
DeleteClientsResponse.update_forward_refs()
GetAccountsResponse.update_forward_refs()
GetAdsLayoutResponse.update_forward_refs()
GetAdsTargetingResponse.update_forward_refs()
GetAdsResponse.update_forward_refs()
GetBudgetResponse.update_forward_refs()
GetCampaignsResponse.update_forward_refs()
GetCategoriesResponse.update_forward_refs()
GetClientsResponse.update_forward_refs()
GetDemographicsResponse.update_forward_refs()
GetFloodStatsResponse.update_forward_refs()
GetLookalikeRequestsResponse.update_forward_refs()
GetMusiciansResponse.update_forward_refs()
GetOfficeUsersResponse.update_forward_refs()
GetPostsReachResponse.update_forward_refs()
GetRejectionReasonResponse.update_forward_refs()
GetStatisticsResponse.update_forward_refs()
GetSuggestionsCitiesResponse.update_forward_refs()
GetSuggestionsRegionsResponse.update_forward_refs()
GetSuggestionsResponse.update_forward_refs()
GetSuggestionsSchoolsResponse.update_forward_refs()
GetTargetGroupsResponse.update_forward_refs()
GetTargetingStatsResponse.update_forward_refs()
GetUploadURLResponse.update_forward_refs()
GetVideoUploadURLResponse.update_forward_refs()
ImportTargetContactsResponse.update_forward_refs()
RemoveOfficeUsersResponse.update_forward_refs()
UpdateAdsResponse.update_forward_refs()
UpdateCampaignsResponse.update_forward_refs()
UpdateClientsResponse.update_forward_refs()

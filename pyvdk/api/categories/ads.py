# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Ads(Category):

    def add_office_users(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("addOfficeUsers", locals())

    def check_link(
        self,
        account_id: int = None,
        link_type: str = None,
        link_url: str = None,
        campaign_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("checkLink", locals())

    def create_ads(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("createAds", locals())

    def create_campaigns(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("createCampaigns", locals())

    def create_clients(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("createClients", locals())

    def create_target_group(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        name: str = None,
        lifetime: int = None,
        target_pixel_id: Optional[int] = None,
        target_pixel_rules: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("createTargetGroup", locals())

    def delete_ads(
        self,
        account_id: int = None,
        ids: str = None,
        **kwargs
    ) -> dict:
        return self._request("deleteAds", locals())

    def delete_campaigns(
        self,
        account_id: int = None,
        ids: str = None,
        **kwargs
    ) -> dict:
        return self._request("deleteCampaigns", locals())

    def delete_clients(
        self,
        account_id: int = None,
        ids: str = None,
        **kwargs
    ) -> dict:
        return self._request("deleteClients", locals())

    def delete_target_group(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        target_group_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("deleteTargetGroup", locals())

    def get_accounts(
        self,
        **kwargs
    ) -> dict:
        return self._request("getAccounts", locals())

    def get_ads(
        self,
        account_id: int = None,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        only_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAds", locals())

    def get_ads_layout(
        self,
        account_id: int = None,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAdsLayout", locals())

    def get_ads_targeting(
        self,
        account_id: int = None,
        ad_ids: Optional[str] = None,
        campaign_ids: Optional[str] = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getAdsTargeting", locals())

    def get_budget(
        self,
        account_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getBudget", locals())

    def get_campaigns(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        include_deleted: Optional[bool] = None,
        campaign_ids: Optional[str] = None,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getCampaigns", locals())

    def get_categories(
        self,
        lang: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getCategories", locals())

    def get_clients(
        self,
        account_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getClients", locals())

    def get_demographics(
        self,
        account_id: int = None,
        ids_type: str = None,
        ids: str = None,
        period: str = None,
        date_from: str = None,
        date_to: str = None,
        **kwargs
    ) -> dict:
        return self._request("getDemographics", locals())

    def get_flood_stats(
        self,
        account_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getFloodStats", locals())

    def get_lookalike_requests(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        requests_ids: Optional[str] = None,
        offset: Optional[int] = None,
        limit: Optional[int] = None,
        sort_by: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getLookalikeRequests", locals())

    def get_musicians(
        self,
        artist_name: str = None,
        **kwargs
    ) -> dict:
        return self._request("getMusicians", locals())

    def get_office_users(
        self,
        account_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getOfficeUsers", locals())

    def get_posts_reach(
        self,
        account_id: int = None,
        ids_type: str = None,
        ids: str = None,
        **kwargs
    ) -> dict:
        return self._request("getPostsReach", locals())

    def get_rejection_reason(
        self,
        account_id: int = None,
        ad_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getRejectionReason", locals())

    def get_statistics(
        self,
        account_id: int = None,
        ids_type: str = None,
        ids: str = None,
        period: str = None,
        date_from: str = None,
        date_to: str = None,
        stats_fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getStatistics", locals())

    def get_suggestions(
        self,
        section: str = None,
        ids: Optional[str] = None,
        q: Optional[str] = None,
        country: Optional[int] = None,
        cities: Optional[str] = None,
        lang: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getSuggestions", locals())

    def get_target_groups(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        extended: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getTargetGroups", locals())

    def get_targeting_stats(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        criteria: Optional[str] = None,
        ad_id: Optional[int] = None,
        ad_format: Optional[int] = None,
        ad_platform: Optional[str] = None,
        ad_platform_no_wall: Optional[str] = None,
        ad_platform_no_ad_network: Optional[str] = None,
        link_url: str = None,
        link_domain: Optional[str] = None,
        need_precise: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getTargetingStats", locals())

    def get_upload_u_r_l(
        self,
        ad_format: int = None,
        icon: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getUploadURL", locals())

    def get_video_upload_u_r_l(
        self,
        **kwargs
    ) -> dict:
        return self._request("getVideoUploadURL", locals())

    def import_target_contacts(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        target_group_id: int = None,
        contacts: str = None,
        **kwargs
    ) -> dict:
        return self._request("importTargetContacts", locals())

    def remove_office_users(
        self,
        account_id: int = None,
        ids: str = None,
        **kwargs
    ) -> dict:
        return self._request("removeOfficeUsers", locals())

    def update_ads(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("updateAds", locals())

    def update_campaigns(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("updateCampaigns", locals())

    def update_clients(
        self,
        account_id: int = None,
        data: str = None,
        **kwargs
    ) -> dict:
        return self._request("updateClients", locals())

    def update_target_group(
        self,
        account_id: int = None,
        client_id: Optional[int] = None,
        target_group_id: int = None,
        name: str = None,
        domain: Optional[str] = None,
        lifetime: int = None,
        target_pixel_id: Optional[int] = None,
        target_pixel_rules: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("updateTargetGroup", locals())

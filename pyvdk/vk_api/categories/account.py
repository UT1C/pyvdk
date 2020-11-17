# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Account(Category):

    def ban(
        self,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("ban", locals())

    def change_password(
        self,
        restore_sid: Optional[str] = None,
        change_password_hash: Optional[str] = None,
        old_password: Optional[str] = None,
        new_password: str = None,
        **kwargs
    ) -> dict:
        return self._request("changePassword", locals())

    def get_active_offers(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getActiveOffers", locals())

    def get_app_permissions(
        self,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getAppPermissions", locals())

    def get_banned(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getBanned", locals())

    def get_counters(
        self,
        filter: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getCounters", locals())

    def get_info(
        self,
        fields: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("getInfo", locals())

    def get_profile_info(
        self,
        **kwargs
    ) -> dict:
        return self._request("getProfileInfo", locals())

    def get_push_settings(
        self,
        device_id: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("getPushSettings", locals())

    def register_device(
        self,
        token: str = None,
        device_model: Optional[str] = None,
        device_year: Optional[int] = None,
        device_id: str = None,
        system_version: Optional[str] = None,
        settings: Optional[str] = None,
        sandbox: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("registerDevice", locals())

    def save_profile_info(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
        maiden_name: Optional[str] = None,
        screen_name: Optional[str] = None,
        cancel_request_id: Optional[int] = None,
        sex: Optional[int] = None,
        relation: Optional[int] = None,
        relation_partner_id: Optional[int] = None,
        bdate: Optional[str] = None,
        bdate_visibility: Optional[int] = None,
        home_town: Optional[str] = None,
        country_id: Optional[int] = None,
        city_id: Optional[int] = None,
        status: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("saveProfileInfo", locals())

    def set_info(
        self,
        name: Optional[str] = None,
        value: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("setInfo", locals())

    def set_name_in_menu(
        self,
        user_id: int = None,
        name: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("setNameInMenu", locals())

    def set_offline(
        self,
        **kwargs
    ) -> dict:
        return self._request("setOffline", locals())

    def set_online(
        self,
        voip: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("setOnline", locals())

    def set_push_settings(
        self,
        device_id: str = None,
        settings: Optional[str] = None,
        key: Optional[str] = None,
        value: Optional[list] = None,
        **kwargs
    ) -> dict:
        return self._request("setPushSettings", locals())

    def set_silence_mode(
        self,
        device_id: Optional[str] = None,
        time: Optional[int] = None,
        peer_id: Optional[int] = None,
        sound: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("setSilenceMode", locals())

    def unban(
        self,
        owner_id: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("unban", locals())

    def unregister_device(
        self,
        device_id: Optional[str] = None,
        sandbox: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("unregisterDevice", locals())

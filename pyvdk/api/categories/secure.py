# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Secure(Category):

    def add_app_event(
        self,
        user_id: int = None,
        activity_id: int = None,
        value: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("addAppEvent", locals())

    def check_token(
        self,
        token: Optional[str] = None,
        ip: Optional[str] = None,
        **kwargs
    ) -> dict:
        return self._request("checkToken", locals())

    def get_app_balance(
        self,
        **kwargs
    ) -> dict:
        return self._request("getAppBalance", locals())

    def get_s_m_s_history(
        self,
        user_id: Optional[int] = None,
        date_from: Optional[int] = None,
        date_to: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getSMSHistory", locals())

    def get_transactions_history(
        self,
        type: Optional[int] = None,
        uid_from: Optional[int] = None,
        uid_to: Optional[int] = None,
        date_from: Optional[int] = None,
        date_to: Optional[int] = None,
        limit: Optional[int] = None,
        **kwargs
    ) -> dict:
        return self._request("getTransactionsHistory", locals())

    def get_user_level(
        self,
        user_ids: list = None,
        **kwargs
    ) -> dict:
        return self._request("getUserLevel", locals())

    def give_event_sticker(
        self,
        user_ids: list = None,
        achievement_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("giveEventSticker", locals())

    def send_notification(
        self,
        user_ids: Optional[list] = None,
        user_id: Optional[int] = None,
        message: str = None,
        **kwargs
    ) -> dict:
        return self._request("sendNotification", locals())

    def send_s_m_s_notification(
        self,
        user_id: int = None,
        message: str = None,
        **kwargs
    ) -> dict:
        return self._request("sendSMSNotification", locals())

    def set_counter(
        self,
        counters: Optional[list] = None,
        user_id: Optional[int] = None,
        counter: Optional[int] = None,
        increment: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("setCounter", locals())

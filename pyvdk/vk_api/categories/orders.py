# -*- coding: utf-8 -*-
#
from typing import Optional

from ..category import Category


class Orders(Category):

    def cancel_subscription(
        self,
        user_id: int = None,
        subscription_id: int = None,
        pending_cancel: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("cancelSubscription", locals())

    def change_state(
        self,
        order_id: int = None,
        action: str = None,
        app_order_id: Optional[int] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("changeState", locals())

    def get(
        self,
        offset: Optional[int] = None,
        count: Optional[int] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("get", locals())

    def get_amount(
        self,
        user_id: int = None,
        votes: list = None,
        **kwargs
    ) -> dict:
        return self._request("getAmount", locals())

    def get_by_id(
        self,
        order_id: Optional[int] = None,
        order_ids: Optional[list] = None,
        test_mode: Optional[bool] = None,
        **kwargs
    ) -> dict:
        return self._request("getById", locals())

    def get_user_subscription_by_id(
        self,
        user_id: int = None,
        subscription_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getUserSubscriptionById", locals())

    def get_user_subscriptions(
        self,
        user_id: int = None,
        **kwargs
    ) -> dict:
        return self._request("getUserSubscriptions", locals())

    def update_subscription(
        self,
        user_id: int = None,
        subscription_id: int = None,
        price: int = None,
        **kwargs
    ) -> dict:
        return self._request("updateSubscription", locals())

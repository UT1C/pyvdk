from typing import Any, Callable, Dict, List, Tuple

from ..logging import log
from ..rule import ABCRule, MessageTextRule, MessageRegexRule
from ..types import Message
from ..vk_api import ABCAPI
from .abc import ABCLabeler, ABCView
from .event_types import GroupEventType
from .handler import Handler


logger = log.getLogger("event/labeler")


class Labeler(ABCLabeler):
    def __init__(self, view: ABCView, endpoint_default: bool):
        self._view = view
        self._endpoint_default = endpoint_default

    def message_new(
        self,
        *rules,
        text: str = None,
        lower: bool = True,
        regex: str = None,
        endpoint: bool = None
    ) -> Callable:
        def decorator(func):

            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if text is not None:
                _rules.append(
                    MessageTextRule(text, lower=lower)
                )

            if regex is not None:
                _rules.append(
                    MessageRegexRule(regex)
                )

            if endpoint is None:
                _endpoint = self._endpoint_default
            else:
                _endpoint = endpoint

            handler = Handler(func, *_rules, endpoint=_endpoint)
            self._view.add(GroupEventType.MESSAGE_NEW, handler)

        return decorator

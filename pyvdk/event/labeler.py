from typing import Any, Callable, Dict, List, Tuple

from ..custom_logging import log
from ..rule import ABCRule, MessageTextRule
from ..types import Message
from ..vk_api import ABCAPI
from .abc import ABCLabeler, ABCView
from .event_types import GroupEventType
from .handler import Handler


logger = log.getLogger("event/labeler")


class Labeler(ABCLabeler):
    def __init__(self, view: ABCView, default_endpoint: bool):
        self._view = view
        self._default_endpoint = default_endpoint

    def message_new(
        self,
        *rules,
        text: str = None,
        lower: bool = True,
        regex: Any = None,
        endpoint: bool = None
    ) -> Callable:
        def decorator(func):
            nonlocal text, lower, regex, endpoint

            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if text is not None:
                _rules.append(
                    MessageTextRule(text, lower=lower)
                )

            if regex is not None:
                # TODO: regexrule there
                ...
            
            if endpoint is None:
                endpoint = self._default_endpoint

            handler = Handler(func, *rules, endpoint=endpoint)
            self._view.add(GroupEventType.MESSAGE_NEW, handler)

        return decorator

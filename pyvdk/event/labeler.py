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
    def __init__(self, view: ABCView):
        self.view = view

    def message_new(self, *rules, **kw):
        def decorator(func):
            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if "text" in kw:
                _rules.append(
                    MessageTextRule(kw["text"], lower=kw.get("lower", True))
                )

            if "regex" in kw:
                # TODO: regexrule there
                ...

            handler = Handler(func, *rules)
            self.view.add(GroupEventType.MESSAGE_NEW, handler)

        return decorator

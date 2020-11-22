from typing import Any, Callable, Dict, List, Tuple, Union
import vbml

from ..logging import log
from ..rules import (
    ABCRule,
    TextRule,
    RegexRule,
    VBMLRule
)
from ..types import Message
from ..vk_api import ABCAPI
from .abc import ABCLabeler, ABCView, ABCHandler
from .event_types import GroupEventType
from .handler import Handler


logger = log.getLogger("event/labeler")


class Labeler(ABCLabeler):
    """  """
    
    def __init__(self, view: ABCView, endpoint_default: bool):
        self._view = view
        self._endpoint_default = endpoint_default

    def message_new(
        self,
        *rules,
        text: str = None,
        lower: bool = True,
        regex: str = None,
        pattern: Union[str, List[str]] = None,
        level: int = 0,
        endpoint: bool = None
    ) -> Callable:
        def decorator(func) -> ABCHandler:

            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if text is not None:
                _rules.append(
                    TextRule(text, lower=lower)
                )

            if regex is not None:
                _rules.append(
                    RegexRule(regex)
                )
            
            if pattern is not None:
                _rules.append(
                    VBMLRule(pattern)
                )

            if endpoint is None:
                _endpoint = self._endpoint_default
            else:
                _endpoint = endpoint

            handler = Handler(
                func,
                GroupEventType.MESSAGE_NEW,
                *_rules,
                level=level,
                endpoint=_endpoint
            )
            self._view.add(handler)
            return handler

        return decorator

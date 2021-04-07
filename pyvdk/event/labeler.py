from typing import Any, Callable, List, Union, Dict

from ..logging import log
from ..rules import (
    ABCRule,
    RegexRule,
    TextRule,
    VBMLRule,
)
from ..api import ABCAPI
from .abc import ABCHandler, ABCLabeler, ABCView
from .view import MessageView, RawView, AnyView
from ..types.events import GroupEventType
from .handler import Handler

logger = log.getLogger("event/labeler")


class Labeler(ABCLabeler):
    """  """

    def __init__(self, api: ABCAPI, endpoint_default: bool):
        self._message_view = MessageView(api)
        self._raw_view = RawView(api)
        self._any_view = AnyView(api)
        self._endpoint_default = endpoint_default

    def message(
        self,
        *rules,
        text: str = None,
        lower: bool = True,
        regex: str = None,
        pattern: Union[str, List[str]] = None,
        level: int = 0,
        endpoint: bool = None
    ) -> Callable[[Callable], ABCHandler]:
        def decorator(func) -> ABCHandler:

            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if text is not None:
                _rules.append(TextRule(text, lower=lower))

            if regex is not None:
                _rules.append(RegexRule(regex))

            if pattern is not None:
                _rules.append(VBMLRule(pattern))

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
            self._message_view.add(handler)
            return handler

        return decorator

    def raw(
        self,
        event_type: Union[str, GroupEventType],
        dataclass: Callable = dict,
        *rules: ABCRule,
        level: int = 0,
        endpoint: bool = None
    ) -> Callable[[Callable], ABCHandler]:

        if not isinstance(event_type, GroupEventType):
            event_type = GroupEventType(event_type)

        def decorator(func) -> ABCHandler:
            _rules = list(i for i in rules if isinstance(i, ABCRule))

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
            self._raw_view.add(handler, dataclass)
            return handler

        return decorator

    def any(
        self,
        *rules: ABCRule,
        level: int = 0,
        endpoint: bool = None
    ) -> Callable[[Callable], ABCHandler]:

        def decorator(func) -> ABCHandler:
            _rules = list(i for i in rules if isinstance(i, ABCRule))

            if endpoint is None:
                _endpoint = self._endpoint_default
            else:
                _endpoint = endpoint

            handler = Handler(
                func,
                GroupEventType.MESSAGE_NEW,  # FIXME: any event type
                *_rules,
                level=level,
                endpoint=_endpoint
            )
            self._any_view.add(handler)
            return handler

        return decorator

    def process(self, event: dict):
        for view in self.views().values():
            try:
                if view.processible(event):
                    view.process(event)
            except Exception:
                logger.exception("error during forwarding event in views")

    def views(self) -> Dict[str, "ABCView"]:
        return {
            "message": self._message_view,
            "raw": self._raw_view,
            "any": self._any_view,
        }

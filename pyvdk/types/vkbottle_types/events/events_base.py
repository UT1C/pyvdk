from typing import Union, Dict, Type, Callable, Any, TYPE_CHECKING
from .enum import GroupEventType


if TYPE_CHECKING:
    from .typings import GroupTypes
    from .bot_events import BaseGroupEvent


class EventsBase:
    events_registered: Dict[
        GroupEventType,
        Type["GroupTypes.UnifiedTypes"],
    ] = {}

    def __init__(
        self,
        type_enum: Type[GroupEventType],
        on_undefined: Callable[[str], Any] = lambda et: exec(
            f"raise NotImplementedError({et})"
        ),
    ):
        self.type_enum = type_enum
        self.on_undefined = on_undefined

    def register(
        self,
        event_type: GroupEventType,
        event_model: "BaseGroupEvent",
    ):
        self.events_registered[event_type] = event_model

    def get(
        self, event_type: Union[int, str, GroupEventType]
    ) -> Callable[..., "GroupTypes.UnifiedTypes"]:
        if not str(event_type).startswith(self.type_enum.__name__):
            event_type = self.type_enum(event_type)

        model = self.events_registered.get(event_type)
        if model is None:
            return self.on_undefined(event_type)
        return model

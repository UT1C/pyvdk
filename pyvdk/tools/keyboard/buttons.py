from typing import Any, Iterable, List, Dict, Optional, Union
from urllib.parse import urlencode
from dataclasses import dataclass
import json

from .abc import ABCKeyboard, ABCRow, ABCButton


class Row(list, ABCRow):
    """ Объект строки клавиатуры """

    limit_exception = Exception('Maximum row length exceeded!')

    def __init__(
        self,
        *args,
        keyboard: ABCKeyboard,
        limit: int
    ) -> None:

        self.keyboard = keyboard
        self.limit = limit
        super().__init__(*args)

    def __call__(self) -> List[dict]:
        return [i() for i in self]

    def append(self, value: Any) -> None:
        if self.limit == len(self):
            raise self.limit_exception

        self.keyboard._check_count_limit(1)

        super().append(value)

    def extend(self, values: Iterable[Any]) -> None:
        if self.limit < len(self) + len(values):
            raise self.limit_exception

        self.keyboard._check_count_limit(len(values))

        super().extend(values)


@dataclass
class Button(ABCButton):
    """ Объект кнопки """

    color: str

    def __post_init__(self) -> None:
        color = self.color
        payload = self.payload

        self.color = self._colors.get(color, color)

        if payload is not None:
            if not isinstance(payload, dict):
                payload = json.dumps({'command': payload})

    def __call__(self) -> dict:
        action = self.get_action()
        action.update({'payload': self.payload})

        return {
            'color': self.color,
            'action': action
        }


@dataclass
class TextButton(Button):
    label: str
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
        'type': 'text',
        'label': self.label
        }


@dataclass
class LinkButton(Button):
    link: str
    label: str
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
            'type': 'link',
            'link': self.link,
            'label': self.label
        }


@dataclass
class LocationButton(Button):
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
            type: 'location'
        }


@dataclass
class VKPayButton(Button):
    hash: Dict[str, Any]
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
            'type': 'vkpay',
            'hash': urlencode(self.hash)
        }


@dataclass
class AppButton(Button):
    app_id: int
    owner_id: int
    label: str
    hash: str
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
            'type': 'open_app',
            'app_id': self.app_id,
            'owner_id': self.owner_id,
            'label': self.label,
            'hash': self.hash
        }


@dataclass
class CallbackButton(Button):
    label: str
    payload: Optional[Union[str, dict]] = None

    def get_action(self) -> dict:
        return {
            'type': 'callback',
            'label': self.label
        }
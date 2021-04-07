from typing import Any, Dict, Optional, Union
from urllib.parse import urlencode
from dataclasses import dataclass
import json

from .abc import ABCButton, ColorData


class Button(ABCButton, ColorData):
    """ Объект кнопки """

    def __init__(self, payload: Optional[Union[str, dict]] = None) -> None:
        if payload is None:
            payload = dict()
        elif not isinstance(payload, dict):
            payload = {'command': payload}

        self.payload = json.dumps(payload)

    def __call__(self) -> dict:
        action = self.get_action()

        return {
            'action': action
        }


class TextButton(Button):
    label: str
    color: str

    def __init__(
        self,
        label: str,
        color: str,
        payload: Optional[Union[str, dict]] = None
    ) -> None:
        self.label = label
        self.color = self._colors.get(color, color)
        super().__init__(payload)

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

from typing import Any, Iterable, List, Optional, Union, TYPE_CHECKING
import json
from urllib.parse import urlencode

if TYPE_CHECKING:
    from .keyboard import Keyboard


class Row(list):
    """ Объект строки клавиатуры """

    limit_exception = Exception('Maximum row length exceeded!')

    def __init__(
        self,
        *args,
        keyboard: "Keyboard",
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


class ButtonData:
    """
    Содержит константы и генераторы поля action.
    Просто для удобства.

    text:
    - label: str

    link:
    - link: str
    - label: str

    location

    vkpay:
    - hash: Dict[str, Any]

    app:
    - app_id: int
    - owner_id: int
    - label: str
    - hash: str

    callback:
    - label: str
    """

    B = BLUE = PRIMARY = 'primary'
    W = WHITE = SECONDARY = 'secondary'
    R = RED = NEGATIVE = 'negative'
    G = GREEN = POSITIVE = 'positive'
    _colors = {
        'blue': B,
        'b': B,
        'white': W,
        'w': W,
        'red': R,
        'r': R,
        'green': G,
        'g': G
    }

    text = lambda label: {
        'type': 'text',
        'label': label
    }

    link = lambda link, label: {
        'type': 'link',
        'link': link,
        'label': label
    }

    location = lambda: {
        type: 'location'
    }

    vkpay = lambda hash: {
        'type': 'vkpay',
        'hash': urlencode(hash)
    }

    app = lambda app_id, owner_id, label, hash: {
        'type': 'open_app',
        'app_id': app_id,
        'owner_id': owner_id,
        'label': label,
        'hash': hash
    }

    callback = lambda label: {
        'type': 'callback',
        'label': label
    }


class Button(ButtonData):
    """ Объект кнопки """

    def __init__(
        self,
        color: str,
        action: dict,
        payload: Optional[Union[str, dict]] = None
    ) -> None:

        self.color = self._colors.get(color, color)

        if payload is not None:
            if not isinstance(payload, dict):
                payload = {'command': payload}
            action.update({'payload': json.dumps(payload)})

        self.action = action

    def __call__(self) -> dict:
        return {
            'color': self.color,
            'action': self.action
        }
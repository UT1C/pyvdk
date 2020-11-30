from typing import Optional, Union
from abc import ABC, abstractmethod


class ColorData:
    """
    Содержит константы цветов.
    Просто для удобства.
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


class ABCKeyboard(ABC, ColorData):
    ...


class ABCRow(ABC):
    ...


class ABCButton(ABC, ColorData):
    color: str
    payload: Optional[Union[str, dict]] = None

    @abstractmethod
    def __call__(self) -> dict:
        ...

    def get_action(self) -> dict:
        ...
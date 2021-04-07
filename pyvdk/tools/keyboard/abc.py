from typing import Optional, Union, Deque, Tuple, Iterable, List
from abc import ABC, abstractmethod, abstractproperty


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


class ABCKeyboard(ABC):
    one_time: bool
    inline: bool
    buttons: List[Deque["ABCButton"]]
    size_limit: Tuple[int, int]
    count_limit: int

    @abstractproperty
    def count(self) -> int:
        ...

    @abstractmethod
    def __init__(
        self,
        one_time: bool = False,
        inline: bool = False
    ) -> None:
        ...

    @abstractmethod
    def __getitem__(self, value: int) -> "ABCKeyboard":
        ...

    @abstractmethod
    def __call__(self) -> str:
        ...

    @abstractmethod
    def append(self, button: "ABCButton", row: Optional[int] = 0):
        ...

    @abstractmethod
    def appendleft(self, button: "ABCButton", row: int = 0):
        ...

    @abstractmethod
    def extend(self, buttons: Iterable["ABCButton"], row: int = 0):
        ...

    @abstractmethod
    def extendleft(self, buttons: Iterable["ABCButton"], row: int = 0):
        ...


class ABCButton(ABC):
    payload: dict

    @abstractmethod
    def __call__(self) -> dict:
        ...

    @abstractmethod
    def get_action(self) -> dict:
        ...

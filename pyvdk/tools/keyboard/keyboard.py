from typing import Iterable, Optional, List
from collections import deque
import json

from .abc import ABCButton, ABCKeyboard, ColorData


class Keyboard(ABCKeyboard, ColorData):
    """ Объект клавиатуры """

    __selected_row: Optional[int] = None

    @property
    def count(self) -> int:
        return sum([len(row) for row in self.buttons])

    def __init__(
        self,
        one_time: bool = False,
        inline: bool = False
    ) -> None:

        self.one_time = one_time
        self.inline = inline

        if inline:
            self.size_limit = 5, 6
            self.count_limit = 10
        else:
            self.size_limit = 5, 10
            self.count_limit = 40

        x, y = self.size_limit
        self.buttons = [
            deque(maxlen=x)
            for i in range(y)
        ]

    def __getitem__(self, value: int) -> ABCKeyboard:
        self.__selected_row = value
        return self

    def __call__(self) -> str:
        data = {
            'one_time': self.one_time,
            'inline': self.inline,
            'buttons': self._get_buttons()
        }
        return json.dumps(data)

    def append(self, button: ABCButton, row: int = 0):
        self._get_row(row).append(button)
        self._check_count()

    def appendleft(self, button: ABCButton, row: int = 0):
        self._get_row(row).appendleft(button)
        self._check_count()

    def extend(self, buttons: Iterable[ABCButton], row: int = 0):
        self._get_row(row).extend(buttons)
        self._check_count()

    def extendleft(self, buttons: Iterable[ABCButton], row: int = 0):
        self._get_row(row).extendleft(buttons)
        self._check_count()

    def _get_row(self, row: Optional[int]) -> deque:
        if row == 0 and self.__selected_row is not None:
            row = self.__selected_row
            self.__selected_row = None
        return self.buttons[row]

    def _get_buttons(self) -> List[List[str]]:
        return [
            [button() for button in row]
            for row in self.buttons
            if len(row) > 0
        ]

    def _check_count(self):
        if self.count_limit < self.count:
            raise Exception('Max keyboard length exceeded!')

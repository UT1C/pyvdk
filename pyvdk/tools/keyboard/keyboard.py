from typing import List, Tuple
import json

from .buttons import Row
from .abc import ABCButton, ABCKeyboard


class Keyboard(ABCKeyboard):
    """ Объект клавиатуры """

    one_time: bool
    inline: bool
    buttons: "List[Row[ABCButton]]"
    size_limit: Tuple[int, int]
    count_limit: int

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
            Row(keyboard=self, limit=x)
            for i in range(y)
        ]

    def __getitem__(self, value: int) -> Row:
        return self.buttons[value]

    def __call__(self) -> str:
        data = {
            'one_time': self.one_time,
            'inline': self.inline,
            'buttons': [
                row()
                for row in self.buttons
                if len(row) > 0
            ]
        }
        return json.dumps(data)

    def append(self, button: ABCButton, row: int = 0):
        self.buttons[row].append(button)

    def extend(self, buttons: List[ABCButton], row: int = 0):
        self.buttons[row].extend(buttons)

    def _check_count_limit(self, n: int):
        """  """

        if self.count + n > self.count_limit:
            raise Exception(
                'The limit on buttons count has been exceeded! Extend was ignored.'
            )
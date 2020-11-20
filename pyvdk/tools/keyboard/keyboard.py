from typing import List, Tuple
import json

from ..logger import logger
from .buttons import Button, Row


class Keyboard:
    """ Объект клавиатуры """

    one_time: bool
    inline: bool
    _buttons: "List[Row[Button]]"
    _count: int
    _size_limit: Tuple[int, int]
    _count_limit: int

    def __init__(
        self,
        one_time: bool = False,
        inline: bool = False
    ) -> None:

        self.one_time = one_time
        self.inline = inline

        if inline:
            self._size_limit = 5, 6
            self._count_limit = 10
        else:
            self._size_limit = 5, 10
            self._count_limit = 40

        x, y = self._size_limit
        self._count = 0
        self._buttons = [
            Row(limit=x)
            for i in range(y)
        ]
    
    def __getitem__(self, value: int) -> Row:
        return self._buttons[value]
    
    def __call__(self) -> str:
        data = {
            'one_time': self.one_time,
            'inline': self.inline,
            'buttons': [
                row()
                for row in self._buttons
                if len(row) > 0
            ]
        }
        return json.dumps(data)
    
    def append(self, button: Button, level: int = 0):
        """  """

        if self._count_limit == self._count:
            logger.warning('The limit on buttons count has been exceeded! Append was ignored.')
            return
        self._count += 1

        try:
            self._buttons[level].append(button)
        except Exception as e:
            logger.exception('Exception occured!')

    def extend(self, buttons: List[Button], level: int = 0):
        """  """
        
        if self._count_limit < self._count + len(buttons):
            logger.warning('The limit on buttons count has been exceeded! Extend was ignored.')
            return
        self._count += len(buttons)

        try:
            self._buttons[level].extend(buttons)
        except Exception as e:
            logger.exception('Exception occured!')
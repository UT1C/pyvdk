from typing import _T, Iterable, List


class Row(list):
    """  """

    _limit: int
    _limit_exception = Exception('Maximum row length exceeded!')

    def __init__(self, *args, limit: int) -> None:
        self._limit = limit
        super().__init__(*args)
    
    def __call__(self) -> List[dict]:
        pass

    def append(self, value: _T) -> None:
        if self._limit == len(self):
            raise self._limit_exception

        super().append(value)
    
    def extend(self, values: Iterable[_T]) -> None:
        if self._limit >= len(self) + len(values):
            raise self._limit_exception
        
        super().extend(values)


class Button:
    """  """

    pass
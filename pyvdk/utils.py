from typing import Any
from collections.abc import Iterable
from pathlib import Path

import jinja2


class DictToObject:
    """ Transforms dict to object """

    _raw_data: dict

    def __init__(self, dict_object: dict) -> None:
        self._data = dict_object
        for k, v in dict_object.items():
            selected = self.type_handle(v)
            self.__setattr__(k, selected)

    def __repr__(self) -> str:
        return f"<DictToObject: {self._raw_data}>"

    def get(self, attr: str) -> Any:
        """ Get attribute """

        return self._raw_data.get(attr)

    @classmethod
    def type_handle(cls, x: Any) -> Any:
        """ Handle types """

        if isinstance(x, dict):
            return cls(x)
        elif isinstance(x, Iterable):
            return (cls.type_handle(i) for i in x)
        return x


def form_render(path: str, **kwargs) -> str:
    """ Just jinja2 """

    file_text = Path(path).read_text()
    template = jinja2.Template(file_text)
    return template.render(**kwargs)


def get_chat_id(peer_id: int) -> int:
    """ Получает chat_id из peer_id """

    return peer_id - 2e9


def gen_alias(id: int, label: str) -> str:
    return f"[{id}|{label}]"
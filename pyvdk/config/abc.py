from abc import ABC


class ABCConfig(ABC):
    """ Абстрактный объект конфига """

    group_id: int
    secret: str
    confcode: str
    token: str
    v: str
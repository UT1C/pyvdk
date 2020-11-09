import yaml
from dataclasses import dataclass


@dataclass
class Config:
    """ Конфиг бота """

    token: str = None
    v: float = None
    group_id: int = None
    confcode: str = None
    secret: str = None

    def from_args(self, **kwargs) -> "Config":
        """ Подгружает данные из аргументов """

        for k, v in kwargs.items():
            self.__setattr__(k, v)
            
        return self

    def from_yaml(self, path: str) -> "Config":
        """ Подгружает данные из конфига yaml """

        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        for k, v in data.items():
            self.__setattr__(k, v)

        return self
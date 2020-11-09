import yaml
from dataclasses import dataclass


@dataclass
class Config:
    """ Конфиг бота """

    token: str
    group_id: int
    confcode: str
    secret: str
    v: float = 5.124

    def edit_from_args(self, **kwargs):
        """ Подгружает данные из аргументов """

        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def edit_from_yaml(self, path: str):
        """ Подгружает данные из конфига yaml """

        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        for k, v in data.items():
            self.__setattr__(k, v)
    
    @classmethod
    def from_yaml(cls, path: str) -> "Config":
        """ Создает объект конфига из yaml """

        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        
        return cls(**data)
from dataclasses import dataclass
import os
import yaml


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
    
    @classmethod
    def from_environ(cls) -> "Config":
        """
        Создает объект конфига из переменных окружения.

        Стандартные названия переменных:
        PYVDK_TOKEN
        PYVDK_GROUP_ID
        PYVDK_CONFIRMATION_CODE
        PYVDK_SECRET
        PYVDK_API_VERSION
        """

        envs = {
            "TOKEN": str,
            "GROUP_ID": int,
            "CONFIRMATION_CODE": str,
            "SECRET": str,
            "API_VERSION": float
        }
        args = list()
        
        for env_name, env_type in envs.items():
            env = env_type(os.environ.get(f"PYVDK_{env_name}"))
            args.append(env)
        
        return cls(*args)
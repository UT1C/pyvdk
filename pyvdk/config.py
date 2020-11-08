import yaml


class Config:
    """ Конфиг бота """

    group_id: int
    secret: str
    confcode: str
    token: str

    def __init__(self, path: str) -> None:
        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        for k, v in data.items():
            self.__setattr__(k, v)
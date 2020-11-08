import yaml


class Config:
    """ Конфиг бота """

    group_id: int
    secret: str
    confcode: str
    token: str

    def __init__(self, path: str) -> None:
        self.load(path)
    
    def load(self, path: str):
        """ Подгружает данные из конфига """

        with open(path, 'r') as f:
            data = yaml.load(f, Loader=yaml.Loader)
        for k, v in data.items():
            self.__setattr__(k, v)
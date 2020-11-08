from .config import Config


class Bot:
    """ Основной класс бота """

    __config: Config

    def __init__(self, config_path: str) -> None:
        self.__config = Config(config_path)
    
    def request_handle(request: dict) -> str:
        """ Хендлит реквест от вк и возвращает ответ """

        pass
    
    def load_config(self, config_path: str):
        """ Изменяет текущий конфиг """

        self.__config.load(config_path)
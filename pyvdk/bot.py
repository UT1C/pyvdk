from .request_handler import RequestHandler
from .config import Config
from .vk_api import API


class Bot:
    """ Основной класс бота """

    __config: Config
    api: API

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.api = API(self.__config)

    def request_handle(request: dict) -> str:
        """ Хендлит реквест от вк и возвращает ответ """

        return RequestHandler(request).response
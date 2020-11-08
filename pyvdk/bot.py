from .request_handler import RequestHandler
from .config import Config
from .vk_api import API


class Bot:
    """ Основной класс бота """

    __config: Config
    __request_handler: RequestHandler
    api: API

    def __init__(self, config: Config) -> None:
        self.__config = config
        self.api = API(self.__config)
        self.__request_handler = RequestHandler(
            self.__config,
            self.api
        )

    def request_handle(self, request: dict) -> str:
        """ Хендлит реквест от вк и возвращает ответ """

        return self.__request_handler(request).response
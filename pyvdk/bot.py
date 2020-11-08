from .request_handler import RequestHandler
from .config import Config


class Bot:
    """ Основной класс бота """

    __config: Config

    def __init__(self, config: Config) -> None:
        self.__config = config

    def request_handle(request: dict) -> str:
        """ Хендлит реквест от вк и возвращает ответ """

        return RequestHandler(request).response
class Bot:
    """ Основной класс бота """

    __config: object

    def __init__(self, config: object) -> None:
        self.__config = config

    def request_handle(request: dict) -> str:
        """ Хендлит реквест от вк и возвращает ответ """

        pass
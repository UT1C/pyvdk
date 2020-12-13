from . import logging
from .event import View, Labeler
from .config import Config
from .api import API
from .types import Callback

logger = logging.log.getLogger('bot')


class Bot:
    """ Основной класс бота """

    api: API
    on: Labeler
    __config: Config

    def __init__(
        self,
        config: Config,
        endpoint_default: bool = False,
        debug: bool = False
    ) -> None:

        if debug:
            logging.enable_debug()

        self.__config = config
        self.api = API(self.__config)
        self.view = View(self.api)
        self.on = Labeler(self.view, endpoint_default)

    def process(self, request: dict) -> str:
        """ Обрабатывает запрос """

        logger.debug(f'new request: {request}')
        callback = Callback(**request)
        response = self.__check(callback)
        if response == 'ok':
            logger.info(f"new event, type:{callback.type}")
            self.view.process(callback)

        return response

    def __check(self, callback: Callback) -> str:
        """ Проверяет данные реквеста """

        if callback.secret != self.__config.secret:
            logger.debug('secret key is invalid')
            return 'not ok'

        elif callback.type == 'confirmation':
            logger.info('confirmation request')
            return self.__config.confcode

        else:
            return 'ok'

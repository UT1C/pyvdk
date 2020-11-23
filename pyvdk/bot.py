from . import logging
from .event import View, Labeler
from .config import Config
from .vk_api import API


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
            logging.toggle_debug()

        self.__config = config
        self.api = API(self.__config)
        self.view = View(self.api)
        self.on = Labeler(self.view, endpoint_default)

    def request_handle(self, request: dict) -> str:
        """ Handle request from vk and return response """

        logger.debug(f'new request: {request}')
        response = self.__check(request)
        if response == 'ok':
            logger.info(f"new event, type:{request.get('type')}")
            self.view.process(request)

        return response

    def __check(self, request: dict) -> str:
        """ Проверяет данные реквеста """

        if request['secret'] != self.__config.secret:
            logger.debug('secret key is invalid')
            return 'not ok'

        elif request['type'] == 'confirmation':
            logger.info('confirmation request')
            return self.__config.confcode

        else:
            return 'ok'
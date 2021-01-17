from typing import Optional

from . import logging
from .event import (
    ABCView,
    ABCLabeler,
    Labeler
)
from .config import Config
from .api import API, ABCAPI

logger = logging.log.getLogger('bot')


class Bot:
    """ Основной класс бота """

    api: ABCAPI
    labeler: ABCLabeler
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
        # self.view = View(self.api)
        self.labeler = Labeler(self.api, endpoint_default)
        # self.on = Labeler(self.view, endpoint_default)

    @property
    def on(self) -> ABCLabeler:
        return self.labeler

    def add(self, *blueprints: "Blueprint"):
        """ Добавляет хендлеры из блюпринтов в бота """

        for bp in blueprints:
            bp.api = self.api
            views = self.labeler.views()
            for k, v in bp.labeler.views().items():
                views[k].extend(v)

    def process(self, request: dict) -> str:
        """ Обрабатывает запрос """

        logger.debug(f'new request: {request}')
        response = self.__check(request)
        if response == 'ok':
            logger.info(f"new event, type: {request.get('type')}")
            self.labeler.process(request)

        return response

    def __check(self, request: dict) -> str:
        """ Проверяет данные реквеста """

        if request.get("secret") != self.__config.secret:
            logger.debug('secret key is invalid')
            return 'not ok'

        elif request.get("type") == 'confirmation':
            logger.info('confirmation request')
            return self.__config.confcode

        else:
            return 'ok'


class Blueprint:
    """  """

    api: Optional[ABCAPI]
    labeler: ABCLabeler

    def __init__(self, endpoint_default: bool = False) -> None:
        self.api = None
        self.labeler = Labeler(self.api, endpoint_default)

    @property
    def on(self) -> ABCLabeler:
        return self.labeler

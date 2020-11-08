from .config import Config
from .event import EventHandler
from .vk_api import API
from .custom_logging import log


logger = log.getLogger('request_handler')


class RequestHandler:
    """  """

    event_handler: EventHandler
    config: Config
    response: str

    def __init__(self, config: Config, api: API) -> None:
        self.config = config
        self.event_handler = EventHandler(api)
    
    def __call__(self, request: dict) -> str:
        """ Проверяет поступивший реквест """
        
        if self.check(request):
            logger.info('new event')
            self.event_handler.process(request)

        return self.response
    
    def check(self, request: dict) -> bool:
        """ Проверяет данные реквеста """

        if request['secret'] != self.config.secret:
            self.response = 'not ok'
            logger.debug('secret key is invalid')

        elif request['type'] == 'confirmation':
            self.response = self.config.confcode
            logger.info('confirmation request')

        else:
            self.response = 'ok'
            return True
        
        return False
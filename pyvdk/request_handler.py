from .config import Config
from .event import EventHandler

class RequestHandler:
    """  """

    event_handler: EventHandler
    config: Config
    response: str

    def __init__(self, config: Config) -> None:
        self.config = config
        self.event_handler = EventHandler(config)
    
    def __call__(self, request: dict) -> str:
        """ Проверяет поступивший реквест """
        
        if self.check(request):
            pass  # TODO: call event_handler

        return self.response
    
    def check(self, request: dict) -> bool:
        """ Проверяет данные реквеста """

        if request['secret'] != self.config.secret:
            self.response = 'not ok'

        elif request['type'] == 'confirmation':
            self.response = self.config.confcode
        
        else:
            self.response = 'ok'
            return True
        
        return False
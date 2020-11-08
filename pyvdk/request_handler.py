from .config import Config


class RequestHandler:
    """  """

    request: dict
    config: Config
    response: str


    def __init__(self, request: dict, config: Config) -> None:
        self.request = request
        self.config = Config
        
        if self.check():
            pass  # TODO: call eventHandler
    
    def check(self) -> bool:
        """ Проверяет данные реквеста """

        if self.request['secret'] != self.config.secret:
            self.response = 'not ok'

        elif self.request['type'] == 'confirmation':
            self.response = self.config.confcode
        
        else:
            self.response = 'ok'
            return True
        
        return False
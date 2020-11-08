from .config import Config


class Bot:
    """  """

    __config: Config

    def __init__(self, request: dict, config_path: str) -> None:
        self.__config = Config(config_path)
    
    def load_config(self, config_path: str):
        """ Изменяет текущий конфиг """

        self.__config.load(config_path)
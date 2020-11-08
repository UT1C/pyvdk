from .config import Config


class Bot:
    """  """

    __config: Config

    def __init__(self, config_path: str) -> None:
        self.__config = Config(config_path)
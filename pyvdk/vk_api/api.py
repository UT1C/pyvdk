from .abc import ABCAPI

from requests import Session
# from requests.exceptions import ...

from .categories import Messages
from .categories import Groups
from .categories import Users
from .categories import Wall

from ..custom_logging import log
from ..config import Config

logger = log.getLogger('vk_api')


class API(ABCAPI):
    """Класс для вызовов методов api VK

    Examples:

        api = API(config)
        r = api.messages.send(
            message="Сервера сегодня не будет",
            domain="lightmanlp",
            random_id=random.getrandbits(64)
        )

    """

    API_URL = "https://api.vk.com/method/"

    def __init__(self, config: Config) -> None:
        """[summary]

        Args:
            config (Config): [description]
        """
        self.config = config
        self.session = Session()

        self.messages = Messages(self)
        self.users = Users(self)
        self.groups = Groups(self)
        self.wall = Wall(self)

    def request(self, method: str, params: dict) -> dict:
        """ Метод для запроса к апи, "лоу-левел"

        Args:
            method (str): запрашиваемый метод
            params (dict): параметры запроса (отфильтрованные!)

        Returns:
            dict: результат запроса
        """
        try:
            url = self.API_URL + method
            _params = {  # params in url
                "access_token": self.config.token,
                "v": self.config.v
            }
            logger.debug(f"request {method} {params}")
            with self.session.post(url, params=_params, data=params) as r:
                # TODO: find & throw vk error there
                result = r.json()
                logger.debug(f"response: [{r.status_code}] {result}")
                return result

        # TODO: catch network exceptions there
        except Exception as e:
            print(e)
            # NOTE: не сетевые ошибки - поднимать выше
            raise

    def method(self, method: str, **params) -> dict:
        # FIXME: тут нет фильтрации агрументов, она в Category
        raise NotImplementedError()
        # необходимо куда-то вынести тот код, или импортировать сюда класс
        # главное не получить цикличный импорт (хотя с abc не должно быть...)
        return self.request(method, params)

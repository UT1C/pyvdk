from requests import Session
# from requests.exceptions import ...

from ..logging import log
from ..config import Config
from ..tools import prepare_params

logger = log.getLogger('api')


class ABCAPI:
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
            print(e)  # FIXME: log.exception()  (Возможно, я не уверен)
            # NOTE: не сетевые ошибки - поднимать выше
            raise

    def method(self, method: str, **params) -> dict:
        return self.request(method, prepare_params(params))


class ABCCategory:

    __name__: str
    __api: ABCAPI

    def __init__(self, api: ABCAPI) -> None:
        ...

    def _request(self, method: str, params: dict) -> dict:
        ...


if __name__ == "__main__":
    ...

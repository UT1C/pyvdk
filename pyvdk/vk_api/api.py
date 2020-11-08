from .abc import ABCApi

from requests import Session
# from requests.exceptions import ...

from .categories.messages import Messages
from ..custom_logging import log


logger = log.getLogger('vk_api')


class Api(ABCApi):
    API_URL = "https://api.vk.com/method/"

    def __init__(self, token: str, version: str = "5.124") -> None:
        self.__token = token
        self.version = version
        self.session = Session()

        self.messages = Messages(self)

    def request(self, method: str, params: dict) -> dict:
        try:
            url = self.API_URL + method
            _params = {  # params in url
                "access_token": self.__token,
                "v": self.version
            }
            logger.debug(f"request {method} {params}")
            with self.session.post(url, params=_params, data=params) as r:
                # TODO: find & throw vk error there
                return r.json()

        # TODO: catch network exceptions there
        except Exception as e:
            print(e)

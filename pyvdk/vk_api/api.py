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
    API_URL = "https://api.vk.com/method/"

    def __init__(self, config: Config) -> None:
        self.config = config
        self.session = Session()

        self.messages = Messages(self)
        self.users = Users(self)
        self.groups = Groups(self)
        self.wall = Wall(self)

    def request(self, method: str, params: dict) -> dict:
        try:
            url = self.API_URL + method
            _params = {  # params in url
                "access_token": self.config.token,
                "v": self.config.version
            }
            logger.debug(f"request {method} {params}")
            with self.session.post(url, params=_params, data=params) as r:
                # TODO: find & throw vk error there
                return r.json()

        # TODO: catch network exceptions there
        except Exception as e:
            print(e)

from .abc import ABCAPI

from ..config import Config

from .categories import Messages
from .categories import Groups
from .categories import Users
from .categories import Wall


class API(ABCAPI):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.messages = Messages(self)
        self.users = Users(self)
        self.groups = Groups(self)
        self.wall = Wall(self)
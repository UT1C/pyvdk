from requests import Session

from ..config import Config
from . import categories
from .abc import ABCAPI
from ..tools import prepare_params
from ..logging import log


logger = log.getLogger("api")


class RawAPI(ABCAPI):
    """Класс для вызовов методов api VK
    """

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


class API(RawAPI):
    def __init__(self, config: Config) -> None:
        super().__init__(config)

        self.account = categories.Account(self)
        self.ads = categories.Ads(self)
        self.appwidgets = categories.AppWidgets(self)
        self.apps = categories.Apps(self)
        self.auth = categories.Auth(self)
        self.board = categories.Board(self)
        self.database = categories.Database(self)
        self.docs = categories.Docs(self)
        self.downloadedgames = categories.DownloadedGames(self)
        self.fave = categories.Fave(self)
        self.friends = categories.Friends(self)
        self.gifts = categories.Gifts(self)
        self.groups = categories.Groups(self)
        self.leads = categories.Leads(self)
        self.likes = categories.Likes(self)
        self.market = categories.Market(self)
        self.messages = categories.Messages(self)
        self.newsfeed = categories.Newsfeed(self)
        self.notes = categories.Notes(self)
        self.notifications = categories.Notifications(self)
        self.orders = categories.Orders(self)
        self.pages = categories.Pages(self)
        self.photos = categories.Photos(self)
        self.polls = categories.Polls(self)
        self.prettycards = categories.PrettyCards(self)
        self.search = categories.Search(self)
        self.secure = categories.Secure(self)
        self.stats = categories.Stats(self)
        self.status = categories.Status(self)
        self.storage = categories.Storage(self)
        self.stories = categories.Stories(self)
        self.streaming = categories.Streaming(self)
        self.users = categories.Users(self)
        self.utils = categories.Utils(self)
        self.video = categories.Video(self)
        self.wall = categories.Wall(self)
        self.widgets = categories.Widgets(self)

from .abc import ABCAPI

from ..config import Config

from . import categories


class API(ABCAPI):
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

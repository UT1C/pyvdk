from ..custom_logging import log
from ..tools import prepare_params
from .abc import ABCAPI, ABCCategory

logger = log.getLogger("vk_api")


class Category(ABCCategory):
    """
    Базовая категория для всех категорий апи.
    Отфильтровывает и приводит параметры запроса к нужному виду,
    и вызывает `Api.request`
    """

    def __init__(self, api: ABCAPI):
        self.__api = api
        if not hasattr(self, "__name__"):
            self.__name__ = self.__class__.__name__.lower()

    def _request(self, method: str, params: dict):
        return self.__api.request(
            f"{self.__name__}.{method}",
            prepare_params(params)
        )

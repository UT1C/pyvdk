from .abc import ABCAPI, ABCCategory

from ..custom_logging import log


logger = log.getLogger('vk_api')


class Category(ABCCategory):
    """
        Базовая категория для всех категорий апи.
        Отфильтровывает и приводит параметры запроса к нужному виду,
        и вызывает `Api.request`
    """

    def __init__(self, api: ABCAPI):
        self.__api = api
        if not hasattr(self, "__name__"):
            self.__name__ = self.__class__.__name__

    def __request__(self, method: str, params: dict):
        return self.__api.request(
            f"{self.__name__}.{method}",
            self.prepare_params(params)
        )

    @classmethod
    def prepare_params(cls, params: dict) -> dict:
        """
        Метод для фильтрации параметров

        Args:
            params (dict): 'сырые' параметры, не мутируются

        Returns:
            dict: отфильтрованные и приведённые к нужному формату параметры,
            мутированная копия входных
        """
        params = params.copy()  # NOTE: возможно создание копии не нужно?
        if "kwargs" in params:
            params.update(params.pop("kwargs"))
        for k, v in params.items():
            if isinstance(v, (tuple, list)):
                # NOTE: возможно вместо repr нужен str, я пока не уверен
                # объединение списков "[1, 2, 3]" к виду "1,2,3"
                params[k] = ",".join(repr(i) for i in v)
        return {
            k if not k.endswith("_") else k[:-1]: v
            for k, v in params.items()
            if k != "self" and v is not None
        }

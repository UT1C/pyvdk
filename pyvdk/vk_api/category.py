from .abc import ABCApi, ABCCategory


class Category(ABCCategory):

    def __init__(self, api: ABCApi):
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
        params = params.copy()
        if "kwargs" in params:
            params.update(params.pop("kwargs"))
        for k, v in params.items():
            if isinstance(v, (tuple, list)):
                params[k] = ",".join(repr(i) for i in v)
        return {
            k if not k.endswith("_") else k[:-1]: v
            for k, v in params.items()
            if k != "self" and v is not None
        }

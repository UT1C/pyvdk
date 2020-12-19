from abc import ABC, abstractmethod

from requests import Session

from ..config import Config


class ABCAPI(ABC):

    API_URL: str = "https://api.vk.com/method/"
    config: Config
    session: Session

    @abstractmethod
    def __init__(self, config: Config) -> None:
        ...

    @abstractmethod
    def request(self, method: str, params: dict) -> dict:
        ...

    @abstractmethod
    def method(self, method: str, **params) -> dict:
        ...


class ABCCategory:

    __name__: str
    __api: ABCAPI

    def __init__(self, api: ABCAPI) -> None:
        ...

    def _request(self, method: str, params: dict) -> dict:
        ...


if __name__ == "__main__":
    ...

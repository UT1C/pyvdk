from abc import ABC, abstractmethod

from requests import Session


class ABCApi(ABC):

    API_URL: str  # NOTE: to lowercase ?
    __token: str
    version: str
    session: Session

    @abstractmethod
    def __init__(self, token: str, version: str) -> None:
        ...

    @abstractmethod
    def request(self, method: str, params: dict) -> dict:
        ...

    @abstractmethod
    def method(self, method: str, **params: dict) -> dict:
        ...


class ABCCategory(ABC):

    __name__: str
    __api: ABCApi

    @abstractmethod
    def __init__(self, api: ABCApi) -> None:
        ...

    @abstractmethod
    def __request__(self, method: str, params: dict) -> dict:
        ...


if __name__ == "__main__":
    ...

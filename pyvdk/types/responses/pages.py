from typing import Optional, List

from ..objects import (
    PagesWikipageFull,
    PagesWikipageHistory,
    PagesWikipage,
)
from ..abc import Model


class GetHistoryResponse(Model):
    response: Optional["GetHistoryResponseModel"] = None


class GetTitlesResponse(Model):
    response: Optional["GetTitlesResponseModel"] = None


class GetVersionResponse(Model):
    response: Optional["GetVersionResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class ParseWikiResponse(Model):
    response: Optional["ParseWikiResponseModel"] = None


class SaveAccessResponse(Model):
    response: Optional["SaveAccessResponseModel"] = None


class SaveResponse(Model):
    response: Optional["SaveResponseModel"] = None


GetHistoryResponseModel = List[PagesWikipageHistory]

GetTitlesResponseModel = List[PagesWikipage]

GetVersionResponseModel = Optional[PagesWikipageFull]

GetResponseModel = Optional[PagesWikipageFull]

ParseWikiResponseModel = str

SaveAccessResponseModel = int

SaveResponseModel = int

GetHistoryResponse.update_forward_refs()
GetTitlesResponse.update_forward_refs()
GetVersionResponse.update_forward_refs()
GetResponse.update_forward_refs()
ParseWikiResponse.update_forward_refs()
SaveAccessResponse.update_forward_refs()
SaveResponse.update_forward_refs()

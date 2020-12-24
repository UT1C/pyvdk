from typing import Optional, List

from ..objects import WidgetsWidgetPage, WidgetsWidgetComment
from ..abc import Model


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetPagesResponse(Model):
    response: Optional["GetPagesResponseModel"] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    posts: Optional[List["WidgetsWidgetComment"]] = None


class GetPagesResponseModel(Model):
    count: Optional[int] = None
    pages: Optional[List["WidgetsWidgetPage"]] = None


GetCommentsResponse.update_forward_refs()
GetPagesResponse.update_forward_refs()

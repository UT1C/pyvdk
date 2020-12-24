from typing import Optional, List

from ..objects import (
    MarketMarketCategory,
    MarketMarketItem,
    WallWallComment,
    MarketMarketItemFull,
    MarketMarketAlbum,
    BaseBoolInt,
)
from ..abc import Model


class AddAlbumResponse(Model):
    response: Optional["AddAlbumResponseModel"] = None


class AddResponse(Model):
    response: Optional["AddResponseModel"] = None


class CreateCommentResponse(Model):
    response: Optional["CreateCommentResponseModel"] = None


class DeleteCommentResponse(Model):
    response: Optional["DeleteCommentResponseModel"] = None


class GetAlbumByIdResponse(Model):
    response: Optional["GetAlbumByIdResponseModel"] = None


class GetAlbumsResponse(Model):
    response: Optional["GetAlbumsResponseModel"] = None


class GetByIdExtendedResponse(Model):
    response: Optional["GetByIdExtendedResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetCategoriesResponse(Model):
    response: Optional["GetCategoriesResponseModel"] = None


class GetCommentsResponse(Model):
    response: Optional["GetCommentsResponseModel"] = None


class GetExtendedResponse(Model):
    response: Optional["GetExtendedResponseModel"] = None


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class RestoreCommentResponse(Model):
    response: Optional["RestoreCommentResponseModel"] = None


class SearchExtendedResponse(Model):
    response: Optional["SearchExtendedResponseModel"] = None


class SearchResponse(Model):
    response: Optional["SearchResponseModel"] = None


class AddAlbumResponseModel(Model):
    market_album_id: Optional[int] = None


class AddResponseModel(Model):
    market_item_id: Optional[int] = None


CreateCommentResponseModel = int

DeleteCommentResponseModel = Optional[BaseBoolInt]


class GetAlbumByIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketAlbum"]] = None


class GetAlbumsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketAlbum"]] = None


class GetByIdExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class GetByIdResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


class GetCategoriesResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketCategory"]] = None


class GetCommentsResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["WallWallComment"]] = None


class GetExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


RestoreCommentResponseModel = Optional[BaseBoolInt]


class SearchExtendedResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItemFull"]] = None


class SearchResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["MarketMarketItem"]] = None


AddAlbumResponse.update_forward_refs()
AddResponse.update_forward_refs()
CreateCommentResponse.update_forward_refs()
DeleteCommentResponse.update_forward_refs()
GetAlbumByIdResponse.update_forward_refs()
GetAlbumsResponse.update_forward_refs()
GetByIdExtendedResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetCategoriesResponse.update_forward_refs()
GetCommentsResponse.update_forward_refs()
GetExtendedResponse.update_forward_refs()
GetResponse.update_forward_refs()
RestoreCommentResponse.update_forward_refs()
SearchExtendedResponse.update_forward_refs()
SearchResponse.update_forward_refs()

from pydantic import BaseModel
from typing import Optional, Any, TYPE_CHECKING

from .enum import GroupEventType
from . import objects
from .events_base import EventsBase

if TYPE_CHECKING:
    from ...api import ABCAPI


class BaseGroupEvent(BaseModel):
    type: Optional[GroupEventType] = None
    object: Optional[BaseModel] = None
    group_id: Optional[int] = None
    unprepared_ctx_api: Optional[Any] = None

    @property
    def ctx_api(self) -> Optional["ABCAPI"]:
        return getattr(self, "unprepared_ctx_api")


class Message(BaseGroupEvent):
    object: "objects.MessageObject"


class MessageNew(BaseGroupEvent):
    object: "objects.MessageNewObject"


class MessageAllow(BaseGroupEvent):
    object: "objects.MessageAllowObject"


class MessageTypingState(BaseGroupEvent):
    object: "objects.MessageTypingStateObject"


class MessageDeny(BaseGroupEvent):
    object: "objects.MessageDenyObject"


class MessageEvent(BaseGroupEvent):
    object: "objects.MessageEventObject"


class PhotoNew(BaseGroupEvent):
    object: "objects.PhotosPhoto"


class PhotoComment(BaseGroupEvent):
    object: "objects.PhotoCommentObject"


class PhotoCommentDelete(BaseGroupEvent):
    object: "objects.PhotoCommentDeleteObject"


class AudioNew(BaseGroupEvent):
    object: "objects.AudioNewObject"


class VideoNew(BaseGroupEvent):
    object: "objects.VideoNewObject"


class VideoComment(BaseGroupEvent):
    object: "objects.VideoCommentObject"


class VideoCommentDelete(BaseGroupEvent):
    object: "objects.VideoCommentDeleteObject"


class WallPostNew(BaseGroupEvent):
    object: "objects.WallPostNewObject"


class WallReply(BaseGroupEvent):
    object: "objects.WallReplyNewObject"


class WallReplyDelete(BaseGroupEvent):
    object: "objects.WallReplyDeleteObject"


class Like(BaseGroupEvent):
    object: "objects.LikeObject"


class BoardPost(BaseGroupEvent):
    object: "objects.BoardPostNewObject"


class BoardPostDelete(BaseGroupEvent):
    object: "objects.BoardPostDeleteObject"


class MarketOrder(BaseGroupEvent):
    object: "objects.MarketOrderObject"


class MarketComment(BaseGroupEvent):
    object: "objects.MarketCommentNewObject"


class MarketCommentDelete(BaseGroupEvent):
    object: "objects.MarketCommentDeleteObject"


class GroupLeave(BaseGroupEvent):
    object: "objects.GroupLeaveObject"


class GroupJoin(BaseGroupEvent):
    object: "objects.GroupJoinObject"


class UserBlock(BaseGroupEvent):
    object: "objects.UserBlockObject"


class UserUnblock(BaseGroupEvent):
    object: "objects.UserUnblockObject"


class PollVoteNew(BaseGroupEvent):
    object: "objects.PollVoteNewObject"


class GroupOfficersEdit(BaseGroupEvent):
    object: "objects.GroupOfficersEditObject"


class GroupChangeSettings(BaseGroupEvent):
    object: "objects.GroupChangeSettingsObject"


class GroupChangePhoto(BaseGroupEvent):
    object: "objects.GroupChangePhotoObject"


class VkPayTransaction(BaseGroupEvent):
    object: "objects.VkPayTransactionObject"


class AppPayload(BaseGroupEvent):
    object: "objects.AppPayloadObject"


class DonutSubscriptionCreate(BaseGroupEvent):
    object: "objects.DonutSubscriptionCreateObject"


class DonutSubscriptionProlonged(BaseGroupEvent):
    object: "objects.DonutSubscriptionProlongedObject"


class DonutSubscriptionExpired(BaseGroupEvent):
    object: "objects.DonutSubscriptionExpiredObject"


class DonutSubscriptionCancelled(BaseGroupEvent):
    object: "objects.DonutSubscriptionCancelledObject"


class DonutSubscriptionPriceChanged(BaseGroupEvent):
    object: "objects.DonutSubscriptionPriceChangedObject"


class DonutMoneyWithdraw(BaseGroupEvent):
    object: "objects.DonutMoneyWithdrawObject"


class DonutMoneyWithdrawError(BaseGroupEvent):
    object: "objects.DonutMoneyWithdrawErrorObject"


Message.update_forward_refs()
MessageNew.update_forward_refs()
MessageAllow.update_forward_refs()
MessageTypingState.update_forward_refs()
MessageDeny.update_forward_refs()
PhotoNew.update_forward_refs()
PhotoComment.update_forward_refs()
PhotoCommentDelete.update_forward_refs()
VideoComment.update_forward_refs()
VideoCommentDelete.update_forward_refs()
WallPostNew.update_forward_refs()
WallReply.update_forward_refs()
WallReplyDelete.update_forward_refs()
BoardPost.update_forward_refs()
BoardPostDelete.update_forward_refs()
MarketComment.update_forward_refs()
MarketCommentDelete.update_forward_refs()
GroupLeave.update_forward_refs()
GroupJoin.update_forward_refs()
UserBlock.update_forward_refs()
UserUnblock.update_forward_refs()
PollVoteNew.update_forward_refs()
GroupOfficersEdit.update_forward_refs()
GroupChangeSettings.update_forward_refs()
GroupChangePhoto.update_forward_refs()
VkPayTransaction.update_forward_refs()
AppPayload.update_forward_refs()
DonutSubscriptionCreate.update_forward_refs()
DonutSubscriptionProlonged.update_forward_refs()
DonutSubscriptionExpired.update_forward_refs()
DonutSubscriptionCancelled.update_forward_refs()
DonutSubscriptionPriceChanged.update_forward_refs()
DonutMoneyWithdraw.update_forward_refs()
DonutMoneyWithdrawError.update_forward_refs()

DEFAULT_EVENTS_BASE_GROUP = EventsBase(GroupEventType)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_NEW, MessageNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_REPLY, Message)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_EDIT, Message)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_ALLOW, MessageAllow)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.MESSAGE_TYPING_STATE, MessageTypingState
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_DENY, MessageDeny)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MESSAGE_EVENT, MessageEvent)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_NEW, PhotoNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_NEW, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_EDIT, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.PHOTO_COMMENT_RESTORE, PhotoComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.PHOTO_COMMENT_DELETE, PhotoCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.AUDIO_NEW, AudioNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_NEW, VideoNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_NEW, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_EDIT, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VIDEO_COMMENT_RESTORE, VideoComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.VIDEO_COMMENT_DELETE, VideoCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_POST_NEW, WallPostNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPOST, WallPostNew)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_NEW, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_EDIT, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_RESTORE, WallReply)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.WALL_REPLY_DELETE, WallReplyDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.LIKE_ADD, Like)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.LIKE_REMOVE, Like)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_NEW, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_EDIT, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_RESTORE, BoardPost)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_DELETE, BoardPostDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_ORDER_NEW, MarketOrder)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_ORDER_EDIT, MarketOrder)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.BOARD_POST_DELETE, BoardPostDelete)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_NEW, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_EDIT, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.MARKET_COMMENT_RESTORE, MarketComment)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.MARKET_COMMENT_DELETE, MarketCommentDelete
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_LEAVE, GroupLeave)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_JOIN, GroupJoin)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.USER_BLOCK, UserBlock)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.USER_UNBLOCK, UserUnblock)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.POLL_VOTE_NEW, PollVoteNew)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.GROUP_OFFICERS_EDIT, GroupOfficersEdit
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.GROUP_CHANGE_SETTINGS, GroupChangeSettings
)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.GROUP_CHANGE_PHOTO, GroupChangePhoto)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.VKPAY_TRANSACTION, VkPayTransaction)
DEFAULT_EVENTS_BASE_GROUP.register(GroupEventType.APP_PAYLOAD, AppPayload)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_CREATE, DonutSubscriptionCreate
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_PROLONGED, DonutSubscriptionProlonged
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_EXPIRED, DonutSubscriptionExpired
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_CANCELLED, DonutSubscriptionCancelled
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_SUBSCRIPTION_PRICE_CHANGED, DonutSubscriptionPriceChanged
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_MONEY_WITHDRAW, DonutMoneyWithdraw
)
DEFAULT_EVENTS_BASE_GROUP.register(
    GroupEventType.DONUT_MONEY_WITHDRAW_ERROR, DonutMoneyWithdrawError
)

__all__ = (
    "DEFAULT_EVENTS_BASE_GROUP",
    "BaseGroupEvent",
    "MessageNew",
    "Message",
    "MessageAllow",
    "MessageTypingState",
    "MessageDeny",
    "MessageEvent",
    "PhotoNew",
    "PhotoComment",
    "PhotoCommentDelete",
    "AudioNew",
    "VideoNew",
    "VideoComment",
    "VideoCommentDelete",
    "WallPostNew",
    "WallReply",
    "WallReplyDelete",
    "Like",
    "BoardPost",
    "BoardPostDelete",
    "MarketComment",
    "MarketCommentDelete",
    "GroupJoin",
    "GroupLeave",
    "UserBlock",
    "UserUnblock",
    "PollVoteNew",
    "GroupOfficersEdit",
    "GroupChangeSettings",
    "GroupChangePhoto",
    "VkPayTransaction",
    "AppPayload",
    "DonutSubscriptionCreate",
    "DonutSubscriptionProlonged",
    "DonutSubscriptionExpired",
    "DonutSubscriptionCancelled",
    "DonutSubscriptionPriceChanged",
    "DonutMoneyWithdraw",
    "DonutMoneyWithdrawError",
)

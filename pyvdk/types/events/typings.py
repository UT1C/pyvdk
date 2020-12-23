from . import events
from typing import Union


class GroupTypes:
    MessageNew = events.MessageNew
    MessageAllow = events.MessageAllow
    MessageReply = events.Message
    MessageEdit = events.Message
    MessageTypingState = events.MessageTypingState
    MessageDeny = events.MessageDeny
    MessageEvent = events.MessageEvent
    PhotoNew = events.PhotoNew
    PhotoComment = events.PhotoComment
    PhotoCommentDelete = events.PhotoCommentDelete
    AudioNew = events.AudioNew
    VideoNew = events.VideoNew
    VideoCommentNew = events.VideoComment
    VideoCommentEdit = events.VideoComment
    VideoCommentRestore = events.VideoComment
    VideoCommentDelete = events.VideoCommentDelete
    WallPostNew = events.WallPostNew
    WallRepost = events.WallPostNew
    WallReplyNew = events.WallReply
    WallReplyEdit = events.WallReply
    WallReplyRestore = events.WallReply
    WallReplyDelete = events.WallReplyDelete
    LikeAdd = events.Like
    LikeRemove = events.Like
    BoardPostNew = events.BoardPost
    BoardPostEdit = events.BoardPost
    BoardPostRestore = events.BoardPost
    BoardPostDelete = events.BoardPostDelete
    MarketCommentNew = events.MarketComment
    MarketCommentEdit = events.MarketComment
    MarketCommentRestore = events.MarketComment
    MarketCommentDelete = events.MarketCommentDelete
    GroupJoin = events.GroupJoin
    GroupLeave = events.GroupLeave
    UserBlock = events.UserBlock
    UserUnblock = events.UserUnblock
    PollVoteNew = events.PollVoteNew
    GroupOfficersEdit = events.GroupOfficersEdit
    GroupChangeSettings = events.GroupChangeSettings
    GroupChangePhoto = events.GroupChangePhoto
    VkPayTransaction = events.VkPayTransaction
    AppPayload = events.AppPayload
    DonutSubscriptionCreate = events.DonutSubscriptionCreate
    DonutSubscriptionProlonged = events.DonutSubscriptionProlonged
    DonutSubscriptionCancelled = events.DonutSubscriptionCancelled
    DonutSubscriptionExpired = events.DonutSubscriptionExpired
    DonutSubscriptionPriceChanged = events.DonutSubscriptionPriceChanged
    DonutMoneyWithdraw = events.DonutMoneyWithdraw
    DonutMoneyWithdrawError = events.DonutMoneyWithdrawError

    UnifiedTypes = Union[
        events.BaseGroupEvent,
        events.MessageNew,
        events.Message,
        events.MessageAllow,
        events.MessageTypingState,
        events.MessageDeny,
        events.MessageEvent,
        events.PhotoNew,
        events.PhotoComment,
        events.PhotoCommentDelete,
        events.AudioNew,
        events.VideoNew,
        events.VideoComment,
        events.VideoCommentDelete,
        events.WallPostNew,
        events.WallReply,
        events.WallReplyDelete,
        events.Like,
        events.BoardPost,
        events.BoardPostDelete,
        events.MarketComment,
        events.MarketCommentDelete,
        events.GroupJoin,
        events.GroupLeave,
        events.UserBlock,
        events.UserUnblock,
        events.PollVoteNew,
        events.GroupOfficersEdit,
        events.GroupChangeSettings,
        events.GroupChangePhoto,
        events.VkPayTransaction,
        events.AppPayload,
        events.DonutSubscriptionCreate,
        events.DonutSubscriptionProlonged,
        events.DonutSubscriptionCancelled,
        events.DonutSubscriptionExpired,
        events.DonutSubscriptionPriceChanged,
        events.DonutMoneyWithdraw,
        events.DonutMoneyWithdrawError,
    ]

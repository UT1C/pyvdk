from .abc import Model
from typing import Optional, List, Callable, Any, Union
import enum


class Message(Model):

    action: Optional["MessageAction"] = None
    admin_author_id: Optional[int] = None
    attachments: Optional[List["MessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    deleted: Optional[bool] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["ForeignMessage"]] = None
    geo: Optional[object] = None
    id: Optional[int] = None
    important: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_cropped: Optional[bool] = None
    keyboard: Optional[object] = None
    members_count: Optional[int] = None
    out: Optional[bool] = None
    payload: Optional[str] = None
    peer_id: Optional[int] = None
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional["ForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    pinned_at: Optional[int] = None

    @property
    def chat_id(self) -> int:
        return self.peer_id - 2_000_000_000


class ForeignMessage(Model):

    attachments: Optional[List["MessageAttachment"]] = None
    conversation_message_id: Optional[int] = None
    date: Optional[int] = None
    from_id: Optional[int] = None
    fwd_messages: Optional[List["ForeignMessage"]] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["ForeignMessage"] = None
    text: Optional[str] = None
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    payload: Optional[str] = None


class MessageAttachment(Model):
    """VK Object Messages/MessagesMessageAttachment"""

    audio: Optional[dict] = None
    poll: Optional[dict] = None
    audio_message: Optional[dict] = None
    doc: Optional[dict] = None
    gift: Optional[dict] = None
    graffiti: Optional[dict] = None
    link: Optional[dict] = None
    market: Optional[dict] = None
    market_market_album: Optional[dict] = None
    photo: Optional[dict] = None
    sticker: Optional[dict] = None
    story: Optional[dict] = None
    type: Optional["MessagesMessageAttachmentType"] = None
    video: Optional[dict] = None
    wall: Optional[dict] = None
    wall_reply: Optional[dict] = None


class MessagesMessageAttachmentType(enum.Enum):
    """ Attachment type """

    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    POLL = "poll"
    LINK = "link"
    MARKET = "market"
    MARKET_ALBUM = "market_album"
    GIFT = "gift"
    STICKER = "sticker"
    WALL = "wall"
    WALL_REPLY = "wall_reply"
    ARTICLE = "article"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"



class BaseGeo(Model):

    coordinates: Optional["BaseGeoCoordinates"] = None
    place: Optional["BasePlace"] = None
    showmap: Optional[int] = None
    type: Optional[str] = None


class BaseGeoCoordinates(Model):
    """VK Object Base/BaseGeoCoordinates"""

    latitude: Optional[float] = None
    longitude: Optional[float] = None


class BasePlace(Model):
    """VK Object Base/BasePlace"""

    address: Optional[str] = None
    checkins: Optional[int] = None
    city: Optional[str] = None
    country: Optional[str] = None
    created: Optional[int] = None
    icon: Optional[str] = None
    id: Optional[int] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    title: Optional[str] = None
    type: Optional[str] = None


class MessageAction(Model):

    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional["MessageActionPhoto"] = None
    text: Optional[str] = None
    type: Optional["MessageActionStatus"] = None


class MessageActionPhoto(Model):

    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None


class MessagesMessageActionStatus(enum.Enum):
    """ Action status """

    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"

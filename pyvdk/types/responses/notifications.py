from typing import Optional, List

from ..objects import (
    NotificationsNotificationItem,
    VideoVideo,
    UsersUser,
    PhotosPhoto,
    GroupsGroup,
    AppsApp,
    BaseBoolInt,
    NotificationsSendMessageItem,
)
from ..abc import Model


class GetResponse(Model):
    response: Optional["GetResponseModel"] = None


class MarkAsViewedResponse(Model):
    response: Optional["MarkAsViewedResponseModel"] = None


class SendMessageResponse(Model):
    response: Optional["SendMessageResponseModel"] = None


class GetResponseModel(Model):
    count: Optional[int] = None
    items: Optional[List["NotificationsNotificationItem"]] = None
    profiles: Optional[List["UsersUser"]] = None
    groups: Optional[List["GroupsGroup"]] = None
    last_viewed: Optional[int] = None
    photos: Optional[List["PhotosPhoto"]] = None
    videos: Optional[List["VideoVideo"]] = None
    apps: Optional[List["AppsApp"]] = None
    next_from: Optional[str] = None
    ttl: Optional[int] = None


MarkAsViewedResponseModel = Optional[BaseBoolInt]

SendMessageResponseModel = List[NotificationsSendMessageItem]

GetResponse.update_forward_refs()
MarkAsViewedResponse.update_forward_refs()
SendMessageResponse.update_forward_refs()

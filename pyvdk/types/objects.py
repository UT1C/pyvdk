# -*- coding: utf-8 -*-
#
import enum
from typing import Any, Dict, Optional, Union

from .abc import Model

class AccountAccountCounters(Model):
    app_requests: int
    events: int
    faves: int
    friends: int
    friends_suggestions: int
    friends_recommendations: int
    gifts: int
    groups: int
    menu_discover_badge: int
    messages: int
    memories: int
    notes: int
    notifications: int
    photos: int
    sdk: int


class AccountInfo(Model):
    wishlists_ae_promo_banner_show: "BaseBoolInt"
    twofa_required: "BaseBoolInt"
    country: str
    https_required: "BaseBoolInt"
    intro: "BaseBoolInt"
    show_vk_apps_intro: bool
    mini_apps_ads_slot_id: int
    qr_promotion: int
    link_redirects: Dict[Any, Any]
    lang: int
    no_wall_replies: "BaseBoolInt"
    own_posts_default: "BaseBoolInt"
    subscriptions: list


class AccountNameRequest(Model):
    first_name: str
    id: int
    last_name: str
    status: "AccountNameRequestStatus"
    lang: str
    link_href: str
    link_label: str


class AccountNameRequestStatus(enum.Enum):
    SUCCESS = "success"
    PROCESSING = "processing"
    DECLINED = "declined"
    WAS_ACCEPTED = "was_accepted"
    WAS_DECLINED = "was_declined"
    DECLINED_WITH_LINK = "declined_with_link"
    RESPONSE = "response"
    RESPONSE_WITH_LINK = "response_with_link"


class AccountOffer(Model):
    description: str
    id: int
    img: str
    instruction: str
    instruction_html: str
    price: int
    short_description: str
    tag: str
    title: str
    currency_amount: float
    link_id: int
    link_type: str


class AccountPushConversations(Model):
    count: int
    items: list


class AccountPushConversationsItem(Model):
    disabled_until: int
    peer_id: int
    sound: "BaseBoolInt"


class AccountPushParams(Model):
    msg: list
    chat: list
    like: list
    repost: list
    comment: list
    mention: list
    reply: list
    new_post: list
    wall_post: list
    wall_publish: list
    friend: list
    friend_found: list
    friend_accepted: list
    group_invite: list
    group_accepted: list
    birthday: list
    event_soon: list
    app_request: list
    sdk_open: list


class AccountPushParamsMode(enum.Enum):
    ON = "on"
    OFF = "off"
    NO_SOUND = "no_sound"
    NO_TEXT = "no_text"


class AccountPushParamsOnoff(enum.Enum):
    ON = "on"
    OFF = "off"


class AccountPushParamsSettings(enum.Enum):
    ON = "on"
    OFF = "off"
    FR_OF_FR = "fr_of_fr"


class AccountPushSettings(Model):
    disabled: "BaseBoolInt"
    disabled_until: int
    settings: "AccountPushParams"
    conversations: "AccountPushConversations"


class AccountUserSettings(Model):
    ...


class AccountUserSettingsInterest(Model):
    title: str
    value: str


class AccountUserSettingsInterests(Model):
    activities: "AccountUserSettingsInterest"
    interests: "AccountUserSettingsInterest"
    music: "AccountUserSettingsInterest"
    tv: "AccountUserSettingsInterest"
    movies: "AccountUserSettingsInterest"
    books: "AccountUserSettingsInterest"
    games: "AccountUserSettingsInterest"
    quotes: "AccountUserSettingsInterest"
    about: "AccountUserSettingsInterest"


class AddressesFields(enum.Enum):
    ID = "id"
    TITLE = "title"
    ADDRESS = "address"
    ADDITIONAL_ADDRESS = "additional_address"
    COUNTRY_ID = "country_id"
    CITY_ID = "city_id"
    METRO_STATION_ID = "metro_station_id"
    LATITUDE = "latitude"
    LONGITUDE = "longitude"
    DISTANCE = "distance"
    WORK_INFO_STATUS = "work_info_status"
    TIMETABLE = "timetable"
    PHONE = "phone"
    TIME_OFFSET = "time_offset"


class AdsAccessRole(enum.Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    REPORTS = "reports"


class AdsAccesses(Model):
    client_id: str
    role: "AdsAccessRole"


class AdsAccount(Model):
    access_role: "AdsAccessRole"
    account_id: int
    account_status: "BaseBoolInt"
    account_type: "AdsAccountType"
    account_name: str


class AdsAccountType(enum.Enum):
    GENERAL = "general"
    AGENCY = "agency"


class AdsAd(Model):
    ad_format: int
    ad_platform: Optional[Union[int, str]] = None
    all_limit: int
    approved: "AdsAdApproved"
    campaign_id: int
    category1_id: Optional[int] = None
    category2_id: Optional[int] = None
    cost_type: "AdsAdCostType"
    cpc: Optional[int] = None
    cpm: Optional[int] = None
    cpa: Optional[int] = None
    ocpm: Optional[int] = None
    autobidding_max_cost: Optional[int] = None
    disclaimer_medical: Optional["BaseBoolInt"] = None
    disclaimer_specialist: Optional["BaseBoolInt"] = None
    disclaimer_supplements: Optional["BaseBoolInt"] = None
    id: int
    impressions_limit: Optional[int] = None
    impressions_limited: Optional["BaseBoolInt"] = None
    name: str
    status: "AdsAdStatus"
    video: Optional["BaseBoolInt"] = None


class AdsAdApproved(enum.Enum):
    NOT_MODERATED = 0
    PENDING_MODERATION = 1
    APPROVED = 2
    REJECTED = 3


class AdsAdCostType(enum.Enum):
    PER_CLICKS = 0
    PER_IMPRESSIONS = 1
    PER_ACTIONS = 2
    PER_IMPRESSIONS_OPTIMIZED = 3


class AdsAdLayout(Model):
    ad_format: int
    campaign_id: int
    cost_type: "AdsAdCostType"
    description: str
    id: int
    image_src: str
    image_src_2x: Optional[str] = None
    link_domain: Optional[str] = None
    link_url: str
    preview_link: Optional[Union[int, str]] = None
    title: str
    video: Optional["BaseBoolInt"] = None


class AdsAdStatus(enum.Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaign(Model):
    all_limit: str
    day_limit: str
    id: int
    name: str
    start_time: int
    status: "AdsCampaignStatus"
    stop_time: int
    type: "AdsCampaignType"


class AdsCampaignStatus(enum.Enum):
    STOPPED = 0
    STARTED = 1
    DELETED = 2


class AdsCampaignType(enum.Enum):
    NORMAL = "normal"
    VK_APPS_MANAGED = "vk_apps_managed"
    MOBILE_APPS = "mobile_apps"
    PROMOTED_POSTS = "promoted_posts"


class AdsCategory(Model):
    id: int
    name: str
    subcategories: Optional[list] = None


class AdsClient(Model):
    all_limit: str
    day_limit: str
    id: int
    name: str


class AdsCriteria(Model):
    age_from: int
    age_to: int
    apps: str
    apps_not: str
    birthday: int
    cities: str
    cities_not: str
    country: int
    districts: str
    groups: str
    interest_categories: str
    interests: str
    paying: "BaseBoolInt"
    positions: str
    religions: str
    retargeting_groups: str
    retargeting_groups_not: str
    school_from: int
    school_to: int
    schools: str
    sex: "AdsCriteriaSex"
    stations: str
    statuses: str
    streets: str
    travellers: "BasePropertyExists"
    uni_from: int
    uni_to: int
    user_browsers: str
    user_devices: str
    user_os: str


class AdsCriteriaSex(enum.Enum):
    ANY = 0
    MALE = 1
    FEMALE = 2


class AdsDemoStats(Model):
    id: int
    stats: "AdsDemostatsFormat"
    type: "AdsObjectType"


class AdsDemostatsFormat(Model):
    age: list
    cities: list
    day: str
    month: str
    overall: int
    sex: list
    sex_age: list


class AdsFloodStats(Model):
    left: int
    refresh: int


class AdsLinkStatus(Model):
    description: str
    redirect_url: str
    status: str


class AdsLookalikeRequest(Model):
    id: int
    create_time: int
    update_time: int
    scheduled_delete_time: Optional[int] = None
    status: str
    source_type: str
    source_retargeting_group_id: Optional[int] = None
    source_name: Optional[str] = None
    audience_count: Optional[int] = None
    save_audience_levels: Optional[list] = None


class AdsLookalikeRequestSaveAudienceLevel(Model):
    level: int
    audience_count: int


class AdsMusician(Model):
    id: int
    name: str


class AdsObjectType(enum.Enum):
    AD = "ad"
    CAMPAIGN = "campaign"
    CLIENT = "client"
    OFFICE = "office"


class AdsParagraphs(Model):
    paragraph: str


class AdsPromotedPostReach(Model):
    hide: int
    id: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_total: int
    report: int
    to_group: int
    unsubscribe: int
    video_views_100p: Optional[int] = None
    video_views_25p: Optional[int] = None
    video_views_3s: Optional[int] = None
    video_views_50p: Optional[int] = None
    video_views_75p: Optional[int] = None
    video_views_start: Optional[int] = None


class AdsRejectReason(Model):
    comment: str
    rules: list


class AdsRules(Model):
    paragraphs: list
    title: str


class AdsStats(Model):
    id: int
    stats: "AdsStatsFormat"
    type: "AdsObjectType"
    views_times: "AdsStatsViewsTimes"


class AdsStatsAge(Model):
    clicks_rate: float
    impressions_rate: float
    value: str


class AdsStatsCities(Model):
    clicks_rate: float
    impressions_rate: float
    name: str
    value: int


class AdsStatsFormat(Model):
    clicks: int
    day: str
    impressions: int
    join_rate: int
    month: str
    overall: int
    reach: int
    spent: int
    video_clicks_site: int
    video_views: int
    video_views_full: int
    video_views_half: int


class AdsStatsSex(Model):
    clicks_rate: float
    impressions_rate: float
    value: "AdsStatsSexValue"


class AdsStatsSexAge(Model):
    clicks_rate: float
    impressions_rate: float
    value: str


class AdsStatsSexValue(enum.Enum):
    FEMALE = "f"
    MALE = "m"


class AdsStatsViewsTimes(Model):
    views_ads_times_1: int
    views_ads_times_2: int
    views_ads_times_3: int
    views_ads_times_4: int
    views_ads_times_5: str
    views_ads_times_6: int
    views_ads_times_7: int
    views_ads_times_8: int
    views_ads_times_9: int
    views_ads_times_10: int
    views_ads_times_11_plus: int


class AdsTargSettings(Model):
    ...


class AdsTargStats(Model):
    audience_count: int
    recommended_cpc: Optional[float] = None
    recommended_cpm: Optional[float] = None
    recommended_cpc_50: Optional[float] = None
    recommended_cpm_50: Optional[float] = None
    recommended_cpc_70: Optional[float] = None
    recommended_cpm_70: Optional[float] = None
    recommended_cpc_90: Optional[float] = None
    recommended_cpm_90: Optional[float] = None


class AdsTargSuggestions(Model):
    id: int
    name: str


class AdsTargSuggestionsCities(Model):
    id: int
    name: str
    parent: str


class AdsTargSuggestionsRegions(Model):
    id: int
    name: str
    type: str


class AdsTargSuggestionsSchools(Model):
    desc: str
    id: int
    name: str
    parent: str
    type: "AdsTargSuggestionsSchoolsType"


class AdsTargSuggestionsSchoolsType(enum.Enum):
    SCHOOL = "school"
    UNIVERSITY = "university"
    FACULTY = "faculty"
    CHAIR = "chair"


class AdsTargetGroup(Model):
    audience_count: int
    domain: str
    id: int
    lifetime: int
    name: str
    pixel: str


class AdsUsers(Model):
    accesses: list
    user_id: int


class AppsApp(Model):
    ...


class AppsAppLeaderboardType(enum.Enum):
    NOT_SUPPORTED = 0
    LEVELS = 1
    POINTS = 2


class AppsAppMin(Model):
    type: "AppsAppType"
    id: int
    title: str
    author_owner_id: Optional[int] = None
    is_installed: Optional[bool] = None
    icon_139: Optional[str] = None
    icon_150: Optional[str] = None
    icon_278: Optional[str] = None
    icon_576: Optional[str] = None
    background_loader_color: Optional[str] = None
    loader_icon: Optional[str] = None
    icon_75: Optional[str] = None


class AppsAppType(enum.Enum):
    APP = "app"
    GAME = "game"
    SITE = "site"
    STANDALONE = "standalone"
    VK_APP = "vk_app"
    COMMUNITY_APP = "community_app"
    HTML5_GAME = "html5_game"
    MINI_APP = "mini_app"


class AppsLeaderboard(Model):
    level: Optional[int] = None
    points: Optional[int] = None
    score: Optional[int] = None
    user_id: int


class AppsScope(Model):
    name: str
    title: Optional[str] = None


class AudioAudio(Model):
    artist: str
    id: int
    title: str
    url: Optional[str] = None
    duration: int
    date: Optional[int] = None
    album_id: Optional[int] = None
    genre_id: Optional[int] = None
    performer: Optional[str] = None


class BaseBoolInt(enum.Enum):
    NO = 0
    YES = 1


class BaseCity(Model):
    id: int
    title: str


class BaseCommentsInfo(Model):
    can_post: "BaseBoolInt"
    count: int
    groups_can_post: bool


class BaseCountry(Model):
    id: int
    title: str


class BaseCropPhoto(Model):
    photo: "PhotosPhoto"
    crop: "BaseCropPhotoCrop"
    rect: "BaseCropPhotoRect"


class BaseCropPhotoCrop(Model):
    x: float
    y: float
    x2: float
    y2: float


class BaseCropPhotoRect(Model):
    x: float
    y: float
    x2: float
    y2: float


class BaseError(Model):
    error_code: int
    error_msg: str
    error_text: str
    request_params: list


class BaseGeo(Model):
    coordinates: "BaseGeoCoordinates"
    place: "BasePlace"
    showmap: int
    type: str


class BaseGeoCoordinates(Model):
    latitude: float
    longitude: float


class BaseGradientPoint(Model):
    color: str
    position: float


class BaseImage(Model):
    id: Optional[str] = None
    height: int
    url: str
    width: int


class BaseLikes(Model):
    count: int
    user_likes: "BaseBoolInt"


class BaseLikesInfo(Model):
    can_like: "BaseBoolInt"
    can_publish: Optional["BaseBoolInt"] = None
    count: int
    user_likes: int


class BaseLink(Model):
    application: Optional["BaseLinkApplication"] = None
    button: Optional["BaseLinkButton"] = None
    caption: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    is_favorite: Optional[bool] = None
    photo: Optional["PhotosPhoto"] = None
    preview_page: Optional[str] = None
    preview_url: Optional[str] = None
    product: Optional["BaseLinkProduct"] = None
    rating: Optional["BaseLinkRating"] = None
    title: Optional[str] = None
    url: str
    target_object: Optional["LinkTargetObject"] = None
    is_external: Optional[bool] = None
    video: Optional["VideoVideo"] = None


class BaseLinkApplication(Model):
    app_id: float
    store: "BaseLinkApplicationStore"


class BaseLinkApplicationStore(Model):
    id: float
    name: str


class BaseLinkButton(Model):
    action: "BaseLinkButtonAction"
    title: str
    block_id: str
    section_id: str
    owner_id: int
    icon: str
    style: "BaseLinkButtonStyle"


class BaseLinkButtonAction(Model):
    type: "BaseLinkButtonActionType"
    url: str
    consume_reason: str


class BaseLinkButtonActionType(enum.Enum):
    OPEN_URL = "open_url"


class BaseLinkButtonStyle(Model):
    ...


class BaseLinkProduct(Model):
    price: "MarketPrice"
    merchant: Optional[str] = None
    orders_count: Optional[int] = None


class BaseLinkRating(Model):
    reviews_count: int
    stars: float


class BaseMessageError(Model):
    code: int
    description: str


class BaseObject(Model):
    id: int
    title: str


class BaseObjectCount(Model):
    count: int


class BaseObjectWithName(Model):
    id: int
    name: str


class BasePlace(Model):
    address: str
    checkins: int
    city: str
    country: str
    created: int
    icon: str
    id: int
    latitude: float
    longitude: float
    title: str
    type: str


class BasePropertyExists(enum.Enum):
    PROPERTY_EXISTS = 1


class BaseRepostsInfo(Model):
    count: int
    user_reposted: int


class BaseRequestParam(Model):
    key: str
    value: str


class BaseSex(enum.Enum):
    UNKNOWN = 0
    FEMALE = 1
    MALE = 2


class BaseSticker(Model):
    sticker_id: int
    product_id: int
    images: list
    images_with_background: list
    animation_url: str
    animations: list
    is_allowed: bool


class BaseStickerAnimation(Model):
    type: str
    url: str


class BaseUploadServer(Model):
    upload_url: str


class BaseUserGroupFields(enum.Enum):
    ABOUT = "about"
    ACTION_BUTTON = "action_button"
    ACTIVITIES = "activities"
    ACTIVITY = "activity"
    ADDRESSES = "addresses"
    ADMIN_LEVEL = "admin_level"
    AGE_LIMITS = "age_limits"
    AUTHOR_ID = "author_id"
    BAN_INFO = "ban_info"
    BDATE = "bdate"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    BOOKS = "books"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_MESSAGE = "can_message"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAREER = "career"
    CITY = "city"
    COMMON_COUNT = "common_count"
    CONNECTIONS = "connections"
    CONTACTS = "contacts"
    COUNTERS = "counters"
    COUNTRY = "country"
    COVER = "cover"
    CROP_PHOTO = "crop_photo"
    DEACTIVATED = "deactivated"
    DESCRIPTION = "description"
    DOMAIN = "domain"
    EDUCATION = "education"
    EXPORTS = "exports"
    FINISH_DATE = "finish_date"
    FIXED_POST = "fixed_post"
    FOLLOWERS_COUNT = "followers_count"
    FRIEND_STATUS = "friend_status"
    GAMES = "games"
    HAS_MARKET_APP = "has_market_app"
    HAS_MOBILE = "has_mobile"
    HAS_PHOTO = "has_photo"
    HOME_TOWN = "home_town"
    ID = "id"
    INTERESTS = "interests"
    IS_ADMIN = "is_admin"
    IS_CLOSED = "is_closed"
    IS_FAVORITE = "is_favorite"
    IS_FRIEND = "is_friend"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    IS_MEMBER = "is_member"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    IS_SUBSCRIBED = "is_subscribed"
    LAST_SEEN = "last_seen"
    LINKS = "links"
    LISTS = "lists"
    MAIDEN_NAME = "maiden_name"
    MAIN_ALBUM_ID = "main_album_id"
    MAIN_SECTION = "main_section"
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    MEMBERS_COUNT = "members_count"
    MILITARY = "military"
    MOVIES = "movies"
    MUSIC = "music"
    NAME = "name"
    NICKNAME = "nickname"
    OCCUPATION = "occupation"
    ONLINE = "online"
    ONLINE_STATUS = "online_status"
    PERSONAL = "personal"
    PHONE = "phone"
    PHOTO_100 = "photo_100"
    PHOTO_200 = "photo_200"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_50 = "photo_50"
    PHOTO_ID = "photo_id"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    QUOTES = "quotes"
    RELATION = "relation"
    RELATIVES = "relatives"
    SCHOOLS = "schools"
    SCREEN_NAME = "screen_name"
    SEX = "sex"
    SITE = "site"
    START_DATE = "start_date"
    STATUS = "status"
    TIMEZONE = "timezone"
    TRENDING = "trending"
    TV = "tv"
    TYPE = "type"
    UNIVERSITIES = "universities"
    VERIFIED = "verified"
    WALL_COMMENTS = "wall_comments"
    WIKI_PAGE = "wiki_page"
    VK_ADMIN_STATUS = "vk_admin_status"


class BaseUserId(Model):
    user_id: int


class BoardDefaultOrder(enum.Enum):
    DESC_UPDATED = 1
    DESC_CREATED = 2
    ASC_UPDATED = -1
    ASC_CREATED = -2


class BoardTopic(Model):
    comments: int
    created: int
    created_by: int
    id: int
    is_closed: "BaseBoolInt"
    is_fixed: "BaseBoolInt"
    title: str
    updated: int
    updated_by: int


class BoardTopicComment(Model):
    attachments: Optional[list] = None
    date: int
    from_id: int
    id: int
    real_offset: Optional[int] = None
    text: str
    can_edit: Optional["BaseBoolInt"] = None
    likes: Optional["BaseLikesInfo"] = None


class BoardTopicPoll(Model):
    answer_id: int
    answers: list
    created: int
    is_closed: Optional["BaseBoolInt"] = None
    owner_id: int
    poll_id: int
    question: str
    votes: str


class CallbackBoardPostDelete(Model):
    topic_owner_id: int
    topic_id: int
    id: int


class CallbackConfirmationMessage(Model):
    type: "CallbackMessageType"
    group_id: int
    secret: str


class CallbackGroupChangePhoto(Model):
    user_id: int
    photo: "PhotosPhoto"


class CallbackGroupChangeSettings(Model):
    user_id: int
    self: "BaseBoolInt"


class CallbackGroupJoin(Model):
    user_id: int
    join_type: "CallbackGroupJoinType"


class CallbackGroupJoinType(enum.Enum):
    JOIN = "join"
    UNSURE = "unsure"
    ACCEPTED = "accepted"
    APPROVED = "approved"
    REQUEST = "request"


class CallbackGroupLeave(Model):
    user_id: int
    self: "BaseBoolInt"


class CallbackGroupMarket(enum.Enum):
    DISABLED = 0
    OPEN = 1


class CallbackGroupOfficerRole(enum.Enum):
    NONE = 0
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class CallbackGroupOfficersEdit(Model):
    admin_id: int
    user_id: int
    level_old: "CallbackGroupOfficerRole"
    level_new: "CallbackGroupOfficerRole"


class CallbackGroupSettingsChanges(Model):
    title: str
    description: str
    access: "GroupsGroupIsClosed"
    screen_name: str
    public_category: int
    public_subcategory: int
    age_limits: "GroupsGroupFullAgeLimits"
    website: str
    enable_status_default: "GroupsGroupWall"
    enable_audio: "GroupsGroupAudio"
    enable_video: "GroupsGroupVideo"
    enable_photo: "GroupsGroupPhotos"
    enable_market: "CallbackGroupMarket"


class CallbackLikeAddRemove(Model):
    liker_id: int
    object_type: str
    object_owner_id: int
    object_id: int
    post_id: int
    thread_reply_id: Optional[int] = None


class CallbackMarketComment(Model):
    id: int
    from_id: int
    date: int
    text: Optional[str] = None
    market_owner_od: Optional[int] = None
    photo_id: Optional[int] = None


class CallbackMarketCommentDelete(Model):
    owner_id: int
    id: int
    user_id: int
    item_id: int


class CallbackMessageAllow(Model):
    user_id: int
    key: str


class CallbackMessageBase(Model):
    type: "CallbackMessageType"
    object: Dict[Any, Any]
    group_id: int


class CallbackMessageDeny(Model):
    user_id: int


class CallbackMessageType(enum.Enum):
    CONFIRMATION = "confirmation"
    GROUP_CHANGE_PHOTO = "group_change_photo"
    GROUP_CHANGE_SETTINGS = "group_change_settings"
    GROUP_OFFICERS_EDIT = "group_officers_edit"
    LEAD_FORMS_NEW = "lead_forms_new"
    MARKET_COMMENT_DELETE = "market_comment_delete"
    MARKET_COMMENT_EDIT = "market_comment_edit"
    MARKET_COMMENT_RESTORE = "market_comment_restore"
    MESSAGE_ALLOW = "message_allow"
    MESSAGE_DENY = "message_deny"
    MESSAGE_READ = "message_read"
    MESSAGE_REPLY = "message_reply"
    MESSAGE_TYPING_STATE = "message_typing_state"
    MESSAGES_EDIT = "messages_edit"
    PHOTO_COMMENT_DELETE = "photo_comment_delete"
    PHOTO_COMMENT_EDIT = "photo_comment_edit"
    PHOTO_COMMENT_RESTORE = "photo_comment_restore"
    POLL_VOTE_NEW = "poll_vote_new"
    USER_BLOCK = "user_block"
    USER_UNBLOCK = "user_unblock"
    VIDEO_COMMENT_DELETE = "video_comment_delete"
    VIDEO_COMMENT_EDIT = "video_comment_edit"
    VIDEO_COMMENT_RESTORE = "video_comment_restore"
    WALL_REPLY_DELETE = "wall_reply_delete"
    WALL_REPLY_RESTORE = "wall_reply_restore"
    WALL_REPOST = "wall_repost"


class CallbackPhotoComment(Model):
    id: int
    from_id: int
    date: int
    text: str
    photo_owner_od: int


class CallbackPhotoCommentDelete(Model):
    id: int
    owner_id: int
    user_id: int
    photo_id: int


class CallbackPollVoteNew(Model):
    owner_id: int
    poll_id: int
    option_id: int
    user_id: int


class CallbackQrScan(Model):
    user_id: int
    data: str
    type: str
    subtype: str
    reread: bool


class CallbackUserBlock(Model):
    admin_id: int
    user_id: int
    unblock_date: int
    reason: int
    comment: Optional[str] = None


class CallbackUserUnblock(Model):
    admin_id: int
    user_id: int
    by_end_date: int


class CallbackVideoComment(Model):
    id: int
    from_id: int
    date: int
    text: str
    video_owner_od: int


class CallbackVideoCommentDelete(Model):
    id: int
    owner_id: int
    user_id: int
    video_id: int


class CallbackWallCommentDelete(Model):
    owner_id: int
    id: int
    user_id: int
    post_id: int


class CommentThread(Model):
    can_post: Optional[bool] = None
    count: int
    groups_can_post: Optional[bool] = None
    items: Optional[list] = None
    show_reply_button: Optional[bool] = None


class DatabaseCity(Model):
    ...


class DatabaseFaculty(Model):
    id: int
    title: str


class DatabaseRegion(Model):
    id: int
    title: str


class DatabaseSchool(Model):
    id: int
    title: str


class DatabaseStation(Model):
    city_id: Optional[int] = None
    color: Optional[str] = None
    id: int
    name: str


class DatabaseUniversity(Model):
    id: int
    title: str


class DocsDoc(Model):
    id: int
    owner_id: int
    title: str
    size: int
    ext: str
    url: Optional[str] = None
    date: int
    type: int
    preview: Optional["DocsDocPreview"] = None
    is_licensed: Optional["BaseBoolInt"] = None
    access_key: Optional[str] = None
    tags: Optional[list] = None


class DocsDocAttachmentType(enum.Enum):
    DOC = "doc"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class DocsDocPreview(Model):
    audio_msg: "DocsDocPreviewAudioMsg"
    graffiti: "DocsDocPreviewGraffiti"
    photo: "DocsDocPreviewPhoto"
    video: "DocsDocPreviewVideo"


class DocsDocPreviewAudioMsg(Model):
    duration: int
    link_mp3: str
    link_ogg: str
    waveform: list


class DocsDocPreviewGraffiti(Model):
    src: str
    width: int
    height: int


class DocsDocPreviewPhoto(Model):
    sizes: list


class DocsDocPreviewPhotoSizes(Model):
    src: str
    width: int
    height: int
    type: "PhotosPhotoSizesType"


class DocsDocPreviewVideo(Model):
    src: str
    width: int
    height: int
    file_size: int


class DocsDocTypes(Model):
    id: int
    name: str
    count: int


class DocsDocUploadResponse(Model):
    file: str


class EventsEventAttach(Model):
    address: Optional[str] = None
    button_text: str
    friends: list
    id: int
    is_favorite: bool
    member_status: Optional["GroupsGroupFullMemberStatus"] = None
    text: str
    time: Optional[int] = None


class FaveBookmark(Model):
    added_date: int
    link: Optional["BaseLink"] = None
    post: Optional["WallWallpostFull"] = None
    product: Optional["MarketMarketItem"] = None
    seen: bool
    tags: list
    type: "FaveBookmarkType"
    video: Optional["VideoVideo"] = None


class FaveBookmarkType(enum.Enum):
    POST = "post"
    VIDEO = "video"
    PRODUCT = "product"
    ARTICLE = "article"
    LINK = "link"


class FavePage(Model):
    description: str
    group: Optional["GroupsGroupFull"] = None
    tags: list
    type: "FavePageType"
    updated_date: Optional[int] = None
    user: Optional["UsersUserFull"] = None


class FavePageType(enum.Enum):
    USER = "user"
    GROUP = "group"
    HINTS = "hints"


class FaveTag(Model):
    id: int
    name: str


class FriendsFriendExtendedStatus(Model):
    ...


class FriendsFriendStatus(Model):
    friend_status: "FriendsFriendStatusStatus"
    sign: Optional[str] = None
    user_id: int


class FriendsFriendStatusStatus(enum.Enum):
    NOT_A_FRIEND = 0
    OUTCOMING_REQUEST = 1
    INCOMING_REQUEST = 2
    IS_FRIEND = 3


class FriendsFriendsList(Model):
    id: int
    name: str


class FriendsMutualFriend(Model):
    common_count: int
    common_friends: list
    id: int


class FriendsRequests(Model):
    from_: str
    mutual: "FriendsRequestsMutual"
    user_id: int


class FriendsRequestsMutual(Model):
    count: int
    users: list


class FriendsRequestsXtrMessage(Model):
    from_: str
    message: str
    mutual: "FriendsRequestsMutual"
    user_id: int


class FriendsUserXtrLists(Model):
    ...


class FriendsUserXtrPhone(Model):
    ...


class GiftsGift(Model):
    date: int
    from_id: int
    gift: "GiftsLayout"
    gift_hash: str
    id: int
    message: str
    privacy: "GiftsGiftPrivacy"


class GiftsGiftPrivacy(enum.Enum):
    NAME_AND_MESSAGE_FOR_ALL = 0
    NAME_FOR_ALL = 1
    NAME_AND_MESSAGE_FOR_RECIPIENT_ONLY = 2


class GiftsLayout(Model):
    id: int
    thumb_512: str
    thumb_256: str
    thumb_48: str
    thumb_96: str
    stickers_product_id: int
    build_id: str
    keywords: str


class GroupsAddress(Model):
    additional_address: Optional[str] = None
    address: Optional[str] = None
    city_id: Optional[int] = None
    country_id: Optional[int] = None
    distance: Optional[int] = None
    id: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    metro_station_id: Optional[int] = None
    phone: Optional[str] = None
    time_offset: Optional[int] = None
    timetable: Optional["GroupsAddressTimetable"] = None
    title: Optional[str] = None
    work_info_status: Optional["GroupsAddressWorkInfoStatus"] = None


class GroupsAddressTimetable(Model):
    fri: "GroupsAddressTimetableDay"
    mon: "GroupsAddressTimetableDay"
    sat: "GroupsAddressTimetableDay"
    sun: "GroupsAddressTimetableDay"
    thu: "GroupsAddressTimetableDay"
    tue: "GroupsAddressTimetableDay"
    wed: "GroupsAddressTimetableDay"


class GroupsAddressTimetableDay(Model):
    break_close_time: Optional[int] = None
    break_open_time: Optional[int] = None
    close_time: int
    open_time: int


class GroupsAddressWorkInfoStatus(enum.Enum):
    NO_INFORMATION = "no_information"
    TEMPORARILY_CLOSED = "temporarily_closed"
    ALWAYS_OPENED = "always_opened"
    TIMETABLE = "timetable"
    FOREVER_CLOSED = "forever_closed"


class GroupsAddressesInfo(Model):
    is_enabled: bool
    main_address_id: Optional[int] = None


class GroupsBanInfo(Model):
    admin_id: int
    comment: str
    comment_visible: bool
    is_closed: bool
    date: int
    end_date: int
    reason: "GroupsBanInfoReason"


class GroupsBanInfoReason(enum.Enum):
    OTHER = 0
    SPAM = 1
    VERBAL_ABUSE = 2
    STRONG_LANGUAGE = 3
    FLOOD = 4


class GroupsBannedItem(Model):
    ...


class GroupsCallbackServer(Model):
    id: int
    title: str
    creator_id: int
    url: str
    secret_key: str
    status: str


class GroupsCallbackSettings(Model):
    api_version: str
    events: "GroupsLongPollEvents"


class GroupsContactsItem(Model):
    desc: str
    email: str
    phone: str
    user_id: int


class GroupsCountersGroup(Model):
    addresses: int
    albums: int
    audios: int
    audio_playlists: int
    docs: int
    market: int
    photos: int
    topics: int
    videos: int


class GroupsCover(Model):
    enabled: "BaseBoolInt"
    images: Optional[list] = None


class GroupsFields(enum.Enum):
    MARKET = "market"
    MEMBER_STATUS = "member_status"
    IS_FAVORITE = "is_favorite"
    IS_SUBSCRIBED = "is_subscribed"
    CITY = "city"
    COUNTRY = "country"
    VERIFIED = "verified"
    DESCRIPTION = "description"
    WIKI_PAGE = "wiki_page"
    MEMBERS_COUNT = "members_count"
    COUNTERS = "counters"
    COVER = "cover"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    ACTIVITY = "activity"
    FIXED_POST = "fixed_post"
    CAN_CREATE_TOPIC = "can_create_topic"
    CAN_UPLOAD_VIDEO = "can_upload_video"
    HAS_PHOTO = "has_photo"
    STATUS = "status"
    MAIN_ALBUM_ID = "main_album_id"
    LINKS = "links"
    CONTACTS = "contacts"
    SITE = "site"
    MAIN_SECTION = "main_section"
    TRENDING = "trending"
    CAN_MESSAGE = "can_message"
    IS_MARKET_CART_ENABLED = "is_market_cart_enabled"
    IS_MESSAGES_BLOCKED = "is_messages_blocked"
    CAN_SEND_NOTIFY = "can_send_notify"
    ONLINE_STATUS = "online_status"
    START_DATE = "start_date"
    FINISH_DATE = "finish_date"
    AGE_LIMITS = "age_limits"
    BAN_INFO = "ban_info"
    ACTION_BUTTON = "action_button"
    AUTHOR_ID = "author_id"
    PHONE = "phone"
    HAS_MARKET_APP = "has_market_app"
    ADDRESSES = "addresses"
    LIVE_COVERS = "live_covers"
    IS_ADULT = "is_adult"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    WARNING_NOTIFICATION = "warning_notification"
    MSG_PUSH_ALLOWED = "msg_push_allowed"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"


class GroupsFilter(enum.Enum):
    ADMIN = "admin"
    EDITOR = "editor"
    MODER = "moder"
    ADVERTISER = "advertiser"
    GROUPS = "groups"
    PUBLICS = "publics"
    EVENTS = "events"
    HAS_ADDRESSES = "has_addresses"


class GroupsGroup(Model):
    admin_level: "GroupsGroupAdminLevel"
    deactivated: str
    finish_date: int
    id: int
    is_admin: "BaseBoolInt"
    is_advertiser: "BaseBoolInt"
    is_closed: "GroupsGroupIsClosed"
    is_member: "BaseBoolInt"
    name: str
    photo_100: str
    photo_200: str
    photo_50: str
    screen_name: str
    start_date: int
    type: "GroupsGroupType"


class GroupsGroupAccess(enum.Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupAdminLevel(enum.Enum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupAgeLimits(enum.Enum):
    UNLIMITED = 1
    _16_PLUS = 2
    _18_PLUS = 3


class GroupsGroupAttach(Model):
    id: int
    text: str
    status: str
    size: int
    is_favorite: bool


class GroupsGroupAudio(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupBanInfo(Model):
    comment: str
    end_date: int
    reason: "GroupsBanInfoReason"


class GroupsGroupCategory(Model):
    id: int
    name: str
    subcategories: Optional[list] = None


class GroupsGroupCategoryFull(Model):
    id: int
    name: str
    page_count: int
    page_previews: list
    subcategories: Optional[list] = None


class GroupsGroupCategoryType(Model):
    id: int
    name: str


class GroupsGroupDocs(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupFull(Model):
    ...


class GroupsGroupFullAgeLimits(enum.Enum):
    NO = 1
    OVER_16 = 2
    OVER_18 = 3


class GroupsGroupFullMainSection(enum.Enum):
    ABSENT = 0
    PHOTOS = 1
    TOPICS = 2
    AUDIO = 3
    VIDEO = 4
    MARKET = 5


class GroupsGroupFullMemberStatus(enum.Enum):
    NOT_A_MEMBER = 0
    MEMBER = 1
    NOT_SURE = 2
    DECLINED = 3
    HAS_SENT_A_REQUEST = 4
    INVITED = 5


class GroupsGroupIsClosed(enum.Enum):
    OPEN = 0
    CLOSED = 1
    PRIVATE = 2


class GroupsGroupLink(Model):
    name: str
    desc: str
    edit_title: "BaseBoolInt"
    id: int
    image_processing: "BaseBoolInt"
    url: str


class GroupsGroupMarketCurrency(enum.Enum):
    RUSSIAN_RUBLES = 643
    UKRAINIAN_HRYVNIA = 980
    KAZAKH_TENGE = 398
    EURO = 978
    US_DOLLARS = 840


class GroupsGroupPhotos(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupPublicCategoryList(Model):
    id: int
    name: str
    subcategories: list


class GroupsGroupRole(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    ADVERTISER = "advertiser"


class GroupsGroupSubject(enum.Enum):
    AUTO = 1
    ACTIVITY_HOLIDAYS = 2
    BUSINESS = 3
    PETS = 4
    HEALTH = 5
    DATING_AND_COMMUNICATION = 6
    GAMES = 7
    IT = 8
    CINEMA = 9
    BEAUTY_AND_FASHION = 10
    COOKING = 11
    ART_AND_CULTURE = 12
    LITERATURE = 13
    MOBILE_SERVICES_AND_INTERNET = 14
    MUSIC = 15
    SCIENCE_AND_TECHNOLOGY = 16
    REAL_ESTATE = 17
    NEWS_AND_MEDIA = 18
    SECURITY = 19
    EDUCATION = 20
    HOME_AND_RENOVATIONS = 21
    POLITICS = 22
    FOOD = 23
    INDUSTRY = 24
    TRAVEL = 25
    WORK = 26
    ENTERTAINMENT = 27
    RELIGION = 28
    FAMILY = 29
    SPORTS = 30
    INSURANCE = 31
    TELEVISION = 32
    GOODS_AND_SERVICES = 33
    HOBBIES = 34
    FINANCE = 35
    PHOTO = 36
    ESOTERICS = 37
    ELECTRONICS_AND_APPLIANCES = 38
    EROTIC = 39
    HUMOR = 40
    SOCIETY_HUMANITIES = 41
    DESIGN_AND_GRAPHICS = 42


class GroupsGroupTopics(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupType(enum.Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupVideo(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupWall(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2
    CLOSED = 3


class GroupsGroupWiki(enum.Enum):
    DISABLED = 0
    OPEN = 1
    LIMITED = 2


class GroupsGroupXtrInvitedBy(Model):
    admin_level: "GroupsGroupXtrInvitedByAdminLevel"
    id: int
    invited_by: int
    is_admin: "BaseBoolInt"
    is_advertiser: "BaseBoolInt"
    is_closed: "BaseBoolInt"
    is_member: "BaseBoolInt"
    name: str
    photo_100: str
    photo_200: str
    photo_50: str
    screen_name: str
    type: "GroupsGroupXtrInvitedByType"


class GroupsGroupXtrInvitedByAdminLevel(enum.Enum):
    MODERATOR = 1
    EDITOR = 2
    ADMINISTRATOR = 3


class GroupsGroupXtrInvitedByType(enum.Enum):
    GROUP = "group"
    PAGE = "page"
    EVENT = "event"


class GroupsGroupsArray(Model):
    count: int
    items: list


class GroupsLinksItem(Model):
    desc: str
    edit_title: "BaseBoolInt"
    id: int
    name: str
    photo_100: str
    photo_50: str
    url: str


class GroupsLiveCovers(Model):
    is_enabled: bool
    is_scalable: Optional[bool] = None
    story_ids: Optional[list] = None


class GroupsLongPollEvents(Model):
    audio_new: "BaseBoolInt"
    board_post_delete: "BaseBoolInt"
    board_post_edit: "BaseBoolInt"
    board_post_new: "BaseBoolInt"
    board_post_restore: "BaseBoolInt"
    group_change_photo: "BaseBoolInt"
    group_change_settings: "BaseBoolInt"
    group_join: "BaseBoolInt"
    group_leave: "BaseBoolInt"
    group_officers_edit: "BaseBoolInt"
    lead_forms_new: Optional["BaseBoolInt"] = None
    market_comment_delete: "BaseBoolInt"
    market_comment_edit: "BaseBoolInt"
    market_comment_new: "BaseBoolInt"
    market_comment_restore: "BaseBoolInt"
    message_allow: "BaseBoolInt"
    message_deny: "BaseBoolInt"
    message_new: "BaseBoolInt"
    message_read: "BaseBoolInt"
    message_reply: "BaseBoolInt"
    message_typing_state: "BaseBoolInt"
    message_edit: "BaseBoolInt"
    photo_comment_delete: "BaseBoolInt"
    photo_comment_edit: "BaseBoolInt"
    photo_comment_new: "BaseBoolInt"
    photo_comment_restore: "BaseBoolInt"
    photo_new: "BaseBoolInt"
    poll_vote_new: "BaseBoolInt"
    user_block: "BaseBoolInt"
    user_unblock: "BaseBoolInt"
    video_comment_delete: "BaseBoolInt"
    video_comment_edit: "BaseBoolInt"
    video_comment_new: "BaseBoolInt"
    video_comment_restore: "BaseBoolInt"
    video_new: "BaseBoolInt"
    wall_post_new: "BaseBoolInt"
    wall_reply_delete: "BaseBoolInt"
    wall_reply_edit: "BaseBoolInt"
    wall_reply_new: "BaseBoolInt"
    wall_reply_restore: "BaseBoolInt"
    wall_repost: "BaseBoolInt"


class GroupsLongPollServer(Model):
    key: str
    server: str
    ts: str


class GroupsLongPollSettings(Model):
    api_version: Optional[str] = None
    events: "GroupsLongPollEvents"
    is_enabled: bool


class GroupsMarketInfo(Model):
    contact_id: int
    currency: "MarketCurrency"
    currency_text: str
    enabled: "BaseBoolInt"
    main_album_id: int
    price_max: str
    price_min: str


class GroupsMemberRole(Model):
    id: int
    permissions: list
    role: "GroupsMemberRoleStatus"


class GroupsMemberRolePermission(enum.Enum):
    ADS = "ads"


class GroupsMemberRoleStatus(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsMemberStatus(Model):
    member: "BaseBoolInt"
    user_id: int


class GroupsMemberStatusFull(Model):
    can_invite: Optional["BaseBoolInt"] = None
    can_recall: Optional["BaseBoolInt"] = None
    invitation: Optional["BaseBoolInt"] = None
    member: "BaseBoolInt"
    request: Optional["BaseBoolInt"] = None
    user_id: int


class GroupsOnlineStatus(Model):
    minutes: Optional[int] = None
    status: "GroupsOnlineStatusType"


class GroupsOnlineStatusType(enum.Enum):
    NONE = "none"
    ONLINE = "online"
    ANSWER_MARK = "answer_mark"


class GroupsOwnerXtrBanInfo(Model):
    ban_info: "GroupsBanInfo"
    group: "GroupsGroup"
    profile: "UsersUser"
    type: "GroupsOwnerXtrBanInfoType"


class GroupsOwnerXtrBanInfoType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"


class GroupsRoleOptions(enum.Enum):
    MODERATOR = "moderator"
    EDITOR = "editor"
    ADMINISTRATOR = "administrator"
    CREATOR = "creator"


class GroupsSettingsTwitter(Model):
    status: str
    name: Optional[str] = None


class GroupsSubjectItem(Model):
    id: int
    name: str


class GroupsTokenPermissionSetting(Model):
    name: str
    setting: int


class GroupsUserXtrRole(Model):
    ...


class LeadsChecked(Model):
    reason: str
    result: "LeadsCheckedResult"
    sid: str
    start_link: str


class LeadsCheckedResult(enum.Enum):
    TRUE = "true"
    FALSE = "false"


class LeadsComplete(Model):
    cost: int
    limit: int
    spent: int
    success: int
    test_mode: "BaseBoolInt"


class LeadsEntry(Model):
    aid: int
    comment: str
    date: int
    sid: str
    start_date: int
    status: int
    test_mode: "BaseBoolInt"
    uid: int


class LeadsLead(Model):
    completed: int
    cost: int
    days: "LeadsLeadDays"
    impressions: int
    limit: int
    spent: int
    started: int


class LeadsLeadDays(Model):
    completed: int
    impressions: int
    spent: int
    started: int


class LeadsStart(Model):
    test_mode: "BaseBoolInt"
    vk_sid: str


class LikesType(enum.Enum):
    POST = "post"
    COMMENT = "comment"
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    NOTE = "note"
    MARKET = "market"
    PHOTO_COMMENT = "photo_comment"
    VIDEO_COMMENT = "video_comment"
    TOPIC_COMMENT = "topic_comment"
    MARKET_COMMENT = "market_comment"
    SITEPAGE = "sitepage"


class LinkTargetObject(Model):
    type: str
    owner_id: int
    item_id: int


class MarketCurrency(Model):
    id: int
    name: str


class MarketMarketAlbum(Model):
    count: int
    id: int
    owner_id: int
    photo: Optional["PhotosPhoto"] = None
    title: str
    updated_time: int


class MarketMarketCategory(Model):
    id: int
    name: str
    section: "MarketSection"


class MarketMarketItem(Model):
    access_key: Optional[str] = None
    availability: "MarketMarketItemAvailability"
    button_title: Optional[str] = None
    category: "MarketMarketCategory"
    date: Optional[int] = None
    description: str
    external_id: Optional[str] = None
    id: int
    is_favorite: Optional[bool] = None
    owner_id: int
    price: "MarketPrice"
    thumb_photo: str
    title: str
    url: Optional[str] = None
    variants_grouping_id: Optional[int] = None
    is_main_variant: Optional[bool] = None


class MarketMarketItemAvailability(enum.Enum):
    AVAILABLE = 0
    REMOVED = 1
    UNAVAILABLE = 2


class MarketMarketItemFull(Model):
    ...


class MarketPrice(Model):
    amount: str
    currency: "MarketCurrency"
    discount_rate: int
    old_amount: str
    text: str


class MarketSection(Model):
    id: int
    name: str


class MediaRestriction(Model):
    text: Optional[str] = None
    title: str
    button: Optional["VideoRestrictionButton"] = None
    always_shown: Optional["BaseBoolInt"] = None
    blur: Optional["BaseBoolInt"] = None
    can_play: Optional["BaseBoolInt"] = None
    can_preview: Optional["BaseBoolInt"] = None
    card_icon: Optional[list] = None
    list_icon: Optional[list] = None


class MessageChatPreview(Model):
    admin_id: int
    joined: bool
    local_id: int
    members: list
    members_count: int
    title: str


class MessagesAudioMessage(Model):
    access_key: Optional[str] = None
    duration: int
    id: int
    link_mp3: str
    link_ogg: str
    owner_id: int
    waveform: list


class MessagesChat(Model):
    admin_id: int
    id: int
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: str
    users: list
    is_default_photo: Optional[bool] = None


class MessagesChatFull(Model):
    admin_id: int
    id: int
    kicked: Optional["BaseBoolInt"] = None
    left: Optional["BaseBoolInt"] = None
    photo_100: Optional[str] = None
    photo_200: Optional[str] = None
    photo_50: Optional[str] = None
    push_settings: Optional["MessagesChatPushSettings"] = None
    title: Optional[str] = None
    type: str
    users: list


class MessagesChatPushSettings(Model):
    disabled_until: int
    sound: "BaseBoolInt"


class MessagesChatRestrictions(Model):
    admins_promote_users: bool
    only_admins_edit_info: bool
    only_admins_edit_pin: bool
    only_admins_invite: bool
    only_admins_kick: bool


class MessagesConversation(Model):
    peer: "MessagesConversationPeer"
    last_message_id: int
    in_read: int
    out_read: int
    unread_count: Optional[int] = None
    is_marked_unread: Optional[bool] = None
    important: Optional[bool] = None
    unanswered: Optional[bool] = None
    special_service_type: Optional[str] = None
    message_request_data: Optional["MessagesMessageRequestData"] = None
    mentions: Optional[list] = None
    current_keyboard: Optional["MessagesKeyboard"] = None


class MessagesConversationMember(Model):
    can_kick: Optional[bool] = None
    invited_by: Optional[int] = None
    is_admin: Optional[bool] = None
    is_owner: Optional[bool] = None
    is_message_request: Optional[bool] = None
    join_date: Optional[int] = None
    request_date: Optional[int] = None
    member_id: int


class MessagesConversationPeer(Model):
    id: int
    local_id: Optional[int] = None
    type: "MessagesConversationPeerType"


class MessagesConversationPeerType(enum.Enum):
    CHAT = "chat"
    EMAIL = "email"
    USER = "user"
    GROUP = "group"


class MessagesConversationWithMessage(Model):
    conversation: "MessagesConversation"
    last_message: "MessagesMessage"


class MessagesForeignMessage(Model):
    attachments: Optional[list] = None
    conversation_message_id: Optional[int] = None
    date: int
    from_id: int
    fwd_messages: Optional[list] = None
    geo: Optional["BaseGeo"] = None
    id: Optional[int] = None
    peer_id: Optional[int] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: str
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    payload: Optional[str] = None


class MessagesGraffiti(Model):
    access_key: Optional[str] = None
    height: int
    id: int
    owner_id: int
    url: str
    width: int


class MessagesHistoryAttachment(Model):
    attachment: "MessagesHistoryMessageAttachment"
    message_id: int
    from_id: int


class MessagesHistoryMessageAttachment(Model):
    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["BaseLink"] = None
    photo: Optional["PhotosPhoto"] = None
    share: Optional["BaseLink"] = None
    type: "MessagesHistoryMessageAttachmentType"
    video: Optional["VideoVideo"] = None
    wall: Optional["BaseLink"] = None


class MessagesHistoryMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    AUDIO = "audio"
    DOC = "doc"
    LINK = "link"
    MARKET = "market"
    WALL = "wall"
    SHARE = "share"
    GRAFFITI = "graffiti"
    AUDIO_MESSAGE = "audio_message"


class MessagesKeyboard(Model):
    author_id: Optional[int] = None
    buttons: list
    one_time: bool
    inline: Optional[bool] = None


class MessagesKeyboardButton(Model):
    action: "MessagesKeyboardButtonAction"
    color: Optional[str] = None


class MessagesKeyboardButtonAction(Model):
    app_id: Optional[int] = None
    hash: Optional[str] = None
    label: Optional[str] = None
    link: Optional[str] = None
    owner_id: Optional[int] = None
    payload: Optional[str] = None
    type: "MessagesTemplateActionTypeNames"


class MessagesLastActivity(Model):
    online: "BaseBoolInt"
    time: int


class MessagesLongpollMessages(Model):
    count: int
    items: list


class MessagesLongpollParams(Model):
    key: str
    pts: int
    server: str
    ts: str


class MessagesMessage(Model):
    action: Optional["MessagesMessageAction"] = None
    admin_author_id: Optional[int] = None
    attachments: Optional[list] = None
    conversation_message_id: Optional[int] = None
    date: int
    deleted: Optional["BaseBoolInt"] = None
    from_id: int
    fwd_messages: Optional[list] = None
    geo: Optional["BaseGeo"] = None
    id: int
    important: Optional[bool] = None
    is_hidden: Optional[bool] = None
    is_cropped: Optional[bool] = None
    keyboard: Optional["MessagesKeyboard"] = None
    members_count: Optional[int] = None
    out: "BaseBoolInt"
    payload: Optional[str] = None
    peer_id: int
    random_id: Optional[int] = None
    ref: Optional[str] = None
    ref_source: Optional[str] = None
    reply_message: Optional["MessagesForeignMessage"] = None
    text: str
    update_time: Optional[int] = None
    was_listened: Optional[bool] = None
    pinned_at: Optional[int] = None


class MessagesMessageAction(Model):
    conversation_message_id: Optional[int] = None
    email: Optional[str] = None
    member_id: Optional[int] = None
    message: Optional[str] = None
    photo: Optional["MessagesMessageActionPhoto"] = None
    text: Optional[str] = None
    type: "MessagesMessageActionStatus"


class MessagesMessageActionPhoto(Model):
    photo_100: str
    photo_200: str
    photo_50: str


class MessagesMessageActionStatus(enum.Enum):
    CHAT_PHOTO_UPDATE = "chat_photo_update"
    CHAT_PHOTO_REMOVE = "chat_photo_remove"
    CHAT_CREATE = "chat_create"
    CHAT_TITLE_UPDATE = "chat_title_update"
    CHAT_INVITE_USER = "chat_invite_user"
    CHAT_KICK_USER = "chat_kick_user"
    CHAT_PIN_MESSAGE = "chat_pin_message"
    CHAT_UNPIN_MESSAGE = "chat_unpin_message"
    CHAT_INVITE_USER_BY_LINK = "chat_invite_user_by_link"


class MessagesMessageAttachment(Model):
    audio: Optional["AudioAudio"] = None
    audio_message: Optional["MessagesAudioMessage"] = None
    doc: Optional["DocsDoc"] = None
    gift: Optional["GiftsLayout"] = None
    graffiti: Optional["MessagesGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    story: Optional["StoriesStory"] = None
    type: "MessagesMessageAttachmentType"
    video: Optional["VideoVideo"] = None
    wall: Optional["WallWallpostFull"] = None
    wall_reply: Optional["WallWallComment"] = None


class MessagesMessageAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
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


class MessagesMessageRequestData(Model):
    status: str
    inviter_id: int
    request_date: int


class MessagesPinnedMessage(Model):
    attachments: Optional[list] = None
    conversation_message_id: Optional[int] = None
    date: int
    from_id: int
    fwd_messages: Optional[list] = None
    geo: Optional["BaseGeo"] = None
    id: int
    peer_id: int
    reply_message: Optional["MessagesForeignMessage"] = None
    text: str
    keyboard: Optional["MessagesKeyboard"] = None


class MessagesTemplateActionTypeNames(enum.Enum):
    TEXT = "text"
    START = "start"
    LOCATION = "location"
    VKPAY = "vkpay"
    OPEN_APP = "open_app"
    OPEN_PHOTO = "open_photo"
    OPEN_LINK = "open_link"


class MessagesUserXtrInvitedBy(Model):
    ...


class NewsfeedCommentsFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    VIDEO = "video"
    TOPIC = "topic"
    NOTE = "note"


class NewsfeedEventActivity(Model):
    address: Optional[str] = None
    button_text: str
    friends: list
    member_status: "GroupsGroupFullMemberStatus"
    text: str
    time: Optional[int] = None


class NewsfeedFilters(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    RECOMMENDED_GROUPS = "recommended_groups"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    AUDIO_PLAYLIST = "audio_playlist"
    CLIP = "clip"


class NewsfeedIgnoreItemType(enum.Enum):
    POST_ON_THE_WALL = "wall"
    TAG_ON_A_PHOTO = "tag"
    PROFILE_PHOTO = "profilephoto"
    VIDEO = "video"
    PHOTO = "photo"
    AUDIO = "audio"


class NewsfeedItemAudio(Model):
    ...


class NewsfeedItemAudioAudio(Model):
    count: int
    items: list


class NewsfeedItemBase(Model):
    type: "NewsfeedNewsfeedItemType"
    source_id: int
    date: int


class NewsfeedItemDigest(Model):
    ...


class NewsfeedItemFriend(Model):
    ...


class NewsfeedItemFriendFriends(Model):
    count: int
    items: list


class NewsfeedItemHolidayRecommendationsBlockHeader(Model):
    title: str
    subtitle: str
    image: list
    action: "BaseLinkButtonAction"


class NewsfeedItemNote(Model):
    ...


class NewsfeedItemNoteNotes(Model):
    count: int
    items: list


class NewsfeedItemPhoto(Model):
    ...


class NewsfeedItemPhotoPhotos(Model):
    count: int
    items: list


class NewsfeedItemPhotoTag(Model):
    ...


class NewsfeedItemPhotoTagPhotoTags(Model):
    count: int
    items: list


class NewsfeedItemPromoButton(Model):
    ...


class NewsfeedItemPromoButtonAction(Model):
    url: str
    type: str
    target: str


class NewsfeedItemPromoButtonImage(Model):
    width: int
    height: int
    url: str


class NewsfeedItemTopic(Model):
    ...


class NewsfeedItemVideo(Model):
    ...


class NewsfeedItemVideoVideo(Model):
    count: int
    items: list


class NewsfeedItemWallpost(Model):
    ...


class NewsfeedItemWallpostFeedback(Model):
    type: "NewsfeedItemWallpostFeedbackType"
    question: str
    answers: Optional[list] = None
    stars_count: Optional[int] = None
    gratitude: Optional[str] = None


class NewsfeedItemWallpostFeedbackAnswer(Model):
    title: str
    id: str


class NewsfeedItemWallpostFeedbackType(enum.Enum):
    BUTTONS = "buttons"
    STARS = "stars"


class NewsfeedItemWallpostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"


class NewsfeedList(Model):
    id: int
    title: str


class NewsfeedListFull(Model):
    ...


class NewsfeedNewsfeedItem(Model):
    ...


class NewsfeedNewsfeedItemType(enum.Enum):
    POST = "post"
    PHOTO = "photo"
    PHOTO_TAG = "photo_tag"
    WALL_PHOTO = "wall_photo"
    FRIEND = "friend"
    NOTE = "note"
    AUDIO = "audio"
    VIDEO = "video"
    TOPIC = "topic"
    DIGEST = "digest"
    STORIES = "stories"
    TAGS_SUGGESTIONS = "tags_suggestions"


class NewsfeedNewsfeedNote(Model):
    comments: int
    id: int
    owner_id: int
    title: str


class NewsfeedNewsfeedPhoto(Model):
    ...


class NotesNote(Model):
    read_comments: Optional[int] = None
    can_comment: Optional["BaseBoolInt"] = None
    comments: int
    date: int
    id: int
    owner_id: int
    text: Optional[str] = None
    text_wiki: Optional[str] = None
    title: str
    view_url: str


class NotesNoteComment(Model):
    date: int
    id: int
    message: str
    nid: int
    oid: int
    reply_to: Optional[int] = None
    uid: int


class NotificationsFeedback(Model):
    attachments: list
    from_id: int
    geo: "BaseGeo"
    id: int
    likes: "BaseLikesInfo"
    text: str
    to_id: int


class NotificationsNotification(Model):
    date: int
    feedback: "NotificationsFeedback"
    parent: "NotificationsNotificationParent"
    reply: "NotificationsReply"
    type: str


class NotificationsNotificationItem(Model):
    ...


class NotificationsNotificationParent(Model):
    ...


class NotificationsNotificationsComment(Model):
    date: int
    id: int
    owner_id: int
    photo: "PhotosPhoto"
    post: "WallWallpost"
    text: str
    topic: "BoardTopic"
    video: "VideoVideo"


class NotificationsReply(Model):
    date: int
    id: int
    text: int


class NotificationsSendMessageError(Model):
    code: int
    description: str


class NotificationsSendMessageItem(Model):
    user_id: int
    status: bool
    error: "NotificationsSendMessageError"


class OauthError(Model):
    error: str
    error_description: str
    redirect_uri: Optional[str] = None


class OrdersAmount(Model):
    amounts: list
    currency: str


class OrdersAmountItem(Model):
    amount: int
    description: str
    votes: str


class OrdersOrder(Model):
    amount: int
    app_order_id: int
    cancel_transaction_id: int
    date: int
    id: int
    item: str
    receiver_id: int
    status: str
    transaction_id: int
    user_id: int


class OrdersSubscription(Model):
    cancel_reason: Optional[str] = None
    create_time: int
    id: int
    item_id: str
    next_bill_time: Optional[int] = None
    pending_cancel: Optional[bool] = None
    period: int
    period_start_time: int
    price: int
    status: str
    test_mode: Optional[bool] = None
    trial_expire_time: Optional[int] = None
    update_time: int


class OwnerState(Model):
    state: int
    description: str


class PagesPrivacySettings(enum.Enum):
    COMMUNITY_MANAGERS_ONLY = 0
    COMMUNITY_MEMBERS_ONLY = 1
    EVERYONE = 2


class PagesWikipage(Model):
    creator_id: Optional[int] = None
    creator_name: Optional[int] = None
    editor_id: Optional[int] = None
    editor_name: Optional[str] = None
    group_id: int
    id: int
    title: str
    views: int
    who_can_edit: "PagesPrivacySettings"
    who_can_view: "PagesPrivacySettings"


class PagesWikipageFull(Model):
    created: int
    creator_id: Optional[int] = None
    current_user_can_edit: Optional["BaseBoolInt"] = None
    current_user_can_edit_access: Optional["BaseBoolInt"] = None
    edited: int
    editor_id: Optional[int] = None
    group_id: int
    html: Optional[str] = None
    id: int
    source: Optional[str] = None
    title: str
    view_url: str
    views: int
    who_can_edit: "PagesPrivacySettings"
    who_can_view: "PagesPrivacySettings"


class PagesWikipageHistory(Model):
    id: int
    length: int
    date: int
    editor_id: int
    editor_name: str


class PhotosCommentXtrPid(Model):
    attachments: Optional[list] = None
    date: int
    from_id: int
    id: int
    likes: Optional["BaseLikesInfo"] = None
    pid: int
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: str
    parents_stack: Optional[list] = None
    thread: Optional["CommentThread"] = None


class PhotosImage(Model):
    height: int
    type: "PhotosImageType"
    url: str
    width: int


class PhotosImageType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    L = "l"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    Y = "y"
    Z = "z"
    W = "w"


class PhotosMarketAlbumUploadResponse(Model):
    gid: int
    hash: str
    photo: str
    server: int


class PhotosMarketUploadResponse(Model):
    crop_data: str
    crop_hash: str
    group_id: int
    hash: str
    photo: str
    server: int


class PhotosMessageUploadResponse(Model):
    hash: str
    photo: str
    server: int


class PhotosOwnerUploadResponse(Model):
    hash: str
    photo: str
    server: int


class PhotosPhoto(Model):
    access_key: Optional[str] = None
    album_id: int
    date: int
    height: Optional[int] = None
    id: int
    images: Optional[list] = None
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: int
    photo_256: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    place: Optional[str] = None
    post_id: Optional[int] = None
    sizes: Optional[list] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None
    has_tags: bool
    restrictions: Optional["MediaRestriction"] = None


class PhotosPhotoAlbum(Model):
    created: int
    description: Optional[str] = None
    id: int
    owner_id: int
    size: int
    thumb: Optional["PhotosPhoto"] = None
    title: str
    updated: int


class PhotosPhotoAlbumFull(Model):
    can_upload: Optional["BaseBoolInt"] = None
    comments_disabled: Optional["BaseBoolInt"] = None
    created: int
    description: Optional[str] = None
    id: int
    owner_id: int
    size: int
    sizes: Optional[list] = None
    thumb_id: Optional[int] = None
    thumb_is_last: Optional["BaseBoolInt"] = None
    thumb_src: Optional[str] = None
    title: str
    updated: int
    upload_by_admins_only: Optional["BaseBoolInt"] = None


class PhotosPhotoFull(Model):
    access_key: Optional[str] = None
    album_id: int
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional["BaseObjectCount"] = None
    date: int
    height: Optional[int] = None
    id: int
    images: Optional[list] = None
    lat: Optional[float] = None
    likes: Optional["BaseLikes"] = None
    long: Optional[float] = None
    owner_id: int
    post_id: Optional[int] = None
    reposts: Optional["BaseObjectCount"] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoFullXtrRealOffset(Model):
    access_key: Optional[str] = None
    album_id: int
    can_comment: Optional["BaseBoolInt"] = None
    comments: Optional["BaseObjectCount"] = None
    date: int
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: int
    lat: Optional[float] = None
    likes: Optional["BaseLikes"] = None
    long: Optional[float] = None
    owner_id: int
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    reposts: Optional["BaseObjectCount"] = None
    sizes: Optional[list] = None
    tags: Optional["BaseObjectCount"] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoSizes(Model):
    height: int
    url: str
    src: Optional[str] = None
    type: "PhotosPhotoSizesType"
    width: int


class PhotosPhotoSizesType(enum.Enum):
    S = "s"
    M = "m"
    X = "x"
    O = "o"
    P = "p"
    Q = "q"
    R = "r"
    K = "k"
    L = "l"
    Y = "y"
    Z = "z"
    C = "c"
    W = "w"


class PhotosPhotoTag(Model):
    date: int
    id: int
    placer_id: int
    tagged_name: str
    user_id: int
    viewed: "BaseBoolInt"
    x: float
    x2: float
    y: float
    y2: float


class PhotosPhotoUpload(Model):
    album_id: int
    upload_url: str
    fallback_upload_url: Optional[str] = None
    user_id: int
    group_id: Optional[int] = None


class PhotosPhotoUploadResponse(Model):
    aid: int
    hash: str
    photos_list: str
    server: int


class PhotosPhotoXtrRealOffset(Model):
    access_key: Optional[str] = None
    album_id: int
    date: int
    height: Optional[int] = None
    hidden: Optional["BasePropertyExists"] = None
    id: int
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: int
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    post_id: Optional[int] = None
    real_offset: Optional[int] = None
    sizes: Optional[list] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosPhotoXtrTagInfo(Model):
    access_key: Optional[str] = None
    album_id: int
    date: int
    height: Optional[int] = None
    id: int
    lat: Optional[float] = None
    long: Optional[float] = None
    owner_id: int
    photo_1280: Optional[str] = None
    photo_130: Optional[str] = None
    photo_2560: Optional[str] = None
    photo_604: Optional[str] = None
    photo_75: Optional[str] = None
    photo_807: Optional[str] = None
    placer_id: Optional[int] = None
    post_id: Optional[int] = None
    sizes: Optional[list] = None
    tag_created: Optional[int] = None
    tag_id: Optional[int] = None
    text: Optional[str] = None
    user_id: Optional[int] = None
    width: Optional[int] = None


class PhotosTagsSuggestionItem(Model):
    title: str
    type: str
    buttons: list
    photo: "PhotosPhoto"
    tags: list


class PhotosTagsSuggestionItemButton(Model):
    title: str
    action: str
    style: str


class PhotosWallUploadResponse(Model):
    hash: str
    photo: str
    server: int


class PollsAnswer(Model):
    id: int
    rate: float
    text: str
    votes: int


class PollsBackground(Model):
    angle: int
    color: str
    height: int
    id: int
    name: str
    images: list
    points: list
    type: str
    width: int


class PollsFriend(Model):
    id: int


class PollsPoll(Model):
    anonymous: "PollsPollAnonymous"
    friends: Optional[list] = None
    multiple: bool
    answer_id: Optional[int] = None
    end_date: int
    answer_ids: Optional[list] = None
    closed: bool
    is_board: bool
    can_edit: bool
    can_vote: bool
    can_report: bool
    can_share: bool
    photo: Optional["PollsBackground"] = None
    answers: list
    created: int
    id: int
    owner_id: int
    author_id: Optional[int] = None
    question: str
    background: Optional["PollsBackground"] = None
    votes: int
    disable_unvote: bool


class PollsPollAnonymous(Model):
    ...


class PollsVoters(Model):
    answer_id: int
    users: "PollsVotersUsers"


class PollsVotersUsers(Model):
    count: int
    items: list


class PrettycardsPrettycard(Model):
    button: Optional[str] = None
    button_text: Optional[str] = None
    card_id: str
    images: Optional[list] = None
    link_url: str
    photo: str
    price: Optional[str] = None
    price_old: Optional[str] = None
    title: str


class SearchHint(Model):
    app: Optional["AppsApp"] = None
    description: str
    global_: Optional["BaseBoolInt"] = None
    group: Optional["GroupsGroup"] = None
    profile: Optional["UsersUserMin"] = None
    section: "SearchHintSection"
    type: "SearchHintType"


class SearchHintSection(enum.Enum):
    GROUPS = "groups"
    EVENTS = "events"
    PUBLICS = "publics"
    CORRESPONDENTS = "correspondents"
    PEOPLE = "people"
    FRIENDS = "friends"
    MUTUAL_FRIENDS = "mutual_friends"


class SearchHintType(enum.Enum):
    GROUP = "group"
    PROFILE = "profile"
    VK_APP = "vk_app"
    APP = "app"
    HTML5_GAME = "html5_game"


class SecureLevel(Model):
    level: int
    uid: int


class SecureSmsNotification(Model):
    app_id: str
    date: str
    id: str
    message: str
    user_id: str


class SecureTokenChecked(Model):
    date: int
    expire: int
    success: int
    user_id: int


class SecureTransaction(Model):
    date: int
    id: int
    uid_from: int
    uid_to: int
    votes: int


class StatsActivity(Model):
    comments: int
    copies: int
    hidden: int
    likes: int
    subscribed: int
    unsubscribed: int


class StatsCity(Model):
    count: int
    name: str
    value: int


class StatsCountry(Model):
    code: str
    count: int
    name: str
    value: int


class StatsPeriod(Model):
    activity: "StatsActivity"
    period_from: int
    period_to: int
    reach: "StatsReach"
    visitors: "StatsViews"


class StatsReach(Model):
    age: list
    cities: list
    countries: list
    mobile_reach: int
    reach: int
    reach_subscribers: int
    sex: list
    sex_age: list


class StatsSexAge(Model):
    count: Optional[int] = None
    value: str
    reach: Optional[int] = None
    reach_subscribers: Optional[int] = None
    count_subscribers: Optional[int] = None


class StatsViews(Model):
    age: list
    cities: list
    countries: list
    mobile_views: int
    sex: list
    sex_age: list
    views: int
    visitors: int


class StatsWallpostStat(Model):
    post_id: int
    hide: int
    join_group: int
    links: int
    reach_subscribers: int
    reach_subscribers_count: int
    reach_total: int
    reach_total_count: int
    reach_viral: int
    reach_ads: int
    report: int
    to_group: int
    unsubscribe: int
    sex_age: list


class StatusStatus(Model):
    text: str
    audio: Optional["AudioAudio"] = None


class StorageValue(Model):
    key: str
    value: str


class StoriesClickableArea(Model):
    x: int
    y: int


class StoriesClickableSticker(Model):
    clickable_area: list
    id: int
    hashtag: Optional[str] = None
    link_object: Optional["BaseLink"] = None
    mention: Optional[str] = None
    tooltip_text: Optional[str] = None
    owner_id: Optional[int] = None
    story_id: Optional[int] = None
    question: Optional[str] = None
    question_button: Optional[str] = None
    place_id: Optional[int] = None
    market_item: Optional["MarketMarketItem"] = None
    audio: Optional["AudioAudio"] = None
    audio_start_time: Optional[int] = None
    style: Optional[str] = None
    type: str
    subtype: Optional[str] = None
    post_owner_id: Optional[int] = None
    post_id: Optional[int] = None
    poll: Optional["PollsPoll"] = None
    color: Optional[str] = None
    sticker_id: Optional[int] = None
    sticker_pack_id: Optional[int] = None
    app: Optional["AppsAppMin"] = None
    app_context: Optional[str] = None
    has_new_interactions: Optional[bool] = None
    is_broadcast_notify_allowed: Optional[bool] = None


class StoriesClickableStickers(Model):
    clickable_stickers: list
    original_height: int
    original_width: int


class StoriesFeedItem(Model):
    type: str
    stories: Optional[list] = None
    grouped: Optional[list] = None
    app: Optional["AppsAppMin"] = None
    promo_data: Optional["StoriesPromoBlock"] = None


class StoriesPromoBlock(Model):
    name: str
    photo_50: str
    photo_100: str
    not_animated: bool


class StoriesReplies(Model):
    count: int
    new: Optional[int] = None


class StoriesStatLine(Model):
    name: str
    counter: Optional[int] = None
    is_unavailable: Optional[bool] = None


class StoriesStory(Model):
    access_key: Optional[str] = None
    can_comment: Optional["BaseBoolInt"] = None
    can_reply: Optional["BaseBoolInt"] = None
    can_see: Optional["BaseBoolInt"] = None
    can_like: Optional[bool] = None
    can_share: Optional["BaseBoolInt"] = None
    can_hide: Optional["BaseBoolInt"] = None
    date: Optional[int] = None
    expires_at: Optional[int] = None
    id: int
    is_deleted: Optional[bool] = None
    is_expired: Optional[bool] = None
    link: Optional["StoriesStoryLink"] = None
    owner_id: int
    parent_story: Optional["StoriesStory"] = None
    parent_story_access_key: Optional[str] = None
    parent_story_id: Optional[int] = None
    parent_story_owner_id: Optional[int] = None
    photo: Optional["PhotosPhoto"] = None
    replies: Optional["StoriesReplies"] = None
    seen: Optional["BaseBoolInt"] = None
    type: Optional["StoriesStoryType"] = None
    clickable_stickers: Optional["StoriesClickableStickers"] = None
    video: Optional["VideoVideo"] = None
    views: Optional[int] = None
    can_ask: Optional["BaseBoolInt"] = None
    can_ask_anonymous: Optional["BaseBoolInt"] = None
    narratives_count: Optional[int] = None
    first_narrative_title: Optional[str] = None
    birthday_wish_user_id: Optional[int] = None


class StoriesStoryLink(Model):
    text: str
    url: str


class StoriesStoryStats(Model):
    answer: "StoriesStoryStatsStat"
    bans: "StoriesStoryStatsStat"
    open_link: "StoriesStoryStatsStat"
    replies: "StoriesStoryStatsStat"
    shares: "StoriesStoryStatsStat"
    subscribers: "StoriesStoryStatsStat"
    views: "StoriesStoryStatsStat"
    likes: "StoriesStoryStatsStat"


class StoriesStoryStatsStat(Model):
    count: Optional[int] = None
    state: "StoriesStoryStatsState"


class StoriesStoryStatsState(enum.Enum):
    ON = "on"
    OFF = "off"
    HIDDEN = "hidden"


class StoriesStoryType(enum.Enum):
    PHOTO = "photo"
    VIDEO = "video"
    LIVE_ACTIVE = "live_active"
    LIVE_FINISHED = "live_finished"


class StoriesUploadLinkText(enum.Enum):
    TO_STORE = "to_store"
    VOTE = "vote"
    MORE = "more"
    BOOK = "book"
    ORDER = "order"
    ENROLL = "enroll"
    FILL = "fill"
    SIGNUP = "signup"
    BUY = "buy"
    TICKET = "ticket"
    WRITE = "write"
    OPEN = "open"
    LEARN_MORE = "learn_more"
    VIEW = "view"
    GO_TO = "go_to"
    CONTACT = "contact"
    WATCH = "watch"
    PLAY = "play"
    INSTALL = "install"
    READ = "read"
    CALENDAR = "calendar"


class StoriesViewersItem(Model):
    is_liked: bool
    user_id: int
    user: Optional["UsersUserFull"] = None


class UsersCareer(Model):
    city_id: int
    company: str
    country_id: int
    from_: int
    group_id: int
    id: int
    position: str
    until: int


class UsersExports(Model):
    facebook: int
    livejournal: int
    twitter: int


class UsersFields(enum.Enum):
    PHOTO_ID = "photo_id"
    VERIFIED = "verified"
    SEX = "sex"
    BDATE = "bdate"
    CITY = "city"
    COUNTRY = "country"
    HOME_TOWN = "home_town"
    HAS_PHOTO = "has_photo"
    PHOTO_50 = "photo_50"
    PHOTO_100 = "photo_100"
    PHOTO_200_ORIG = "photo_200_orig"
    PHOTO_200 = "photo_200"
    PHOTO_400_ORIG = "photo_400_orig"
    PHOTO_MAX = "photo_max"
    PHOTO_MAX_ORIG = "photo_max_orig"
    ONLINE = "online"
    LISTS = "lists"
    DOMAIN = "domain"
    HAS_MOBILE = "has_mobile"
    CONTACTS = "contacts"
    SITE = "site"
    EDUCATION = "education"
    UNIVERSITIES = "universities"
    SCHOOLS = "schools"
    STATUS = "status"
    LAST_SEEN = "last_seen"
    FOLLOWERS_COUNT = "followers_count"
    COUNTERS = "counters"
    COMMON_COUNT = "common_count"
    OCCUPATION = "occupation"
    NICKNAME = "nickname"
    RELATIVES = "relatives"
    RELATION = "relation"
    PERSONAL = "personal"
    CONNECTIONS = "connections"
    EXPORTS = "exports"
    WALL_COMMENTS = "wall_comments"
    ACTIVITIES = "activities"
    INTERESTS = "interests"
    MUSIC = "music"
    MOVIES = "movies"
    TV = "tv"
    BOOKS = "books"
    GAMES = "games"
    ABOUT = "about"
    QUOTES = "quotes"
    CAN_POST = "can_post"
    CAN_SEE_ALL_POSTS = "can_see_all_posts"
    CAN_SEE_AUDIO = "can_see_audio"
    CAN_WRITE_PRIVATE_MESSAGE = "can_write_private_message"
    CAN_SEND_FRIEND_REQUEST = "can_send_friend_request"
    IS_FAVORITE = "is_favorite"
    IS_HIDDEN_FROM_FEED = "is_hidden_from_feed"
    TIMEZONE = "timezone"
    SCREEN_NAME = "screen_name"
    MAIDEN_NAME = "maiden_name"
    CROP_PHOTO = "crop_photo"
    IS_FRIEND = "is_friend"
    FRIEND_STATUS = "friend_status"
    CAREER = "career"
    MILITARY = "military"
    BLACKLISTED = "blacklisted"
    BLACKLISTED_BY_ME = "blacklisted_by_me"
    CAN_SUBSCRIBE_POSTS = "can_subscribe_posts"
    DESCRIPTIONS = "descriptions"
    TRENDING = "trending"
    MUTUAL = "mutual"
    FRIENDSHIP_WEEKS = "friendship_weeks"
    CAN_INVITE_TO_CHATS = "can_invite_to_chats"
    STORIES_ARCHIVE_COUNT = "stories_archive_count"
    VIDEO_LIVE_LEVEL = "video_live_level"
    VIDEO_LIVE_COUNT = "video_live_count"
    CLIPS_COUNT = "clips_count"


class UsersLastSeen(Model):
    platform: int
    time: int


class UsersMilitary(Model):
    country_id: int
    from_: Optional[int] = None
    id: Optional[int] = None
    unit: str
    unit_id: int
    until: Optional[int] = None


class UsersOccupation(Model):
    id: int
    name: str
    type: str


class UsersOnlineInfo(Model):
    visible: bool
    last_seen: Optional[int] = None
    is_online: Optional[bool] = None
    app_id: Optional[int] = None
    is_mobile: Optional[bool] = None
    status: Optional[str] = None


class UsersPersonal(Model):
    alcohol: int
    inspired_by: str
    langs: list
    life_main: int
    people_main: int
    political: int
    religion: str
    religion_id: int
    smoking: int


class UsersRelative(Model):
    birth_date: Optional[str] = None
    id: Optional[int] = None
    name: Optional[str] = None
    type: str


class UsersSchool(Model):
    city: int
    class_: str
    country: int
    id: str
    name: str
    type: int
    type_str: str
    year_from: int
    year_graduated: int
    year_to: int


class UsersSubscriptionsItem(Model):
    ...


class UsersUniversity(Model):
    chair: int
    chair_name: str
    city: int
    country: int
    education_form: str
    education_status: str
    faculty: int
    faculty_name: str
    graduation: int
    id: int
    name: str


class UsersUser(Model):
    ...


class UsersUserConnections(Model):
    skype: str
    facebook: str
    facebook_name: Optional[str] = None
    twitter: str
    livejournal: Optional[str] = None
    instagram: str


class UsersUserCounters(Model):
    albums: int
    audios: int
    followers: int
    friends: int
    gifts: int
    groups: int
    notes: int
    online_friends: int
    pages: int
    photos: int
    subscriptions: int
    user_photos: int
    user_videos: int
    videos: int


class UsersUserFull(Model):
    ...


class UsersUserMin(Model):
    deactivated: Optional[str] = None
    first_name: str
    hidden: Optional[int] = None
    id: int
    last_name: str
    can_access_closed: Optional[bool] = None
    is_closed: Optional[bool] = None


class UsersUserRelation(enum.Enum):
    NOT_SPECIFIED = 0
    SINGLE = 1
    IN_A_RELATIONSHIP = 2
    ENGAGED = 3
    MARRIED = 4
    COMPLICATED = 5
    ACTIVELY_SEARCHING = 6
    IN_LOVE = 7
    IN_A_CIVIL_UNION = 8


class UsersUserSettingsXtr(Model):
    connections: Optional["UsersUserConnections"] = None
    bdate: Optional[str] = None
    bdate_visibility: Optional[int] = None
    city: Optional["BaseCity"] = None
    country: Optional["BaseCountry"] = None
    first_name: Optional[str] = None
    home_town: str
    last_name: Optional[str] = None
    maiden_name: Optional[str] = None
    name_request: Optional["AccountNameRequest"] = None
    personal: Optional["UsersPersonal"] = None
    phone: Optional[str] = None
    relation: Optional["UsersUserRelation"] = None
    relation_partner: Optional["UsersUserMin"] = None
    relation_pending: Optional["BaseBoolInt"] = None
    relation_requests: Optional[list] = None
    screen_name: Optional[str] = None
    sex: Optional["BaseSex"] = None
    status: str
    status_audio: Optional["AudioAudio"] = None
    interests: Optional["AccountUserSettingsInterests"] = None
    languages: Optional[list] = None


class UsersUserType(enum.Enum):
    PROFILE = "profile"


class UsersUserXtrCounters(Model):
    ...


class UsersUserXtrType(Model):
    ...


class UsersUsersArray(Model):
    count: int
    items: list


class UtilsDomainResolved(Model):
    object_id: int
    group_id: int
    type: "UtilsDomainResolvedType"


class UtilsDomainResolvedType(enum.Enum):
    USER = "user"
    GROUP = "group"
    APPLICATION = "application"
    PAGE = "page"


class UtilsLastShortenedLink(Model):
    access_key: str
    key: str
    short_url: str
    timestamp: int
    url: str
    views: int


class UtilsLinkChecked(Model):
    link: str
    status: "UtilsLinkCheckedStatus"


class UtilsLinkCheckedStatus(enum.Enum):
    NOT_BANNED = "not_banned"
    BANNED = "banned"
    PROCESSING = "processing"


class UtilsLinkStats(Model):
    key: str
    stats: list


class UtilsLinkStatsExtended(Model):
    key: str
    stats: list


class UtilsShortLink(Model):
    access_key: str
    key: str
    short_url: str
    url: str


class UtilsStats(Model):
    timestamp: int
    views: int


class UtilsStatsCity(Model):
    city_id: int
    views: int


class UtilsStatsCountry(Model):
    country_id: int
    views: int


class UtilsStatsExtended(Model):
    cities: list
    countries: list
    sex_age: list
    timestamp: int
    views: int


class UtilsStatsSexAge(Model):
    age_range: str
    female: int
    male: int


class VideoLiveSettings(Model):
    can_rewind: "BaseBoolInt"
    is_endless: "BaseBoolInt"
    max_duration: int


class VideoRestrictionButton(Model):
    action: str
    title: str


class VideoSaveResult(Model):
    access_key: str
    description: str
    owner_id: int
    title: str
    upload_url: str
    video_id: int


class VideoVideo(Model):
    ...


class VideoVideoAlbumFull(Model):
    count: int
    id: Optional[int] = None
    image: Optional[list] = None
    image_blur: Optional["BasePropertyExists"] = None
    is_system: Optional["BasePropertyExists"] = None
    owner_id: int
    title: str
    updated_time: int


class VideoVideoFiles(Model):
    external: str
    mp4_240: str
    mp4_360: str
    mp4_480: str
    mp4_720: str
    mp4_1080: str
    flv_320: str


class VideoVideoFull(Model):
    ...


class VideoVideoImage(Model):
    ...


class WallAppPost(Model):
    id: int
    name: str
    photo_130: str
    photo_604: str


class WallAttachedNote(Model):
    comments: int
    date: int
    id: int
    owner_id: int
    read_comments: int
    title: str
    view_url: str


class WallCarouselBase(Model):
    carousel_offset: int


class WallCommentAttachment(Model):
    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    sticker: Optional["BaseSticker"] = None
    type: "WallCommentAttachmentType"
    video: Optional["VideoVideo"] = None


class WallCommentAttachmentType(enum.Enum):
    PHOTO = "photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    NOTE = "note"
    PAGE = "page"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    STICKER = "sticker"


class WallGeo(Model):
    coordinates: str
    place: "BasePlace"
    showmap: int
    type: str


class WallGraffiti(Model):
    id: int
    owner_id: int
    photo_200: str
    photo_586: str


class WallPostCopyright(Model):
    id: Optional[int] = None
    link: str
    name: str
    type: str


class WallPostSource(Model):
    data: str
    platform: str
    type: "WallPostSourceType"
    url: str


class WallPostSourceType(enum.Enum):
    VK = "vk"
    WIDGET = "widget"
    API = "api"
    RSS = "rss"
    SMS = "sms"


class WallPostType(enum.Enum):
    POST = "post"
    COPY = "copy"
    REPLY = "reply"
    POSTPONE = "postpone"
    SUGGEST = "suggest"


class WallPostedPhoto(Model):
    id: int
    owner_id: int
    photo_130: str
    photo_604: str


class WallViews(Model):
    count: int


class WallWallComment(Model):
    attachments: Optional[list] = None
    date: int
    from_id: int
    id: int
    likes: Optional["BaseLikesInfo"] = None
    real_offset: Optional[int] = None
    reply_to_comment: Optional[int] = None
    reply_to_user: Optional[int] = None
    text: str
    thread: Optional["CommentThread"] = None
    post_id: Optional[int] = None
    owner_id: Optional[int] = None
    parents_stack: Optional[list] = None
    deleted: Optional[bool] = None


class WallWallpost(Model):
    access_key: str
    attachments: list
    copyright: "WallPostCopyright"
    date: int
    edited: int
    from_id: int
    geo: "WallGeo"
    id: int
    is_archived: bool
    is_favorite: bool
    likes: "BaseLikesInfo"
    owner_id: int
    post_source: "WallPostSource"
    post_type: "WallPostType"
    reposts: "BaseRepostsInfo"
    signer_id: int
    text: str
    views: "WallViews"


class WallWallpostAttachment(Model):
    access_key: Optional[str] = None
    album: Optional["PhotosPhotoAlbum"] = None
    app: Optional["WallAppPost"] = None
    audio: Optional["AudioAudio"] = None
    doc: Optional["DocsDoc"] = None
    event: Optional["EventsEventAttach"] = None
    group: Optional["GroupsGroupAttach"] = None
    graffiti: Optional["WallGraffiti"] = None
    link: Optional["BaseLink"] = None
    market: Optional["MarketMarketItem"] = None
    market_album: Optional["MarketMarketAlbum"] = None
    note: Optional["WallAttachedNote"] = None
    page: Optional["PagesWikipageFull"] = None
    photo: Optional["PhotosPhoto"] = None
    photos_list: Optional[list] = None
    poll: Optional["PollsPoll"] = None
    posted_photo: Optional["WallPostedPhoto"] = None
    type: "WallWallpostAttachmentType"
    video: Optional["VideoVideo"] = None


class WallWallpostAttachmentType(enum.Enum):
    PHOTO = "photo"
    POSTED_PHOTO = "posted_photo"
    AUDIO = "audio"
    VIDEO = "video"
    DOC = "doc"
    LINK = "link"
    GRAFFITI = "graffiti"
    NOTE = "note"
    APP = "app"
    POLL = "poll"
    PAGE = "page"
    ALBUM = "album"
    PHOTOS_LIST = "photos_list"
    MARKET_MARKET_ALBUM = "market_market_album"
    MARKET = "market"
    EVENT = "event"


class WallWallpostFull(Model):
    ...


class WallWallpostToId(Model):
    attachments: list
    comments: "BaseCommentsInfo"
    copy_owner_id: int
    copy_post_id: int
    date: int
    from_id: int
    geo: "WallGeo"
    id: int
    is_favorite: bool
    likes: "BaseLikesInfo"
    post_id: int
    post_source: "WallPostSource"
    post_type: "WallPostType"
    reposts: "BaseRepostsInfo"
    signer_id: int
    text: str
    to_id: int


class WidgetsCommentMedia(Model):
    item_id: int
    owner_id: int
    thumb_src: str
    type: "WidgetsCommentMediaType"


class WidgetsCommentMediaType(enum.Enum):
    AUDIO = "audio"
    PHOTO = "photo"
    VIDEO = "video"


class WidgetsCommentReplies(Model):
    can_post: "BaseBoolInt"
    count: int
    replies: list


class WidgetsCommentRepliesItem(Model):
    cid: int
    date: int
    likes: "WidgetsWidgetLikes"
    text: str
    uid: int
    user: "UsersUserFull"


class WidgetsWidgetComment(Model):
    attachments: Optional[list] = None
    can_delete: Optional["BaseBoolInt"] = None
    comments: Optional["WidgetsCommentReplies"] = None
    date: int
    from_id: int
    id: int
    likes: Optional["BaseLikesInfo"] = None
    media: Optional["WidgetsCommentMedia"] = None
    post_source: Optional["WallPostSource"] = None
    post_type: int
    reposts: Optional["BaseRepostsInfo"] = None
    text: str
    to_id: int
    user: Optional["UsersUserFull"] = None


class WidgetsWidgetLikes(Model):
    count: int


class WidgetsWidgetPage(Model):
    comments: "BaseObjectCount"
    date: int
    description: str
    id: int
    likes: "BaseObjectCount"
    page_id: str
    photo: str
    title: str
    url: str


[v.update_forward_refs() for v in globals().values() if hasattr(v, "update_forward_refs")]

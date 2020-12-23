from pydantic import BaseModel
from typing import Optional
from ...state import StatePeer


class BaseEventObject(BaseModel):
    state_peer: Optional[StatePeer] = None

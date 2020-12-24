from typing import Optional, List

from ..objects import PollsVoters, PollsPoll, BaseBoolInt
from ..abc import Model


class AddVoteResponse(Model):
    response: Optional["AddVoteResponseModel"] = None


class CreateResponse(Model):
    response: Optional["CreateResponseModel"] = None


class DeleteVoteResponse(Model):
    response: Optional["DeleteVoteResponseModel"] = None


class GetByIdResponse(Model):
    response: Optional["GetByIdResponseModel"] = None


class GetVotersResponse(Model):
    response: Optional["GetVotersResponseModel"] = None


AddVoteResponseModel = Optional[BaseBoolInt]

CreateResponseModel = Optional[PollsPoll]

DeleteVoteResponseModel = Optional[BaseBoolInt]

GetByIdResponseModel = Optional[PollsPoll]

GetVotersResponseModel = List[PollsVoters]

AddVoteResponse.update_forward_refs()
CreateResponse.update_forward_refs()
DeleteVoteResponse.update_forward_refs()
GetByIdResponse.update_forward_refs()
GetVotersResponse.update_forward_refs()

from pydantic import BaseModel


class Model(BaseModel):
    raw_data: dict

    class Config:
        arbitrary_types_allowed = True
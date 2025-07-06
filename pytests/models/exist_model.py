from pydantic import BaseModel


class ExistModel(BaseModel):
    exist: bool

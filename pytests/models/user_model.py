from pydantic import BaseModel
from typing import Optional


class UserInfoModel(BaseModel):
    id: int
    email: str
    name: str
    age: int


class UserModel(BaseModel):
    user: Optional[UserInfoModel] = None

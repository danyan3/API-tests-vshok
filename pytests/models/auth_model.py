from pydantic import BaseModel
from .user_model import UserInfoModel
from typing import Optional


class AuthModel(BaseModel):
    token: Optional[str] = None
    user: Optional[UserInfoModel] = None

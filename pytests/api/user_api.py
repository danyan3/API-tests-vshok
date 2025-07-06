from typing import Optional
from .base_api import BaseApi
from models import UserModel


class UserApi(BaseApi):
    def __init__(self, token: Optional[str] = None):
        super().__init__(token)

    def change_name(self, name: str) -> tuple[UserModel, int]:
        response = self.patch(
            url='/user/name/',
            json={
                'name': name
            }
        )

        return UserModel(**response.json()), response.status_code

    def get_user_info(self) -> tuple[UserModel, int]:
        response = self.get(
            url='/user/me/'
        )

        return UserModel(**response.json()), response.status_code

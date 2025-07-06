from typing import Optional
from .base_api import BaseApi
from models import AuthModel


class AuthApi(BaseApi):
    def __init__(self, token: Optional[str] = None):
        super().__init__(token)

    def login(self, email: str, password: str) -> tuple[AuthModel, int]:
        response = self.post(
            url='/auth/login/',
            json={
                'email': email,
                'password': password
            }
        )

        return AuthModel(**response.json()), response.status_code

    def register(self, email: str, password: str, age: int) -> tuple[AuthModel, int]:
        response = self.post(
            url='/auth/register/',
            json={
                'email': email,
                'password': password,
                'age': age
            }
        )

        return AuthModel(**response.json()), response.status_code

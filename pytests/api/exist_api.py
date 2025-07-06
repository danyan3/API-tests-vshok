from .base_api import BaseApi
from models import ExistModel


class ExistApi(BaseApi):
    def __init__(self):
        super().__init__()

    def check_user_exist(self, email: str) -> tuple[ExistModel, int]:
        response = self.post(
            url='/exist/',
            json={
                'email': email
            }
        )

        return ExistModel(**response.json()), response.status_code

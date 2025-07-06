import pytest
from api import AuthApi, UserApi, ExistApi
from utils import random_register_payload


@pytest.fixture(scope='module')
def auth_api():
    return AuthApi()


@pytest.fixture(scope='module')
def exist_api():
    return ExistApi()


@pytest.fixture(scope='function')
def user_api(user_payload):
    auth_api = AuthApi()
    response, _ = auth_api.register(**user_payload)

    return UserApi(token=response.token)


@pytest.fixture(scope='function')
def user_payload():
    payload = random_register_payload()

    return payload

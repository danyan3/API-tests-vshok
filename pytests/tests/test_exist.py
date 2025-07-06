import pytest
from packages import fake


@pytest.fixture
def registered_user(auth_api, user_payload):
    return auth_api.register(**user_payload)[0]


def test_user_exist(exist_api, registered_user):
    response_model, status_code = exist_api.check_user_exist(
        email=registered_user.user.email
    )

    assert status_code == 200
    assert response_model.exist == True


def test_user_not_exist(exist_api):
    response_model, status_code = exist_api.check_user_exist(
        email=fake.email()
    )

    assert status_code == 200
    assert response_model.exist == False

from utils import random_register_payload
import pytest


def test_user_can_register(auth_api, user_payload):
    response_model, status_code = auth_api.register(**user_payload)

    assert status_code == 200

    assert response_model.user.email == user_payload["email"]
    assert response_model.user.age == user_payload["age"]


def test_user_can_login(auth_api, user_payload):
    auth_api.register(**user_payload)

    response_model, status_code = auth_api.login(
        email=user_payload['email'],
        password=user_payload['password']
    )

    assert status_code == 200

    assert response_model.user.email == user_payload["email"]
    assert response_model.user.age == user_payload["age"]


def test_register_existing_email(auth_api, user_payload):
    auth_api.register(**user_payload)

    _, status_code = auth_api.register(**user_payload)

    assert status_code == 422


def test_register_with_invalid_email(auth_api, user_payload):
    user_payload['email'] = "email"

    _, status_code = auth_api.register(**user_payload)

    assert status_code == 422


def test_register_with_short_password(auth_api, user_payload):
    user_payload['password'] = "123"

    _, status_code = auth_api.register(**user_payload)

    assert status_code == 422


@pytest.mark.parametrize("field", ["email", "password", "age"])
def test_register_with_null_fields(auth_api, field, user_payload):
    user_payload[field] = None

    _, status_code = auth_api.register(**user_payload)

    assert status_code == 422


def test_login_with_wrong_password(auth_api, user_payload):
    auth_api.register(**user_payload)
    wrong_payload = dict(user_payload)
    wrong_payload['password'] = "wrong_password"

    _, status_code = auth_api.login(
        email=user_payload['email'],
        password=wrong_payload['password']
    )

    assert status_code == 422


def test_login_nonexistent_email(auth_api):
    _, status_code = auth_api.login(
        email="notfound@example.com",
        password="12345678"
    )

    assert status_code == 422


def test_login_missing_email(auth_api, user_payload):
    auth_api.register(**user_payload)

    _, status_code = auth_api.login(
        email=None,
        password=user_payload['password']
    )

    assert status_code == 422


def test_login_missing_password(auth_api, user_payload):
    auth_api.register(**user_payload)

    _, status_code = auth_api.login(
        email=user_payload['email'],
        password=None
    )

    assert status_code == 422

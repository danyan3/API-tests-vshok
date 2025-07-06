import pytest


@pytest.mark.parametrize("name", ["test", "test_name"])
def test_change_name_valid(user_api, name):
    response_model, status_code = user_api.change_name(
        name=name
    )

    assert status_code == 200
    assert response_model.user.name == name


@pytest.mark.parametrize("name", ["", "A"*100])
def test_change_name_invalid(user_api, name):
    _, status_code = user_api.change_name(
        name=name
    )

    assert status_code == 422


def test_get_user_info(user_api, user_payload):
    response_model, status_code = user_api.get_user_info()

    assert status_code == 200

    assert response_model.user.email == user_payload['email']
    assert response_model.user.age == user_payload['age']
    assert response_model.user.name == 'Neko'

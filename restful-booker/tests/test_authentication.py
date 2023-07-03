from json import dumps
import requests
from assertpy import assert_that


def test_can_get_auth_token():
    payload = dumps({
        "username": "admin",
        "password": "password123"
    })
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post('https://restful-booker.herokuapp.com/auth', data=payload, headers=headers)
    token = response.json()['token']

    assert_that(response.status_code).is_equal_to(200)
    assert_that(token).is_not_none()
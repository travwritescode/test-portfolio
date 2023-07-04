"""
Test the functionality of retrieving authentication tokens.
"""

from json import dumps
import requests
from assertpy import assert_that

from config import BASE_URI


def test_can_get_auth_token():
    """
    Test that an auth token can be retrieved for required functionality
    (PUT and DELETE enpoints)
    """
    payload = dumps({"username": "admin", "password": "password123"})
    headers = {"Content-Type": "application/json"}

    response = requests.post(f"{BASE_URI}/auth", data=payload, headers=headers, timeout=10000)
    token = response.json()["token"]

    assert_that(response.status_code).is_equal_to(200)
    assert_that(token).is_not_none()


"""
Test the functionality of retrieving authentication tokens.
"""

from json import dumps
import requests
from assertpy import assert_that

from restful_booker.config import BASE_URI


def test_can_get_auth_token(get_token):
    """
    Test that an auth token can be retrieved for required functionality
    (PUT and DELETE enpoints)
    """
    response, token = get_token
    assert_that(response.status_code).is_equal_to(200)
    assert_that(token).is_not_none()

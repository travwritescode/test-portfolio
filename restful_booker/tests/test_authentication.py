"""
Test the functionality of retrieving authentication tokens.
"""

from assertpy import assert_that

def test_can_get_auth_token(get_token):
    """
    Test that an auth token can be retrieved for required functionality
    (PUT and DELETE endpoints)
    """
    response, token = get_token
    assert_that(response.status_code).is_equal_to(200)
    assert_that(token).is_not_none()

"""
Test the functionality of the booking endpoints. 
Endpoints include:

"""
from assertpy import assert_that
import requests
from config import BASE_URI


def test_can_get_all_booking_ids():
    """
    Test that all booking ids may be retrieved
    """
    response = requests.get(f"{BASE_URI}/booking", timeout=10000)

    assert_that(response.status_code).is_equal_to(200)

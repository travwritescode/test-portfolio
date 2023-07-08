from assertpy import assert_that
import requests

from restful_booker.config import BASE_URI

def test_can_get_all_booking_ids():
    """
    Test that all booking ids may be retrieved
    """
    response = requests.get(f"{BASE_URI}/booking", timeout=10000)

    assert_that(response.status_code).is_equal_to(200)


def test_can_create_new_booking(create_new_booking):
    """
    Test the creating a new booking with a valid request body creates the new
    booking and returns information about the booing
    """
    assert_that(create_new_booking.status_code).is_equal_to(200)


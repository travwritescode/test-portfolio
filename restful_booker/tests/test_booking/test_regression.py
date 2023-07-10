import json
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


def test_can_update_booking(get_token, create_new_booking):
    """
    Can update an existing booking with valid request body
    """
    _, token = get_token
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={token}'
    }

    new_booking = create_new_booking.json()
    booking_id = new_booking['bookingid']
    updated_booking = new_booking['booking']
    updated_booking['depositpaid'] = False

    payload = json.dumps(updated_booking)

    response = requests.put(f'{BASE_URI}/booking/{booking_id}', data=payload, headers=headers, timeout=10000)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['depositpaid']).is_false()

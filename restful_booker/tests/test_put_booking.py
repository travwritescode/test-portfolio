import json
from assertpy import assert_that
import requests

from conftest import BASE_URI

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

    # Get response and update the 'depositpaid' field to False
    new_booking = create_new_booking.json()
    booking_id = new_booking['bookingid']
    updated_booking = new_booking['booking']
    updated_booking['depositpaid'] = False

    # Send PUT request to update booking info
    payload = json.dumps(updated_booking)
    response = requests.put(f'{BASE_URI}/booking/{booking_id}', data=payload, headers=headers, timeout=10000)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['depositpaid']).is_false()


def test_can_update_booking_with_partial_payload(get_token, create_new_booking):
    """
    Can update existing booking by sending a partial payload
    """
    _, token = get_token
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Cookie': f'token={token}'
    }

    # Create new booking and retrieve id
    new_booking = create_new_booking.json()
    booking_id = new_booking['bookingid']

    # Send partial payload to update first and last name
    payload = json.dumps({
        'firstname': 'Ethan',
        'lastname': 'Stanfield'
    })
    response = requests.patch(f'{BASE_URI}/booking/{booking_id}', data=payload, headers=headers, timeout=10000)

    assert_that(response.status_code).is_equal_to(200)
    assert_that(response.json()['firstname']).is_equal_to('Ethan')
    assert_that(response.json()['lastname']).is_equal_to('Stanfield')


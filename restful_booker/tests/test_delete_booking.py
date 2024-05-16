from assertpy import assert_that
import requests

from conftest import BASE_URI

def test_can_delete_booking(get_token, create_new_booking):
    """
    Can delete a booking by providing the booking ID
    """
    _, token = get_token
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={token}'
    }

    # Create new booking and retrieve id
    new_booking = create_new_booking.json()
    booking_id = new_booking['bookingid']

    # Delete booking and verify a 201 status which indicates successful deletion in this API
    response = requests.delete(f'{BASE_URI}/booking/{booking_id}', headers=headers, timeout=10000)

    assert_that(response.status_code).is_equal_to(201)
    
    # Verify the deleted booking cannot be found
    deleted_booking = requests.get(f'{BASE_URI}/booking/{booking_id}', timeout=10000)

    assert_that(deleted_booking.status_code).is_equal_to(404)

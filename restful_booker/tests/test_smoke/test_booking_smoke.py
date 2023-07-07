"""
Test the functionality of the booking endpoints. 
Endpoints include:

"""
from assertpy import assert_that
import requests

from restful_booker.config import BASE_URI


def test_can_get_booking_id_by_name(create_new_booking):
    """
    Test that requesting a booking id filtering by first and last name
    as query params returns just that booking id
    """
    new_booking_json = create_new_booking.json()
    booking_id = new_booking_json['bookingid']
    fname = new_booking_json['booking']['firstname']
    lname = new_booking_json['booking']['lastname']
    query = f'?firstname={fname}&lastname={lname}'
    response = requests.get(f'{BASE_URI}/booking{query}', timeout=10000)

    id_list = [id['bookingid'] for id in response.json()]

    assert_that(response.status_code).is_equal_to(200)
    assert_that(id_list).contains(booking_id)


def test_can_get_booking_id_by_checkin_date(create_new_booking):
    """
    According to documentation, passing query param of checkin date retrieves
    booking ids with date greater than or equal to date.
    Retrieving booking id with checkin date after query param date returns
    the expected booking id
    """
    new_booking_json = create_new_booking.json()
    print(new_booking_json)
    booking_id = new_booking_json['bookingid']
    query = '?checkin=2023-07-20'

    # In the absence of a datetime object as the checkin/checkout dates, I am hardcoding this
    # value as I won't be dynamically generating it nor can I modify it
    # See known issues as to shy I can't pass the checkin date from the response itself
    response = requests.get(f'{BASE_URI}/booking{query}', timeout=10000)
    id_list = [id['bookingid'] for id in response.json()]

    assert_that(response.status_code).is_equal_to(200)
    assert_that(id_list).contains(booking_id)

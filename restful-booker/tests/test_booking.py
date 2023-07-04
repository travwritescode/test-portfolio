"""
Test the functionality of the booking endpoints. 
Endpoints include:

"""
import json
from assertpy import assert_that
import requests
from config import BASE_URI


def test_can_get_all_booking_ids():
    """
    Test that all booking ids may be retrieved
    """
    response = requests.get(f"{BASE_URI}/booking", timeout=10000)

    assert_that(response.status_code).is_equal_to(200)


def test_can_get_booking_id_by_name():
    """
    Test that requesting a booking id filtering by first and last name
    as query params returns just that booking id
    """
    # TODO - Update test with user creation script as method
    query = '?firstname=Ethan&lastname=Stanfield'
    response = requests.get(f'{BASE_URI}/booking{query}', timeout=10000)

    assert_that(response.status_code).is_equal_to(200)
    # TODO - Update is equal to with dynamic value after creation script
    assert_that(response.json()[0]['bookingid']).is_equal_to(1128)

def test_can_get_booking_id_by_checkin_date():
    """
    According to documentation, passing query param of checkin date retrieves
    booking ids with date greater than or equal to date.
    Retrieving booking id with checkin date after query param date returns
    the expected booking id
    """

def test_can_create_new_booking():
    """
    Test the creating a new booking with a valid request body creates the new
    booking and returns information about the booing
    """
    payload = json.dumps({
        "firstname": "Ethan",
        "lastname": "Stanfield",
        "totalprice": 299,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-07-21",
            "checkout": "2023-07-23"
        },
        "additionalneeds": "Coffee"
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    # TODO - Extract firstname, lastname, checkin, and checkout dates from payload

    response = requests.post(f'{BASE_URI}/booking', headers=headers, data=payload, timeout=10000)
    # TODO - Extract bookingid from response object, assert status code


"""
Known issues:
- Retrieving booking id with checkin date query param equal to expected checkin
    date returns no results
    This does not meet acceptance criteria defined in documentation
- Retrieving booking id with checkout date query param less than expected checkout
    date returns no results (returns ids of checkout date less than or equal to)
    This does not meet acceptance criteria defined in documentation
"""
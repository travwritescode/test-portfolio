import json
from uuid import uuid4
import pytest
import requests

from restful_booker.config import BASE_URI


pytest.fixture
def create_new_booking():
    """
    Creates a new booking and returns the response object
    """
    lname = f'User {uuid4()}'

    payload = json.dumps({
        "firstname": "New",
        "lastname": lname,
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

    response = requests.post(f'{BASE_URI}/booking', headers=headers, data=payload, timeout=10000)

    return response

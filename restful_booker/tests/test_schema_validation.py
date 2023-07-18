from cerberus import Validator
import pytest
from assertpy import assert_that

@pytest.fixture
def validator():
    v = Validator()
    return v

def test_auth(validator, get_token):
    schema = {'token': {'type': 'string'}}
    response, _ = get_token

    assert_that(validator.validate(response.json(), schema)).is_true()
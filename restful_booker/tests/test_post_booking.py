from assertpy import assert_that

def test_can_create_new_booking(create_new_booking):
    """
    Test the creating a new booking with a valid request body creates the new
    booking and returns information about the booking
    """

    # This just tests that the output of the fixture is a 200 status code since
    # I am using the fixture in every other test
    assert_that(create_new_booking.status_code).is_equal_to(200)


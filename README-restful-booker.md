# API Tests
## Restful Booker API
### Regression Tests
1. Get Auth Token
    - Test that the user can log in to the app and retrieve a valid auth token
2. Get Booking IDs
    - Test that all booking IDs in the database can be retrieved
3. Get Booking ID
    - Test that user can get details of a single booking ID
4. Create Booking
    - Test that the user can create a booking by passing valid request body
5. Update Booking
    - Test that the user can update an existing booking by passing a valid request body
    - Requires valid token
6. Partial Update Booking
    - Test that the user can update a booking by passing a partial JSON payload
    - Requires valid token
7. Delete Booking
    - Test that the user can delete a booking
    - Requires valid token
8. Health check
    - Validates that the API is up and running
    - Fixture for performing the test suite. If not up and running, do not run all tests

### Smoke Tests
1. Get Booking ID by Full Name
    - Teststhat user can pass full name as query params to retrieve booking ID that matches the name
2. Get Booking ID by First Name
    - Test that user can pass first name as query param to retrieve booking ID that matches the name
3. Get Booking ID by Last Name
    - Test that user can pass last name as query param to retrieve booking ID that matches the name
4. Get Booking ID by Checkin and Checkout Date
    - Test that the user can pass the checkin and checkout date as query params to retrieve booking IDs that match both
5. Get Booking ID by Checkin Date
    - Test that the user can pass the checkin date as a query param to retrieve booking IDs with checkin date equal to or later than
6. Get Booking ID by Checkout Date
    - Test that the user can pass the checkin date as a query param to retrieve booking IDs with checkin date equal to or earlier than


Known issues:
- Retrieving booking id with checkin date query param equal to expected checkin
    date returns no results
    This does not meet acceptance criteria defined in documentation
- Retrieving booking id with checkout date query param less than expected checkout
    date returns no results (returns ids of checkout date less than or equal to)
    This does not meet acceptance criteria defined in documentation
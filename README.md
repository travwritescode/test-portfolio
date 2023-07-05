# test-portfolio
A portfolio of all of my practice testing solutions

Known issues:
- Retrieving booking id with checkin date query param equal to expected checkin
    date returns no results
    This does not meet acceptance criteria defined in documentation
- Retrieving booking id with checkout date query param less than expected checkout
    date returns no results (returns ids of checkout date less than or equal to)
    This does not meet acceptance criteria defined in documentation
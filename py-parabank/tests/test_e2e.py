import time
import pytest
from pages.accounts.accounts_overview_page import AccountsOverviewPage
from pages.accounts.account_details_page import AccountDetailsPage


@pytest.mark.usefixtures('clean_database', 'login_user')
def test_log_in_and_check_account_details(driver):
    # Open accounts overview and ensure the page shows the user's account
    accounts_overview_page = AccountsOverviewPage(driver)
    accounts_overview_page.open_overview_page()

    assert accounts_overview_page.shows_starter_account()

    # Open account details and ensure all info looks correct
    accounts_overview_page.open_details_page('13344')
    account_details_page = AccountDetailsPage(driver)

    # Pages flicker on load, need to write helper function to handle retrying
    # Sleep is a temporary solution
    time.sleep(.5)
    assert account_details_page.account_number_matches('13344')
    assert account_details_page.account_type_matches('CHECKING')
    assert account_details_page.account_balance_matches('$5022.93')
    assert account_details_page.available_balance_matches('$5022.93')

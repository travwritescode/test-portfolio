import pytest
import pages.accounts.accounts_overview as accounts_overview

@pytest.mark.usefixtures('clean_database', 'login_user')
def test_does_account_overview_look_good(driver):
    overview = accounts_overview.AccountsOverviewPage(driver)
    overview.open_accounts_overview_page()

    assert overview.does_overview_show_starter_account()
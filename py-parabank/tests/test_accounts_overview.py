import pytest
import pages.accounts.accounts_overview_page as accounts_overview_page

@pytest.mark.usefixtures('clean_database', 'login_user')
def test_does_account_overview_look_accurate(driver):
    overview = accounts_overview_page.AccountsOverviewPage(driver)
    overview.open_accounts_overview_page()

    assert overview.does_overview_show_starter_account()
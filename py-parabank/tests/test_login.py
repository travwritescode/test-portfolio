import pytest
from pages.login_page import LoginPage, LoginResultPage

@pytest.mark.usefixtures('clean_database')
def test_login_as_existing_user(driver):
    login_page = LoginPage(driver)
    assert login_page.is_title_matches()
    login_page.login("john", "demo")

    login_results_page = LoginResultPage(driver)
    assert login_results_page.is_user_logged_in()

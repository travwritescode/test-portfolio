import pages.login as login

def test_login_as_existing_user(driver):
    login_page = login.LoginPage(driver)
    assert login_page.is_title_matches()
    login_page.login("john", "demo")

    login_results_page = login.LoginResultPage(driver)
    assert login_results_page.is_user_logged_in()

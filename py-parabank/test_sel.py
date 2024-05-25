import page

def test_selenium_is_working(driver):
    login_page = page.LoginPage(driver)
    assert login_page.is_title_matches
    login_page.login("john", "demo")

    login_results_page = page.LoginResultPage(driver)
    assert login_results_page.is_error_encountered

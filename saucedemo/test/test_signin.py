from src.pages.signin_page import SignInpage

def test_standard_user_can_sign_in(browser):
    sign_in_page = SignInpage(browser)

    sign_in_page.login('standard_user', 'secret_sauce')
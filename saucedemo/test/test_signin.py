from src.pages.signin_page import SignInpage

#Add test_ prefix to run test again
def standard_user_can_sign_in(browser):
    sign_in_page = SignInpage(browser)

    sign_in_page.login('standard_user', 'secret_sauce')
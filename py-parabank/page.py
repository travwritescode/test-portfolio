from locators import LoginPageLocators, LoginResultPageLocators

class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver

class LoginPage(BasePage):
    """Home page action methods come here."""

    def is_title_matches(self):
        """Verifies that the hardcoded text "ParaBank" appears in page title"""

        return "ParaBank" in self.driver.title
    
    def login(self, username, password):
        """Triggers login"""
        username_field = self.driver.find_element(*LoginPageLocators.USERNAME)
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)
        login = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        login.click()

class LoginResultPage(BasePage):
    def is_error_encountered(self):
        error = self.driver.find_element(*LoginResultPageLocators.ERROR_MESSAGE)
        return "An internal error has occurred and has been logged" in error.text

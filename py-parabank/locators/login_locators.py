from selenium.webdriver.common.by import By

class LoginPageLocators(object):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//input[@value='Log In']")

class LoginResultPageLocators(object):
    GREETING = (By.CLASS_NAME, "smallText")
    ERROR_MESSAGE = (By.CLASS_NAME, "error")
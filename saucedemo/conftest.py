import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def browser():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.add_argument("--headless=new")
    chromeOptions.add_argument("--log-level=3")
    browser = webdriver.Chrome(options=chromeOptions)

    browser.get("https://automationintesting.online/")

    yield browser
import pytest
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.headless = False
    chromeOptions.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chromeOptions)

    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    yield driver

    driver.close()
import pytest
from selenium import webdriver
import requests
import pages.login as login

@pytest.fixture(scope='function')
def driver():
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions.headless = True
    chromeOptions.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=chromeOptions)

    driver.get("https://parabank.parasoft.com/parabank/index.htm")

    yield driver

    driver.close()


@pytest.fixture(scope='function')
def clean_database():
    base_url = "https://parabank.parasoft.com/parabank/services/bank"
    print('Cleaning database prior to test run')
    response = requests.post(f'{base_url}/cleanDB')
    
    assert response.status_code == 204

@pytest.fixture(scope='function')
def login_user(driver):
    login_page = login.LoginPage(driver)
    login_page.login("john", "demo")

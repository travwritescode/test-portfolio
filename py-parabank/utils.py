import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException


MAX_WAIT = 10


def get_account_row_contents(driver, account):
    # Wait for the account table to properly load
    wait_for_element_to_be_visible(driver, By.LINK_TEXT, account)

    # Search table and return the row contents of the given account
    tbody = driver.find_element(By.XPATH, "//table[@id='accountTable']/tbody")
    for row in tbody.find_elements(By.XPATH, './/tr'):
        row_data = row.find_elements(By.XPATH, './/td')
        if (row_data[0].text == account):
            return row_data[0].text, row_data[1].text, row_data[2].text
        else:
            raise Exception("An error occurred or the account could not be found")


# Helper to wait for an element to be visible, return the elements when it is
def wait_for_element_to_be_visible(browser, by, path):
    start_time = time.time()
    while True:
        try:
            element = browser.find_element(by, path)
            return element
        except (AssertionError, WebDriverException) as e:
            if time.time() - start_time > MAX_WAIT:
                raise e
            time.sleep(0.5)
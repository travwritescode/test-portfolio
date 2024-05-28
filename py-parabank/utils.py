import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException

def get_account_row_contents(driver, account):
    tbody = driver.find_element(By.XPATH, "//table[@id='accountTable']/tbody")
    for row in tbody.find_elements(By.CSS_SELECTOR, 'tr'):
        row.find_elements(By.CSS_SELECTOR, 'td')
        if (row[0].text == account):
            print(row[0].text)
            print(row[1].text)
            print(row[2].text)
            return row[0].text, row[1].text, row[2].text
        else:
            raise Exception("An error occurred or the account could not be found")

# def wait_for_element_to_be_visible(browser, by, path):
#     start_time = time.time()
#     while True:
#         try:
#             element = browser.find_element(by, path)
#             return element
#         except (AssertionError, WebDriverException) as e:
#             if time.time() - start_time > MAX_WAIT:
#                 raise e
#             time.sleep(0.5)
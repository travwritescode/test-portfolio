from selenium.webdriver.common.by import By

class AccountDetailsPageLocators(object):
    ACCOUNT_ID = (By.ID, 'accountId')
    ACCOUNT_TYPE = (By.ID, 'accountType')
    ACCOUNT_BALANACE = (By.ID, 'balance')
    AVAILABLE_BALANCE = (By.ID, 'availableBalance')

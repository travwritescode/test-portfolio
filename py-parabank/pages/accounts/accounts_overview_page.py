from pages.base_page import BasePage
from locators.accounts_overview_locators import AccountsOverviewPageLocators
from utils import get_account_row_contents
from selenium.webdriver.common.by import By


class AccountsOverviewPage(BasePage):
    def open_details_page(self, account):
        account_link = self.driver.find_element(By.LINK_TEXT, account)
        account_link.click()

    def open_overview_page(self):
        link = self.driver.find_element(*AccountsOverviewPageLocators.ACCOUNTS_OVERVIEW_LINK)
        link.click()

    def shows_starter_account(self):
        account, balance, available_amount = get_account_row_contents(self.driver, '13344')
        return account == '13344' and balance == '$5022.93' and available_amount == '$5022.93'


        
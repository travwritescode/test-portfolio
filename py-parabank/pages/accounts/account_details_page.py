from pages.base_page import BasePage
from locators.account_details_locators import AccountDetailsPageLocators


class AccountDetailsPage(BasePage):
    def account_number_matches(self, account_number):
        displayed_account_number = self.driver.find_element(*AccountDetailsPageLocators.ACCOUNT_ID).text
        return displayed_account_number == account_number
    

    def account_type_matches(self, account_type):
        displayed_account_type = self.driver.find_element(*AccountDetailsPageLocators.ACCOUNT_TYPE).text
        return displayed_account_type == account_type
    

    def account_balance_matches(self, account_balance):
        displayed_account_balance = self.driver.find_element(*AccountDetailsPageLocators.ACCOUNT_BALANACE).text
        return displayed_account_balance == account_balance
    

    def available_balance_matches(self, available_balance):
        displayed_available_balance = self.driver.find_element(*AccountDetailsPageLocators.AVAILABLE_BALANCE).text
        return displayed_available_balance == available_balance

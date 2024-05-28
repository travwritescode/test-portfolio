from pages.base import BasePage
from locators.accounts_overview_locators import AccountsOverviewPageLocators
from utils import get_account_row_contents

class AccountsOverviewPage(BasePage):
    def open_accounts_overview_page(self):
        link = self.driver.find_element(*AccountsOverviewPageLocators.ACCOUNTS_OVERVIEW_LINK)
        link.click()

    def does_overview_show_starter_account(self):
        account, balance, available_amount = get_account_row_contents(self.driver, '13344')
        return account == '13344' and balance == '$5022.93' and available_amount == '$5022.93'


        
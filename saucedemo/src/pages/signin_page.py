from seleniumpagefactory.Pagefactory import PageFactory

class SignInpage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'ipt_username': ('XPATH', '//*[@data-test="username"]'),
        'ipt_password': ('XPATH', '//*[@data-test="password"]'),
        'btn_login': ('XAPTH', '//*[@data-test="login-button"]')
    }

    def login(self, username, password):
        self.ipt_username.set_text(username)
        self.ipt_password.set_text(password)
        self.btn_login.click_button()

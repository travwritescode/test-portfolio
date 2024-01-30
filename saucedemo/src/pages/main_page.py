from seleniumpagefactory.Pagefactory import PageFactory

class MainPage(PageFactory):
    def __init__(self, driver):
        self.driver = driver

    locators = {
        'shopping_cart_container', ('ID', 'shopping_cart_container')
    }

    def is_page_loaded(self):
        self.shopping_cart_container.visibility
from pageobject.base_page import BasePage


class ShoppingCartPage(BasePage):

    def get_url(self):
        return 'http://tutorialsninja.com/demo/index.php?route=checkout/cart'

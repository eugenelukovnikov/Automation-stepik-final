from settings import *
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage): 

    def should_not_be_products_on_page(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_TABLE), "Product table is presented, but should not"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "Text about empty basket is not presented"
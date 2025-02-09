from .base_page import BasePage
from .locators import ProductPageLocators
import time




class ProductPage(BasePage): 
    
    PRODUCT_PAGE_URL = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

    def __init__(self, driver, url=PRODUCT_PAGE_URL):
        super().__init__(driver, url)

    
    def add_to_basket(self):
        add_button = self.driver.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        add_button.click()
    
    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET), "Add button is not presented"
    
    def name_in_alert_should_be_equal_to_item_name(self):
        product_name = self.driver.find_element(*ProductPageLocators.PRODUCT_NAME).text
        time.sleep(5)
        name_in_first_alert = self.driver.find_element(*ProductPageLocators.FIRST_ALERT_NAME).text
        assert product_name == name_in_first_alert, f"Product name {product_name} and name in the message {name_in_first_alert} don't match"

    def basket_price_in_alert_should_be_equal_to_item_price(self):
        product_price = self.driver.find_element(*ProductPageLocators.PRICE).text
        third_alert_basket_price = self.driver.find_element(*ProductPageLocators.THIRD_ALERT_BASKET_PRICE).text
        assert product_price == third_alert_basket_price, f"Product price {product_price} and price in the message {third_alert_basket_price} don't match"



from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 
    
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, driver, url=MAIN_PAGE_URL):
        super().__init__(driver, url)

    def go_to_login_page(self):
        login_link = self.driver.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
from .base_page import BasePage

class MainPage(BasePage): 
    
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, driver, url=MAIN_PAGE_URL):
        super().__init__(driver, url)

    def go_to_login_page(self):
        login_link = self.driver.find_element('xpath', "//a[@id='login_link']")
        login_link.click()
    
    def should_be_login_link(self):
        assert self.is_element_present('xpath', "//a[@id='login_link']"), "Login link is not presented"
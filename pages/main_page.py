from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage): 
    
    MAIN_PAGE_URL = "http://selenium1py.pythonanywhere.com/"

    def __init__(self, driver, url=MAIN_PAGE_URL):
         super().__init__(driver, url)
    # def __init__(self, *args, **kwargs):
    #     super(MainPage, self).__init__(*args, **kwargs)

    
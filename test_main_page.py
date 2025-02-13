from settings import *
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

@pytest.mark.skip
def test_guest_should_see_login_link(driver):
    #link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(driver)
    page.open()
    page.should_be_login_link()

@pytest.mark.skip
def test_guest_can_go_to_login_page(driver):
    #link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(driver)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(driver, driver.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(driver):
    page = MainPage(driver)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_products_on_page()
    basket_page.should_be_empty_basket_text()

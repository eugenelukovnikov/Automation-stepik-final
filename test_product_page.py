from settings import *

from pages.product_page import ProductPage


# def test_guest_can_add_product_to_basket(driver):
#     page = ProductPage(driver)
#     page.open()
#     page.should_be_add_button()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.name_in_alert_should_be_equal_to_item_name()
#     page.basket_price_in_alert_should_be_equal_to_item_price()


# @pytest.mark.parametrize("offer", [
#     pytest.param(0, id="offer_0"),
#     pytest.param(1, id="offer_1"),
#     pytest.param(2, id="offer_2"),
#     pytest.param(3, id="offer_3"),
#     pytest.param(4, id="offer_4"),
#     pytest.param(5, id="offer_5"),
#     pytest.param(6, id="offer_6"),
#     pytest.param(7, id="offer_7"),
#     pytest.param(8, id="offer_8"),
#     pytest.param(9, id="offer_9"),
# ])
# def test_guest_can_add_product_to_basket(driver, offer):
#     link = (
#         f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#         f"?promo=offer{offer}"
#     )
#     if offer == 7:
#         pytest.xfail("Ожидаемый сбой для offer = 7")
#     page = ProductPage(driver, link)
#     print('Мы на странице:', link)
#     page.open()
#     page.should_be_add_button()
#     page.add_to_basket()
#     page.solve_quiz_and_get_code()
#     page.name_in_alert_should_be_equal_to_item_name()
#     page.basket_price_in_alert_should_be_equal_to_item_price()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.should_not_be_success_message()

@pytest.mark.skip
def test_guest_cant_see_success_message(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_not_be_success_message()
    
@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.success_message_should_disappear()

def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver, 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver, 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/')
    page.open()
    page.go_to_login_page()
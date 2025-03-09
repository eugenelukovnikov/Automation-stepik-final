from settings import *
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage

@pytest.mark.parametrize("offer", [
    pytest.param(0, id="offer_0"),
    pytest.param(1, id="offer_1"),
    pytest.param(2, id="offer_2"),
    pytest.param(3, id="offer_3"),
    pytest.param(4, id="offer_4"),
    pytest.param(5, id="offer_5"),
    pytest.param(6, id="offer_6"),
    pytest.param(7, id="offer_7"),
    pytest.param(8, id="offer_8"),
    pytest.param(9, id="offer_9"),
])
@allure.feature("Карточка товара")
@allure.story("Добавление товара в корзину - гость")
@allure.title("Проверка успешного добавления товара в корзину")
@pytest.mark.skip
def test_guest_can_add_product_to_basket(driver, offer):
    link = (
        f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        f"?promo=offer{offer}"
    )
    if offer == 7:
        pytest.xfail("Ожидаемый сбой для offer = 7")
    page = ProductPage(driver, link)
    print('Мы на странице:', link)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.name_in_alert_should_be_equal_to_item_name()
    page.basket_price_in_alert_should_be_equal_to_item_price()

@allure.feature("Карточка товара")
@allure.story("Уведомления о добавлении товара в корзину не должно быть - гость")
@allure.title("Проверка отсутствия уведомления об успешном добавлении в корзину") 
@pytest.mark.skip #xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.should_not_be_success_message()

@allure.feature("Карточка товара")
@allure.story("Уведомление о добавлении товара в корзину должно пропадать")
@allure.title("Проверка исчезновения уведомления о добавлении в корзину")   
@pytest.mark.skip #xfail
def test_message_disappeared_after_adding_product_to_basket(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.success_message_should_disappear()

@allure.feature("Карточка товара")
@allure.story("С карточки товара можно перейти на страницу логина - гость")
@allure.title("Проверка наличия ссылки на страницу логина")
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(driver):
    page = ProductPage(driver)
    page.open()
    page.should_be_login_link()

@allure.feature("Карточка товара")
@allure.story("С карточки товара можно перейти на страницу логина - гость")
@allure.title("Проверка успешного перехода на страницу логина из карточки товара")
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(driver):
    page = ProductPage(driver)
    page.open()
    page.go_to_login_page()

@allure.feature("Карточка товара")
@allure.story("Корзина по умолчанию является пустой - гость")
@allure.title("Проверка отсутствия товара после перехода в корзину")
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    page = ProductPage(driver)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_products_on_page()
    basket_page.should_be_empty_basket_text()

@allure.feature("Карточка товара")
@allure.story("После добавления товара в корзину, он должен находиться в ней - гость")
@allure.title("Проверка наличия товара в корзине после добавления с карточки товара") 
@pytest.mark.skip #xfail
def test_guest_can_see_product_in_basket_after_adding_from_product_page(driver):
    page = ProductPage(driver)
    page.open()
    page.add_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_not_be_products_on_page()
    basket_page.should_be_empty_basket_text()

@allure.feature("Карточка товара")
@allure.story("Уведомления о добавлении товара в корзину не должно быть - гость")
@allure.title("Проверка отсутствия уведомления об успешном добавлении в корзину") 
@pytest.mark.skip
def test_guest_cant_see_success_message(driver): 
    page = ProductPage(driver)
    page.open()
    page.should_not_be_success_message()

@allure.feature("Карточка товара")
@allure.story("Добавление товара в корзину - гость")
@allure.title("Проверка успешного добавления товара в корзину")
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(driver):
    page = ProductPage(driver)
    page.open()
    page.should_be_add_button()
    page.add_to_basket()
    page.name_in_alert_should_be_equal_to_item_name()
    page.basket_price_in_alert_should_be_equal_to_item_price()

@allure.feature("Карточка товара")
class TestUserAddToBasketFromProductPage():
    
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver):
        page = LoginPage(driver)
        page.open()
        page.register_new_user(email = fake.email(), password = fake.password())
        page.should_be_authorized_user()
    
    @allure.story("Уведомления о добавлении товара в корзину не должно быть - авторизованный")
    @allure.title("Проверка отсутствия уведомления об успешном добавлении в корзину")
    @pytest.mark.skip
    def test_user_cant_see_success_message(self, driver): 
        page = ProductPage(driver)
        page.open()
        page.should_not_be_success_message()
    
    @allure.story("Добавление товара в корзину - авторизованный")
    @allure.title("Проверка успешного добавления товара в корзину")
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, driver):
        page = ProductPage(driver)
        page.open()
        page.should_be_add_button()
        page.add_to_basket()
        page.name_in_alert_should_be_equal_to_item_name()
        page.basket_price_in_alert_should_be_equal_to_item_price()
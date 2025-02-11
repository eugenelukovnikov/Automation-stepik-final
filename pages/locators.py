
class BasePageLocators():
    LOGIN_LINK = ('xpath', "//a[@id='login_link']")
    LOGIN_LINK_INVALID = ('xpath', "//a[@id='login_link_inc']")
    BASKET_LINK = ('xpath', "//span[@class='btn-group']//a[contains(@class,'btn-default')]")


class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = ('xpath', "//form[@id='login_form']")
    REGISTER_FORM = ('xpath', "//form[@id='register_form']")


class BasketPageLocators():
    EMPTY_BASKET_TEXT = ('xpath', "//div[@id='content_inner']/p")
    BASKET_TABLE = ('xpath', "//form[@id='basket_formset']")


class ProductPageLocators():
    PRODUCT_NAME = ('xpath', "//h1")
    BTN_ADD_TO_BASKET = ('xpath', "//button[contains(@class,'btn-add-to-basket')]")
    PRICE = ('xpath', "//p[@class='price_color']")
    FIRST_ALERT_NAME = ('xpath', "(//div[@class='alertinner '])[1]//strong")
    THIRD_ALERT_BASKET_PRICE = ('xpath', "(//div[@class='alertinner '])[3]//p//strong")
    SUCCESS_MESSAGE = ('xpath', "//div[contains(@class,'alert-success')][1]")

class BasePageLocators():
    LOGIN_LINK = ('xpath', "//a[@id='login_link']")
    LOGIN_LINK_INVALID = ('xpath', "//a[@id='login_link_inc']")

class MainPageLocators():
    pass


class LoginPageLocators():
    LOGIN_FORM = ('xpath', "//form[@id='login_form']")
    REGISTER_FORM = ('xpath', "//form[@id='register_form']")


class ProductPageLocators():
    PRODUCT_NAME = ('xpath', "//h1")
    BTN_ADD_TO_BASKET = ('xpath', "//button[contains(@class,'btn-add-to-basket')]")
    PRICE = ('xpath', "//p[@class='price_color']")
    FIRST_ALERT_NAME = ('xpath', "(//div[@class='alertinner '])[1]//strong")
    THIRD_ALERT_BASKET_PRICE = ('xpath', "(//div[@class='alertinner '])[3]//p//strong")
    SUCCESS_MESSAGE = ('xpath', "//div[contains(@class,'alert-success')][1]")
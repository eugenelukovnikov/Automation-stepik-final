from settings import *
# from selenium.common.exceptions import NoSuchElementException
# from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators


class BasePage():
    
    def __init__(self, driver, url, timeout=5):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def go_to_login_page(self):
        link = self.driver.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def go_to_basket_page(self):
        link = self.driver.find_element(*BasePageLocators.BASKET_LINK)
        link.click()    

    def open(self):
        self.driver.get(self.url)

    # def is_element_present(self, how, what):
    #     try:
    #         self.driver.find_element(how, what)
    #     except (NoSuchElementException):
    #         return False
    #     return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout).until(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    def is_element_present(self, how, what, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.driver, timeout, 1, TimeoutException).until_not(ec.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
   
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented, probably unauthorised user"

    def solve_quiz_and_get_code(self):
        alert = self.driver.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        # alert.accept() #Отключен, чтобы проходил нормально тест test_product_page
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
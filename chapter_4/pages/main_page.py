"""
https://stepik.org/lesson/238819/step/10?unit=211271
example from lesson 2 step 10
"""

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        # если будет добавлен alert в страницы
        # alert = self.browser.switch_to.alert
        # alert.accept()

        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

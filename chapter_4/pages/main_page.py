"""
https://stepik.org/lesson/238819/step/5?unit=211271
example from lesson 2 step 5

В качестве ответа на данное задание напишите название исключения, которое вы получили в результате запуска теста.
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

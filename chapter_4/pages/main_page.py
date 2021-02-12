"""
https://stepik.org/lesson/238819/step/3?unit=211271
example from lesson 2 step 3
"""
from .base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

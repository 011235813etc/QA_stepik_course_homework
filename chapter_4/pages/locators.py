"""
https://stepik.org/lesson/238819/step/8?unit=211271
example from lesson 2 step 8
"""

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_OFFERED = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_OFFERED = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner  strong")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")

from selenium.webdriver.common.by import By


class BasePageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")
    BASKET_WITH_PRODUCT = (By.CSS_SELECTOR, "#content_inner .basket-title")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    MAIN_LINK = (By.CSS_SELECTOR, ".col-sm-7.h1")
    TITLE_BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner > p")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_FORM_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_FORM_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_FORM_PASSWORD_CONFIRM = (By.ID, "id_registration-password2")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner  strong")
    PRODUCT_NAME_OFFERED = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-info .alertinner strong")
    PRODUCT_PRICE_OFFERED = (By.CSS_SELECTOR, ".product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")

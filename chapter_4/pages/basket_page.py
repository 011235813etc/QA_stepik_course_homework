from .base_page import BasePage
from .locators import BasePageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        current_url = self.browser.current_url
        # проверяем наличие слова "basket" в url текущей страницы
        assert "basket" in current_url, "Login page don't have 'basket' word in url"

    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.BASKET_WITH_PRODUCT), \
            "Basket is not empty"

    def should_be_title_basket_is_empty(self):
        assert self.is_element_present(*BasePageLocators.TITLE_BASKET_IS_EMPTY), \
            "Title 'Basket is empty' is not present"

    def should_not_be_empty_basket(self):
        assert self.is_element_present(*BasePageLocators.BASKET_WITH_PRODUCT), \
            "Basket is empty"

    def should_not_be_title_basket_is_empty(self):
        assert self.is_not_element_present(*BasePageLocators.TITLE_BASKET_IS_EMPTY), \
            "Title 'Basket is empty' is present"

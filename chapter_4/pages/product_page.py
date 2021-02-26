from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def get_product_name_from_description(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_OFFERED).text

    def get_product_price_from_description(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_OFFERED).text

    def should_be_added_to_basket(self):
        try:
            # ищем кнопку и добавляем в корзину
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
            self.solve_quiz_and_get_code()
        except NoSuchElementException:
            assert False, "Not found button 'Add to basket'"

    def should_be_same_product_name(self, product_name_offered):
        # получаем название товара в корзине
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert product_name_offered == name_in_basket, "Offered name and name in basket is not equal"

    def should_be_same_product_price(self, product_price_offered):
        # получаем цену в корзине
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert product_price_offered == price_in_basket, "Offered price and price in basket is not equal"

    def should_be_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is  not disappeared, but should be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
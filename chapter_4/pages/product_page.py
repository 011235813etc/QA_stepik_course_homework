"""
https://stepik.org/lesson/201964/step/5?unit=176022
example from lesson 3 step 5

Метод-проверка в классе про страницу товара будет выглядеть аналогично
should_not_be_success_message, напишите его самостоятельно.
"""
from selenium.common.exceptions import NoSuchElementException
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_added_to_basket(self):
        self.should_not_be_success_message()
        # self.should_be_added_by_button()
        # self.should_be_same_product_name()
        # self.should_be_same_product_price()

    def should_be_added_by_button(self):
        try:
            # ищем кнопку и добавляем в корзину
            self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
            self.solve_quiz_and_get_code()
        except NoSuchElementException:
            print("Not found button 'Add to basket'")

    def _get_description(self, locator):
        return self.browser.find_element(*locator).text

    def should_be_same_product_name(self):
        # получаем название продукта в описании товара
        name_offered = self._get_description(ProductPageLocators.PRODUCT_NAME_OFFERED)
        # получаем название товара в корзине
        name_in_basket = self._get_description(ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert name_offered == name_in_basket, "Offered name and name in basket is not equal"

    def should_be_same_product_price(self):
        # получаем предлагаемую цену товара
        price_offered = self._get_description(ProductPageLocators.PRODUCT_PRICE_OFFERED)
        # получаем цену в корзине
        price_in_basket = self._get_description(ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        assert price_offered == price_in_basket, "Offered price and price in basket is not equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

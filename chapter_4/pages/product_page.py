from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_added_to_basket(self):
        self.should_be_added_by_button()
        self.should_be_same_product_name()
        self.should_be_same_product_price()

    def should_be_added_by_button(self):
        # ищем кнопку
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        # добавляем в корзину
        button.click()
        self.solve_quiz_and_get_code()
        assert button is not None, "Not found button 'Add to basket'"

    def should_be_same_product_name(self):
        # получаем название продукта в описании товара
        name_offered = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_OFFERED).text
        # получаем название товара в корзине
        name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text
        assert name_offered == name_in_basket, "Offered name and name in basket is not equal"

    def should_be_same_product_price(self):
        # получаем предлагаемую цену товара
        price_offered = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_OFFERED).text
        # получаем цену в корзине
        price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        assert price_offered == price_in_basket, "Offered price and price in basket is not equal"

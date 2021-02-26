import pytest
import time
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.links import ProductPageLinks


@pytest.mark.parametrize('link', ProductPageLinks.add_product_in_basket)
@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, link):
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, link):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        page.open()
        page.should_be_added_to_basket()
        product_name_offered = page.get_product_name_from_description()
        page.should_be_same_product_name(product_name_offered)
        product_price_offered = page.get_product_price_from_description()
        page.should_be_same_product_price(product_price_offered)

    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

@pytest.mark.parametrize('link', ProductPageLinks.promo_offers)
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    product_name_offered = page.get_product_name_from_description()
    page.should_be_same_product_name(product_name_offered)
    product_price_offered = page.get_product_price_from_description()
    page.should_be_same_product_price(product_price_offered)


@pytest.mark.parametrize('link', ProductPageLinks.check_functionality)
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.parametrize('link', ProductPageLinks.check_functionality)
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_title_basket_is_empty()


@pytest.mark.parametrize('link', ProductPageLinks.add_product_in_basket)
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ProductPageLinks.add_product_in_basket)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', ProductPageLinks.check_functionality)
def test_guest_should_see_login_link_on_product_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', ProductPageLinks.add_product_in_basket)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_be_success_message_disappeared()

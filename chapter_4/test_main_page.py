import pytest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.links import MainPageLinks


@pytest.mark.parametrize('link', MainPageLinks.main_page)
def test_guest_can_go_to_login_page(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.parametrize('link', MainPageLinks.main_page)
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.go_to_main_page()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_title_basket_is_empty()


@pytest.mark.parametrize('link', MainPageLinks.main_page)
def test_guest_should_see_login_link(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.parametrize('link', MainPageLinks.main_page)
@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser, link):
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        page.open()
        # выполняем метод страницы — переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser, link):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

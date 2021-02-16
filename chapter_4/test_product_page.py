"""
https://stepik.org/lesson/201964/step/13?unit=176022
example lesson 3 step 13

Задание: группировка тестов и setup

ВАЖНО! Вообще говоря манипулировать браузером в сетапе и уж тем более что-то там
проверять — это плохая практика, лучше так не делать без особой необходимости.
Здесь этот пример исключительно в учебных целях, чтобы вы попробовали писать сетапы
для тестов. В реальной жизни мы реализовали бы все эти манипуляции с помощью API
или напрямую через базу данных.

В этом задании мы хотим добавить тестовые сценарии не только для гостей сайта, но и
для зарегистрированных пользователей. Для этого:

   - В файле test_product_page.py добавьте новый класс для тестов TestUserAddToBasketFromProductPage.
   - Добавьте туда уже написанные тесты test_guest_cant_see_success_message и
   test_guest_can_add_product_to_basket и переименуйте, заменив guest на user.
    Шаги тестов не изменятся, добавится лишь регистрация перед тестами.
    Параметризация здесь уже не нужна, не добавляйте её.
   - Добавьте в LoginPage метод register_new_user(email, password), который принимает
   две строки и регистрирует пользователя. Реализуйте его, описав соответствующие элементы страницы.
   - Добавьте в BasePage проверку того, что пользователь залогинен:

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                     " probably unauthorised user"

    Селектор соответственно в BasePageLocators:

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

    Добавьте в класс фикстуру setup. В этой функции нужно:
        открыть страницу регистрации;
        зарегистрировать нового пользователя;
        проверить, что пользователь залогинен.
    Запустите оба теста и убедитесь, что они проходят и действительно регистрируют новых пользователей
    Зафиксируйте изменения в репозитории коммитом с осмысленным сообщением

Примечание:

yield писать не нужно — пользователей удалять мы не умеем. Генерировать email адреса
для пользователей можно по-разному, один из вариантов, чтобы избежать повторения,
использовать текущее время с помощью модуля time:

import time # в начале файла

email = str(time.time()) + "@fakemail.org"
"""
import pytest
import time

from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


@pytest.mark.login
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.go_to_login_page()

        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = ProductPage(browser, link)
        page.open()
        page.should_be_added_to_basket()
        page.should_be_same_product_name()
        page.should_be_same_product_price()


@pytest.mark.parametrize('link',
    [
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
    ])
def test_guest_can_add_product_to_basket(browser, link):
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_be_same_product_name()
    page.should_be_same_product_price()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_be_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_title_basket_is_empty()

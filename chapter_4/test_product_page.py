"""
Задание: отрицательные проверки

Добавьте к себе в проект функции из предыдущего шага и реализуйте несколько простых тестов:

test_guest_cant_see_success_message_after_adding_product_to_basket:

   1. Открываем страницу товара
   2. Добавляем товар в корзину
   3. Проверяем, что нет сообщения об успехе с помощью is_not_element_present

test_guest_cant_see_success_message:

   1. Открываем страницу товара
   2. Проверяем, что нет сообщения об успехе с помощью is_not_element_present

test_message_disappeared_after_adding_product_to_basket:

   1. Открываем страницу товара
   2. Добавляем товар в корзину
   3. Проверяем, что нет сообщения об успехе с помощью is_disappeared

Запустите все три теста, и отметьте ниже верные утверждения для каждого теста.

Важно! После того как пройдете это задание, те тесты, которые упали пометьте как
XFail или skip, как это сделать мы разбирали в модуле 3: XFail: помечать тест как ожидаемо падающий.
"""
import pytest
from .pages.product_page import ProductPage

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


@pytest.mark.parametrize('link', [
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
        marks=pytest.mark.xfail
    )])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link',
        ["http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.parametrize('link', [
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear",
        marks=pytest.mark.xfail
    )])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_added_to_basket()
    page.should_be_success_message_disappeared()

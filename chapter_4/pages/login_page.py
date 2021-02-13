"""
https://stepik.org/lesson/238819/step/8?unit=211271
example from lesson 2 step 8

Реализация LoginPage

Если вы хорошо ориентируетесь в тест-дизайне, скорее всего вас немного коробит тест с переходом к логину —
там ведь нет никаких проверок. Давайте проверим, что мы действительно перешли на страницу логина.
Для этого нам будет нужен новый Page Object. Заодно разберемся, как между ними переключаться в ходе теста.

Скачайте файл с шаблоном для LoginPage. Добавьте его в папку pages. Внутри есть заглушки для методов проверок:

should_be_login_url
should_be_login_form
should_be_register_form

Реализуйте их самостоятельно:

1. В файле locators.py создайте класс LoginPageLocators

2. Подберите селекторы к формам регистрации и логина, добавьте их в класс LoginPageLocators

3. Напишите проверки, используя эти селекторы. Не забудьте через запятую указать адекватное сообщение
об ошибке. Напишите сначала красный тест, чтобы убедиться в понятности вывода.

4. В методе should_be_login_url реализуйте проверку, что подстрока "login" есть в текущем url браузера.
Для этого используйте соответствующее свойство Webdriver.

5. Добавьте изменения в коммит с осмысленным сообщением

Теперь посмотрим, как можно осуществлять переход между страницами.
"""
from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес

        # ищем кнопку для перехода на страницу регистрации
        login_page = self.browser.find_element(*LoginPageLocators.LOGIN_URL)
        # переходим на страницу регистрации
        login_page.click()
        # получаем url текущей страницы
        current_url = self.browser.current_url
        # проверяем наличие слова "login" в url текущей страницы
        assert "login" in current_url, "Login page don't have 'login' word in url"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

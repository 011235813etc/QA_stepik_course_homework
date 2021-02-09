"""
Задание: параметризация тестов

Инопланетяне оставляют загадочные сообщения на Stepik в фидбеке задач на правильное решение.
Мы смогли локализовать несколько url-адресов задач, где появляются кусочки сообщений.
Ваша задача — реализовать автотест со следующим сценарием действий:

   - открыть страницу
   - ввести правильный ответ
   - нажать кнопку "Отправить"
   - дождаться фидбека о том, что ответ правильный
   - проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"

   Правильным ответом на задачу в заданных шагах является число:

Опциональный фидбек — это текст в черном поле, как показано на скриншоте:

import time
import math
answer = math.log(int(time.time()))

Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:

https://stepik.org/lesson/236895/step/1
https://stepik.org/lesson/236896/step/1
https://stepik.org/lesson/236897/step/1
https://stepik.org/lesson/236898/step/1
https://stepik.org/lesson/236899/step/1
https://stepik.org/lesson/236903/step/1
https://stepik.org/lesson/236904/step/1
https://stepik.org/lesson/236905/step/1

Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания,
чтобы тесты работали стабильно.

В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке
не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте
в качестве ответа на это задание.

Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное
локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно,
иначе они устаревают.
"""
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest
import time
import math

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1'
]


# Фикстура возвращающий значение для передачи в поле
@pytest.fixture
def answer():
    return math.log(int(time.time()))


# Фикстура запуска и закрытия браузера
@pytest.fixture
def browser():
    print("\nstart browser for test...")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser...")
    browser.quit()


# Тест с параметризированным декоратором
@pytest.mark.parametrize('link', links)
def test_get_aliens_message(browser, answer, link):
    timeout = 10
    browser.get(link)

    # Ожидаем загрузки поля ввода ответа
    WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".textarea"))
        ).send_keys(str(answer))

    # Ожидаем доступности кнопки отправки результата
    WebDriverWait(browser, timeout).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        ).click()

    # Ожидаем поле проверки корреткности введенной ранее информации
    result_text = WebDriverWait(browser, timeout).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))
        ).text

    # Сравниваем полученную строку с ожидаемым значением
    assert result_text == "Correct!", f"{result_text}"

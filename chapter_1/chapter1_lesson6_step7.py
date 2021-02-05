"""
Задание: использование метода find_elements_by

В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html).
С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта.
В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали,
добавив в форму 100 обязательных полей и ограничив время на ее заполнение.
Теперь эта задача под силу только роботам.

Используйте WebDriver и подходящий метод find_elements_by. Введите полученный код в качестве ответа к этой задаче.

Используйте приведенный ниже шаблон: в цикле for мы можем последовательно взять каждый элемент
из найденного списка текстовых полей и отправить произвольный текст в каждое поле.
Если скрипт не успевает заполнить форму, выберите текст покороче.

from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_ * (value)
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
"""
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
       element.send_keys("Мой ответ")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

"""
Задание: принимаем alert

В этой задаче вам нужно написать программу, которая будет выполнять следующий сценарий:

   - Открыть страницу http://suninjuly.github.io/alert_accept.html
   - Нажать на кнопку
   - Принять confirm
   - На новой странице решить капчу для роботов, чтобы получить число с ответом

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
from selenium import webdriver
import time
import math


def calc(x: str) -> str:
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/alert_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Нажимаем на кнопку для запуска задачи
        browser.find_element_by_css_selector("button.btn").click()

        # Соглашаемся с окном типа confirm
        browser.switch_to.alert.accept()

        # Получаем значение x и рассчитываем y
        x = browser.find_element_by_id("input_value").text
        y = calc(x)

        # Заполняем форму
        browser.find_element_by_id("answer").send_keys(y)

        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

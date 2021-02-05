"""
Задание: переход на новую вкладку

В этом задании после нажатия кнопки страница откроется в новой вкладке, нужно переключить
WebDriver на новую вкладку и решить в ней задачу.

Сценарий для реализации выглядит так:

   - Открыть страницу http://suninjuly.github.io/redirect_accept.html
   - Нажать на кнопку
   - Переключиться на новую вкладку
   - Пройти капчу для робота и получить число-ответ

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа на это задание.
"""
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/redirect_accept.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Нажимаем на кнопку для запуска задачи
        browser.find_element_by_css_selector("button.btn").click()

        # Переключаемся на следующее окно
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)

        # Получаем значение x
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

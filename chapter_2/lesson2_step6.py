"""
Задание на execute_script

В данной задаче вам нужно будет снова преодолеть капчу для роботов и справиться с ужасным и огромным футером,
который дизайнер всё никак не успевает переделать. Вам потребуется написать код, чтобы:

   - Открыть страницу http://SunInJuly.github.io/execute_script.html.
   - Считать значение для переменной x.
   - Посчитать математическую функцию от x.
   - Проскроллить страницу вниз.
   - Ввести ответ в текстовое поле.
   - Выбрать checkbox "I'm the robot".
   - Переключить radiobutton "Robots rule!".
   - Нажать на кнопку "Submit".

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Отправьте полученное число в качестве ответа для этого задания.

Для этой задачи вам понадобится использовать метод execute_script,
чтобы сделать прокрутку в область видимости элементов, перекрытых футером.
"""
from selenium import webdriver
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


if __name__ == "__main__":
    try:
        link = "https://SunInJuly.github.io/execute_script.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Получаем записанное число
        x = int(browser.find_element_by_id("input_value").text)
        y = calc(x)

        # Поиск поля для ответа и размещение в нем посчитанного значения
        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(y))

        # Поиск checkbox с надписью "I'm the robot" и нажатие на него
        browser.find_element_by_id("robotCheckbox").click()

        # Поиск radiobutton с надписью "Robots rule" и нажатие на него
        robot_radio = browser.find_element_by_id("robotsRule")
        browser.execute_script("return arguments[0].scrollIntoView(true);", robot_radio)
        robot_radio.click()

        # Отправляем заполненную форму
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

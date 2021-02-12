"""
Задание: поиск сокровища с помощью get_attribute

В данной задаче вам нужно с помощью роботов решить ту же математическую задачу, как и в прошлом задании.
Но теперь значение переменной х спрятано в "сундуке", точнее, значение хранится
в атрибуте valuex у картинки с изображением сундука.

Ваша программа должна:

   - Открыть страницу http://suninjuly.github.io/get_attribute.html.
   - Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
   - Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
   - Посчитать математическую функцию от x (сама функция остаётся неизменной).
   - Ввести ответ в текстовое поле.
   - Отметить checkbox "I'm the robot".
   - Выбрать radiobutton "Robots rule!".
   - Нажать на кнопку "Submit".

Для вычисления значения выражения в п.4 используйте функцию calc(x) из предыдущей задачи.

Если все сделано правильно и достаточно быстро (в этой задаче тоже есть ограничение по времени),
вы увидите окно с числом. Скопируйте его в поле ниже и нажмите кнопку "Submit", чтобы получить баллы за задание.
"""
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/get_attribute.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Получение значения для расчета
        treasure = browser.find_element_by_id("treasure")
        x_value = treasure.get_attribute("valuex")
        y = calc(x_value)

        # Поиск поля для ответа и размещение в нем посчитанного значения
        answer = browser.find_element_by_id("answer")
        answer.send_keys(str(y))

        # Поиск checkbox с надписью "I'm the robot" и нажатие на него
        check_box = browser.find_element_by_id("robotCheckbox")
        check_box.click()

        # Поиск radiobutton с надписью "Robots rule" и нажатие на него
        radio_button = browser.find_element_by_id("robotsRule")
        radio_button.click()

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

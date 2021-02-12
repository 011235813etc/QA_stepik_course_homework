"""
Метод get_attribute

Мы уже знаем, как найти нужный элемент на странице и как получить видимый пользователю текст.
Для более детальных проверок в тесте нам может понадобиться узнать значение атрибута элемента.
Атрибуты могут быть стандартными свойствами, которые понимает и использует браузер для отображения
и вёрстки элементов или для хранения служебной информации, например, name, width, height, color и многие другие.
Также атрибуты могут быть созданы разработчиками проекта для задания собственных стилей или правил.

Значение атрибута представляет собой строку. Если значение атрибута отсутствует, то это равносильно
значению атрибута равному "false". Давайте еще раз взглянем на страницу http://suninjuly.github.io/math.html.
На ней есть radiobuttons, для которых выбрано значение по умолчанию. В автотесте нам может понадобиться проверить,
что для одного из radiobutton по умолчанию уже выбрано значение. Для этого мы можем проверить значение
атрибута checked у этого элемента. Вот HTML-код элемента:

<input class="check-input" type="radio" name="ruler" id="peopleRule" value="people" checked>

Найдём этот элемент с помощью WebDriver:

people_radio = browser.find_element_by_id("peopleRule")

Найдём атрибут "checked" с помощью встроенного метода get_attribute и проверим его значение:

people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"

Т.к. у данного атрибута значение не указано явно, то метод get_attribute вернёт "true".
Возможно, вы заметили, что "true" написано с маленькой буквы, — все методы WebDriver взаимодействуют
с браузером с помощью JavaScript, в котором булевые значения пишутся с маленькой буквы, а не с большой, как в Python.

Мы можем написать проверку другим способом, сравнив строки:

assert people_checked == "true", "People radio is not selected by default"

Если атрибута нет, то метод get_attribute вернёт значение None. Применим метод get_attribute
ко второму radiobutton, и убедимся, что атрибут отсутствует.

robots_radio = browser.find_element_by_id("robotsRule")
robots_checked = robots_radio.get_attribute("checked")
assert robots_checked is None

Так же мы можем проверять наличие атрибута disabled, который определяет, может ли пользователь
взаимодействовать с элементом. Например, в предыдущем задании на странице с капчей для роботов JavaScript
устанавливает атрибут disabled у кнопки Submit, когда истекает время, отведенное на решение задачи.

<button type="submit" class="btn btn-default" disabled>Submit</button>
"""
from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/math.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Проверка состояния radiobutton "People rule"
        people_radio_button = browser.find_element_by_id("peopleRule")
        people_checked = people_radio_button.get_attribute("checked")
        print("value of people radio: ", people_checked)
        assert  people_checked == "true", "People radio is not selected by default"

        # Проверка состояния radiobutton "Robots rule"
        robot_radio_button = browser.find_element_by_id("robotsRule")
        robots_checked = robot_radio_button.get_attribute("checked")
        print("value of robots_radio: ", robots_checked)
        assert  robots_checked is None, "Robot radio is selected by default"

        # Проверка состояния кнопки "Submit"
        button = browser.find_element_by_css_selector("button.btn")
        button_submit = button.get_attribute("disabled")
        print("value of button_submit: ", button_submit)
        assert  robots_checked is None, "Robot radio is selected by default"

        # Проверка состояния кнопки "Submit" после 10 секундного ожидания
        time.sleep(10)
        button = browser.find_element_by_css_selector("button.btn")
        button_submit = button.get_attribute("disabled")
        print("value of button_submit after 10sec: ", button_submit)
        assert  robots_checked is not None, "Robot radio is selected by default"

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

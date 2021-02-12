"""
Задание: поиск элемента по XPath

На этот раз воспользуемся возможностью искать элементы по XPath. 

На странице http://suninjuly.github.io/find_xpath_form вы найдете такую же форму регистрации, как в шаге 3,
при этом в нее добавилась куча одинаковых кнопок отправки. Но сработает только кнопка с текстом "Submit",
и наша задача нажать в коде именно на неё.

Ваши шаги: 

   - В коде из шага 4 замените ссылку на  http://suninjuly.github.io/find_xpath_form.
   - Подберите уникальный XPath-селектор так, чтобы он находил только кнопку с текстом Submit. XPath можете
   - формулировать как угодно (по тексту, по структуре, по атрибутам) - главное, чтобы он работал.
   - Модифицируйте код из шага 3 таким образом, чтобы поиск кнопки происходил с помощью XPath.
   - Запустите ваш код.

Если вы подобрали правильный селектор и все прошло хорошо, то вы получите код, который нужно
отправить в качестве ответа на это задание.
"""
from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value1 = "input"
    value2 = "last_name"
    value3 = "city"
    value4 = "country"

    input1 = browser.find_element_by_tag_name(value1)
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name(value2)
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name(value3)
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id(value4)
    input4.send_keys("Russia")
    button = browser.find_element_by_xpath("//button[text() = \"Submit\"]")
    button.click()

finally:
    time.sleep(30)
    browser.quit()

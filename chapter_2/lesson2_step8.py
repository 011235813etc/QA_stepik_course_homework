"""
Задание: загрузка файла

В этом задании в форме регистрации требуется загрузить текстовый файл.

Напишите скрипт, который будет выполнять следующий сценарий:

   - Открыть страницу http://suninjuly.github.io/file_input.html
   - Заполнить текстовые поля: имя, фамилия, email
   - Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
   - Нажать кнопку "Submit"

Если все сделано правильно и быстро, вы увидите окно с числом. 
Отправьте полученное число в качестве ответа для этого задания.
"""

from selenium import webdriver
import time
import os


if __name__ == "__main__":
    try:
        link = "http://suninjuly.github.io/file_input.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем поле имени
        firstname = browser.find_element_by_name("firstname")
        firstname.send_keys("Ivan")

        # Заполняем поле фамилии
        lastname = browser.find_element_by_name("lastname")
        lastname.send_keys("Petrov")

        # Заполняем поле электронной почты
        email = browser.find_element_by_name("email")
        email.send_keys("example@gmail.com")

        # Получаем путь до файла
        current_path = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_path, "lesson2_step8.txt")

        # Загружаем файл в форму
        load_file = browser.find_element_by_id("file")
        load_file.send_keys(file_path)

        # Отправляем заполненную форму
        button = browser.find_element_by_tag_name("button")
        browser.execute_script("return arguments[0].scrollIntoView(true);", button)
        button.click()

    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()

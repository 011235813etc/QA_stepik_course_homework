# QA_tests_stepik_course_homework
In this repository, I am post my course homework from stepik "QA course with Selenium and Python".

Link to online auto tests course: 
https://stepik.org/course/575/syllabus

Course completed. Link to certificate: 
https://stepik.org/cert/892410

Link with instructions installing Python 3 and virtual environment:
https://stepik.org/lesson/25969/step/2?unit=196192

Link with instructions installing Selenium:
https://stepik.org/lesson/25969/step/6?unit=196192

Link with instructions installing ChromeDriver:
https://stepik.org/lesson/25969/step/7?unit=196192

Command to run tests:
    
        pytest -v --tb=line --language=en \path\to\test_file_name.py

Небольшая инструкция по запуску:

1. Скачайте к себе проект, либо скачав и распаковав архив, либо склонировав репозитарий.
2. Создайте новое виртуальное окружение. Kак работать с виртуальными окружениями можно прочитать тут (для Windows):
https://stepik.org/lesson/25969/step/2?unit=196192
3. Перейдите в папку вновь созданного окружения:
cd \path\to\new_virtual_env\Scripts
4. Активируйте данное виртуальное окружение.
5. Установите пакеты в окружение из файла requirements.txt, который должен быть в скачанном проекте:
   

    pip install -r \path\to\requirements.txt
   
6. Убедитесь, что путь к chromedriver.exe прописан в PATH, либо скопируйте этот файл в текущую папку Scripts из шага 3.
7. Если chromedriver не установлен на компьютере, установите его следуя инструкциям на странице:
    https://stepik.org/lesson/25969/step/7?unit=196192
8. Запустите тесты командой:


    pytest -v --tb=line --language=en \path\to\test_file_name.py
9. Проверьте, что все тесты прошли успешно.
10. Если же тесты не запускаются, попробуйте сначала разобраться, в чем заключается ошибка. 
    Возможно, дело в путях к файлам в импорте -- тогда попробуйте поставить / убрать точку в начале и / или 
    добавить / удалить пустой файл __init__.py в корневой папке и / или подпапках.


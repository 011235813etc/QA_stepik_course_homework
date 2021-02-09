import time
import os


if __name__ == "__main__":
    myCmds = [
        'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it',
        'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans'
    ]

    # Запуск без параметров для проверки реакции программы на такую ситуацию
    os.system('pytest -s -v test_items.py')
    time.sleep(1)

    # Перебор всех языков
    for myCmd in myCmds:
        os.system(f'pytest -s -v --language={myCmd} test_items.py')
        time.sleep(1)

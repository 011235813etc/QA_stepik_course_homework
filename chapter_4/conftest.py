import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

language_settings = [
    'ar', 'ca', 'cs', 'da', 'de', 'en-gb', 'el', 'es', 'fi', 'fr', 'it',
    'ko', 'nl', 'pl', 'pt', 'pt-br', 'ro', 'ru', 'sk', 'uk', 'zh-hans'
]


# Добавление параметра --language
def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: " + ", ".join(language_settings))


# Фикстура запуска и закрытия браузера
@pytest.fixture(scope="function")
def browser(request):
    current_language = request.config.getoption("language")
    browser = None
    if current_language is None:
        raise pytest.UsageError("--language should be one of values: " + ", ".join(language_settings))
    else:
        print("\nstart chrome browser for test, current languages is " + str(current_language))
        # запуск браузера с выбранном языком в параметре --language
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': current_language})
        browser = webdriver.Chrome(options=options)
    yield browser
	# пауза для просмотра результата
    time.sleep(4)
    print("\nquit browser..")
    browser.quit()

"""
https://stepik.org/lesson/237240/step/4?unit=209628
example from lesson 6 step 4
"""
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

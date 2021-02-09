import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_check_exist_button_add_to_basket(browser):
    timeout = 10
    browser.get(link)

    # Проверяем наличие кнопки добавления в корзину с ожидаеним отображения на странице
    button = WebDriverWait(browser, timeout).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket"))
        )

    # Сравнение с ожидаемым результатом
    assert button is not None, f"Button does not exist"

"""
https://stepik.org/lesson/237240/step/6?unit=209628
example from lesson 6 step 6
"""
link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.find_element_by_css_selector("#login_link")

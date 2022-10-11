from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
import math

pages = ["https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",]

def calc():
    return str(math.log(int(time.time())))


@pytest.mark.parametrize('page', pages)
def test_stepik_page(browser, page):
    link = page
    browser.get(link)
    browser.implicitly_wait(10)
    input_answer = browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(calc())
    send_answer = browser.find_element(By.CLASS_NAME, "submit-submission").click()
    status = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert status == "Correct!",  status





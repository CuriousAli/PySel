from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import time
import math


link ="http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.TAG_NAME, "button").click()
    alert = browser.switch_to.alert.accept()

    x = int(browser.find_element(By.ID,"input_value").text)
    answer_input = browser.find_element(By.ID, "answer").send_keys(calc(x))

    button2 = browser.find_element(By.TAG_NAME, "button").click()

    addToClipBoard = (browser.switch_to.alert.text).split(': ')[-1]
    pyperclip.copy(addToClipBoard)

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
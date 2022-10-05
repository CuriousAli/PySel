from selenium import webdriver
from selenium.webdriver.common.by import By
import pyperclip
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button").click()
    browser.switch_to.window(browser.window_handles[1])
    x = int(browser.find_element(By.ID, "input_value").text)
    input = browser.find_element(By.ID, "answer").send_keys(calc(x))
    button1 = browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    addToClipBoard = (browser.switch_to.alert.text).split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    browser.switch_to.alert.accept()

finally:
    time.sleep(10)
    browser.quit()
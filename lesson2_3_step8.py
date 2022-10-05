import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import math
import pyperclip

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button = browser.find_element(By.ID, "book").click()

    x = int(browser.find_element(By.ID, "input_value").text)
    input = browser.find_element(By.ID, "answer").send_keys(calc(x))
    button1 = browser.find_element(By.ID, "solve").click()

    addToClipBoard = (browser.switch_to.alert.text).split(': ')[-1]
    pyperclip.copy(addToClipBoard)
    browser.switch_to.alert.accept()

finally:
    time.sleep(5)
    browser.quit()
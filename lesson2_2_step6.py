from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = int(browser.find_element(By.ID, "input_value").text)

    browser.execute_script("window.scrollBy(0, 150);")
    input = browser.find_element(By.ID, "answer").send_keys(calc(x))
    notRobot = browser.find_element(By.ID, "robotCheckbox").click()
    robotsRule = browser.find_element(By.ID, "robotsRule").click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = " https://suninjuly.github.io/math.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)
    robot = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    robot.click()
    robot_rule = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    robot_rule.click()
    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
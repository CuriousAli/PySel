from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

link = "http://suninjuly.github.io/file_input.html"
directory = "C:/Users/user/Desktop"
file_name = "upload.txt"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_name = browser.find_element(By.NAME, 'firstname').send_keys('AAAAAA')
    input_name = browser.find_element(By.NAME, 'lastname').send_keys('AAAAAABBBBB')
    input_name = browser.find_element(By.NAME, 'email').send_keys('AAAAAA@aaaa.com')

    file_path = os.path.join(directory, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "[type='submit']").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
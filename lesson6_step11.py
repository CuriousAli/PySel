from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
    input3.send_keys("pochta@dasds.com")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block input.first")
    input4.send_keys("777777777")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block input.second")
    input5.send_keys("Tr.Kemer.")

    # Отправляем заполненную форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class Test_Remastered(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("pochta@dasds.com")
        input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("777777777")
        input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
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

        try:
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text )

        finally:
            browser.quit()

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input")
        input3.send_keys("pochta@dasds.com")
        input4 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input")
        input4.send_keys("777777777")
        input5 = browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input")
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

        try:
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text )

        finally:
            browser.quit()


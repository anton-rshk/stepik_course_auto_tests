from asyncio import log
from cmath import sin
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import os

link = "https://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys('Anton')

    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys('Babin')

    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys('Babin')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'test.txt')
    print(file_path)

    input4 = browser.find_element(By.ID, 'file')
    input4.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

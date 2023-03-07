from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


def calc(x):
    return math.log(abs(12*math.sin(x)))


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
    alert = browser.switch_to.alert
    alert.accept()

    x_element = browser.find_element(By.ID, 'input_value')
    x = int(x_element.text)
    result = calc(x)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

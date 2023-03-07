from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()


def calc(x):
    return str(math.log(abs(12 * math.sin(x))))


browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = browser.find_element(By.ID, "book")
price = WebDriverWait(browser, 13).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)
button.click()

x_element = browser.find_element(By.ID, 'input_value')
x = int(x_element.text)
result = calc(x)

input = browser.find_element(By.ID, "answer")
input.send_keys(result)

send_button = browser.find_element(By.ID, "solve")
send_button.click()

time.sleep(10)

browser.quit()

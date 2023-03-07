from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1_element = browser.find_element(By.ID, 'num1')
    num1 = num1_element.text
    num2_element = browser.find_element(By.ID, 'num2')
    num2 = num2_element.text
    result = int(num1) + int(num2)

    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(result)).click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

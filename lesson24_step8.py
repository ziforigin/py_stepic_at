import math
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    price = WebDriverWait(browser, 12).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100"))
    button = browser.find_element_by_id("book")
    button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))



    input_value = browser.find_element_by_id("input_value").text
    result = calc(input_value)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)
    submit_btn = browser.find_element_by_css_selector("button[type=\"submit\"]")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
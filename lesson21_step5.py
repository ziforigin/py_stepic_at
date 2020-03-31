import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    formula = browser.find_element_by_id("input_value").text

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    result = calc(formula)
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(result)

    radiobtn = browser.find_element_by_css_selector(".form-check-input[value=\"robots\"]")
    radiobtn.click()
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    button = browser.find_element_by_css_selector(".btn.btn-default[type=\"submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
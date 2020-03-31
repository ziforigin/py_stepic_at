import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/execute_script.html"

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
    browser.execute_script("return arguments[0].scrollIntoView(true);", radiobtn)
    radiobtn.click()
    checkbox = browser.find_element_by_id("robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    button = browser.find_element_by_css_selector(".btn.btn-primary[type=\"submit\"]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
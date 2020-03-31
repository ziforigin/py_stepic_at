import math
from selenium import webdriver
import time

link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    magical_journey = browser.find_element_by_css_selector("button[type=\"submit\"]")
    magical_journey.click()
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
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
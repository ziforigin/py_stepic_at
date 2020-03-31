import os
from selenium import webdriver
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'somefile.txt')
    first_name = browser.find_element_by_css_selector("input[name=\"firstname\"]")
    first_name.send_keys("Ivan")
    last_name = browser.find_element_by_css_selector("input[name=\"lastname\"]")
    last_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector("input[name=\"email\"]")
    email.send_keys("Smolensk")
    upload_btn = browser.find_element_by_id("file")
    upload_btn.send_keys(file_path)
    submit_btn = browser.find_element_by_css_selector("button.btn")
    submit_btn.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

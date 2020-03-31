from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    num1str = num1.text
    num2str = num2.text
    sum = int(num1str) + int(num2str)
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(sum))  # ищем элемент с текстом "Python"
    button = browser.find_element_by_css_selector(".btn.btn-default[type=\"submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(7)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
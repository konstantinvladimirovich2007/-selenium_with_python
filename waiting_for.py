import math
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 13).until(
            EC.text_to_be_present_in_element ((By.ID, "price"), "100")
        )

    browser.find_element_by_id("book").click()

    number = browser.find_element_by_id("input_value").text
    x = int(number)
    res = str(math.log(abs(12 * math.sin(x))))

    answer = browser.find_element_by_css_selector("[type='text']").send_keys(res)
    button = browser.find_element_by_css_selector("[type='submit']").click()

finally:
    time.sleep(5)
    browser.quit()
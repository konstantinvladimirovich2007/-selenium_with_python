from selenium import webdriver
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_one(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(".first_block input[class='form-control first']")
        first_name.send_keys("1")

        last_name = browser.find_element_by_css_selector(".first_block input[class='form-control second']")
        last_name.send_keys("2")

        email = browser.find_element_by_css_selector(".first_block input[class='form-control third']")
        email.send_keys("3")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "IT'S OK")
        browser.quit()

    def test_two(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(".first_block input[class='form-control first']")
        first_name.send_keys("1")

        last_name = browser.find_element_by_css_selector(".first_block input[class='form-control second']")
        last_name.send_keys("2")

        email = browser.find_element_by_css_selector(".first_block input[class='form-control third']")
        email.send_keys("3")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "NO BRO, FAILED")
        browser.quit()


if __name__ == "__main__":
    unittest.main()
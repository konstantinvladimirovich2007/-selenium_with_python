import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_is_exist(browser):
    browser.get(link)
    time.sleep(3)
    submit = browser.find_element_by_xpath("//button[contains(@class, 'btn-add-to-basket')]").is_displayed()

    time.sleep(3)
    assert submit == True, "Button is exist"

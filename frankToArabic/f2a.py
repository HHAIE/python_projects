from selenium.webdriver.common.by import By
import time


def f2a(browser, text):
    browser.switch_to.default_content()
    text_area = browser.find_element(By.ID, "editor_ifr")
    browser.switch_to.frame(text_area)
    text_element = browser.find_element(By.TAG_NAME, "p")
    text_element.clear()
    time.sleep(0.5)
    
    text_element.send_keys(text + " ")

    time.sleep(1)
    text_element = browser.find_element(By.TAG_NAME, "p")
    return text_element.text


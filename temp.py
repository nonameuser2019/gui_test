from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import time
def temp():
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(5)
    browser.get('https://qa.platform.masterservice.company/')
    browser.execute_script("window.scrollBy(0, 200)", "")
    block = browser.find_element(By.CSS_SELECTOR, '.header-block__title.text_header_s.text_700.text_uppercase')
    print(block)

temp()

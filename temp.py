from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

def temp():
    browser = webdriver.Chrome()
    browser.set_window_size(1920, 1080)
    browser.implicitly_wait(5)
    browser.get('https://qa.platform.masterservice.company/')
    assert browser.find_elements(By.CSS_SELECTOR, 'ul.header-desktop__nav>li')[0].text == 'О нас'


temp()

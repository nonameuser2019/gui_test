from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import date

# import time
# def temp():
#     browser = webdriver.Chrome()
#     browser.set_window_size(1920, 1080)
#     browser.implicitly_wait(5)
#     browser.get('https://qa.platform.masterservice.company/')
#     button = browser.find_element(By.CSS_SELECTOR, 'button.subscribe__button__')
#     print(button)
#
# temp()
current_date = date.today()
print(current_date.strftime('%d'))
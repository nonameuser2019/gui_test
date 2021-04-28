from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import date
from pages.basket_page import *
import re

wrong_price = '6 950 грн.'

correct_price = ''.join(re.findall(r'[\d+]', wrong_price))
print(correct_price)


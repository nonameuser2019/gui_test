from pages.basket_page import BasketPage
from pages.checkout_page import CheckOut
from pages.locators import *
from selenium import webdriver
import time
import pytest

def test_chek_possibility_to_contatacts_tab(browser: webdriver.Chrome):
    page = CheckOut(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.setup_checkout()
    page.checkout_continue()
    assert page.get_active_tab_name() == '2.контактные данные', f'Wrong active tab your active tab is {page.get_active_tab_name()}'

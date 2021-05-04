from pages.basket_page import BasketPage
from pages.checkout_page import CheckOut
from pages.locators import *
from selenium import webdriver
import time
import pytest


@pytest.mark.smoke
def test_chek_possibility_to_contatacts_tab(browser: webdriver.Chrome):
    page = CheckOut(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.setup_checkout()
    page.checkout_continue()
    assert page.get_active_tab_name() == '2.контактные данные', f'Wrong active tab your active tab is {page.get_active_tab_name()}'


@pytest.mark.smoke
def test_possibility_fill_contacts(browser:webdriver.Chrome):
    page = CheckOut(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.setup_checkout()
    page.checkout_continue()
    page.fill_name('Alex')
    page.fill_phone('685340603')
    page.fill_email('zhe.depotop@gmail.com')
    page.change_consignee_i_am()
    #page.user_agreement()
    page.click_on_area(*CheckOutLocators.CHECKBOX_TERMS)
    time.sleep(3)
    assert page.get_active_tab_name() == '3.доставка и оплатаэ', f'Wrong active tab your active tab is {page.get_active_tab_name()}'


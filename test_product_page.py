import pytest
from .pages.main_page import MainPage
from .pages.product_page import ProductPage
from .pages.locators import MainPageLocators
from selenium import webdriver


@pytest.mark.test
def test_add_product_to_bag(browser: webdriver.Chrome):
    product_url = 'https://qa.platform.masterservice.company/258112'
    page = ProductPage(browser, product_url)
    page.open()
    page.add_product_to_card(browser)

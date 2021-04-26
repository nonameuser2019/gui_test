import pytest
from .pages.main_page import MainPage
from .pages.product_cart import ProductPage
from .pages.locators import MainPageLocators
from selenium import webdriver


class TestProductPage(ProductPage):
    product_url = 'https://qa.platform.masterservice.company/258112'
    @pytest.mark.test
    def test_add_product_to_bag(self, browser: webdriver.Chrome):
        page = ProductPage(browser, self.product_url)
        page.open()
        page.add_product_to_card(browser)

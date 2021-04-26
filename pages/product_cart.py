from .base_page import BasePage
from .locators import ProductPageLocator
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class ProductPage(BasePage):

    def add_product_to_card(self, browser: webdriver.Chrome):
        button_add = browser.find_element(*ProductPageLocator.BUTTON_BUY)
        button_add.click()
        text_button = browser.find_element(*ProductPageLocator.BUTTON_BUY_TEXT).text
        assert text_button == 'В корзине', f'The product is not in the product card'
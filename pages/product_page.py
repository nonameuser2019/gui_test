from pages.base_page import BasePage
from .locators import ProductPageLocator
from selenium import webdriver


class ProductPage(BasePage):

    def add_product_to_card(self, browser: webdriver.Chrome):
        button_add = browser.find_element(*ProductPageLocator.BUTTON_BUY)
        condition = button_add.get_attribute('disabled')
        if condition:
            print(f'Product is not avalible')
            assert not condition
        else:
            button_add.click()
        condition = button_add.get_attribute('disabled')
        assert condition, f'The product is not in the product card'


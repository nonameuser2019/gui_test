from pages.base_page import BasePage
from pages.locators import BasketPageLocator, ProductPageLocator
from selenium import webdriver
import re


class BasketPage(BasePage):
    def basket_is_empty(self, browser: webdriver.Chrome):
        self.open_basket()
        empty_text = browser.find_element(*BasketPageLocator.EMPTY_BUTTON_TEST)
        assert 'нет товаров' in empty_text.text.lower(), f'product basket is not empty'


    def add_product_count(self):
        plus_btn = self.browser.find_element(*BasketPageLocator.COUNT_ITEM_BTN)
        plus_btn.click()


    def get_product_count(self, browser:webdriver.Chrome):
        product_count = browser.find_element(*BasketPageLocator.PRODUCT_COUNT_VALUE)
        return product_count.text


    def reduce_count(self):
        reduce_btn = self.browser.find_element(*BasketPageLocator.REDUCE_ITEM_BTN)
        reduce_btn.click()

    def get_price(self):
        basket_price = self.browser.find_element(*BasketPageLocator.PRICE_ITEM).text
        return int(''.join(re.findall(r'[\d+]', basket_price)))

    def get_total_sum(self):
        total_sum = self.browser.find_element(*BasketPageLocator.ORDER_TOTAL).text
        return int(''.join(re.findall(r'[\d+]', total_sum)))

    def delete_product(self):
        delete_btn = self.browser.find_element(*BasketPageLocator.DELETE_ITEM_BTN)
        delete_btn.click()
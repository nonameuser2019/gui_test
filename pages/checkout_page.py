from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.locators import BasketPageLocator, ProductPageLocator, CheckOutLocators
from selenium import webdriver
import re


class CheckOut(ProductPage):

    def setup_checkout(self, browser: webdriver.Chrome):
        self.add_product_to_card()
        check_out_btn = browser.find_element(*BasketPageLocator.CHECK_OUT_ORDER_BTN)
        check_out_btn.click()

    def checkout_continue(self):
        checkout_continue_btn = self.browser.find_element(*CheckOutLocators.CHECKOUT_ORDER_CONFIRM)
        checkout_continue_btn.click()

    def search_product(self, search_key):
        search_field = self.browser.find_element(*CheckOutLocators.PRODUCT_SEARCH_FIELD)
        search_field.send_keys(search_key)

    def add_product_count(self, count):
        add_product_btn = self.browser.find_element(*CheckOutLocators.ADD_COUNT_ITEM)
        for i in range(count):
            add_product_btn.click()

    def reduce_product_count(self, count):
        reduce_product_btn = self.browser.find_element(*CheckOutLocators.REDUCE_COUNT_ITEM)
        for i in range(count):
            reduce_product_btn.click()

    def delete_product(self):
        delete_btn = self.browser.find_element(*CheckOutLocators.DELETE_ITEM_BTN)
        delete_btn.click()

    def fill_name(self, name):
        name_field = self.browser.find_element(*CheckOutLocators.NAME_FIELD)
        name_field.send_keys(name)

    def fill_phone(self, phone_number):
        phone_field = self.browser.find_element(*CheckOutLocators.PHONE_FIELD)
        phone_field.send_keys(phone_number)

    def fill_email(self, email):
        email_field = self.browser.find_element(*CheckOutLocators.EMAIL_FIELD)
        email_field.send_keys(email)

from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.locators import BasketPageLocator, ProductPageLocator, CheckOutLocators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
import re
import time

class CheckOut(ProductPage):

    def setup_checkout(self):
        self.add_product_to_card()
        self.open_basket()
        check_out_btn = self.browser.find_element(*BasketPageLocator.CHECK_OUT_ORDER_BTN)
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

    def change_consignee_i_am(self):
        i_am_radio_btn = self.browser.find_element(*CheckOutLocators.RADIO_BTN_IAM)
        i_am_radio_btn.click()

    def change_consignee_other_person(self):
        other_person_redio_btn = self.browser.find_element(*CheckOutLocators.RADIO_BTN_OTHER_PEOPLE)
        other_person_redio_btn.click()

    def get_active_tab_name(self):
        active_name = self.browser.find_element(*CheckOutLocators.ACTIVE_TAB_TITLE).text
        return active_name.lower()

    def user_agreement(self):
        user_agreement_check_box = self.browser.find_element(*CheckOutLocators.CHECKBOX_TERMS)
        user_agreement_check_box.click()

    def click_on_area(self, how, what):
        click_element = self.browser.find_element(how, what)
        elem_location = click_element.location
        x = elem_location['x'] + 3
        y = elem_location['y'] + 3
        actions = ActionChains(self.browser)
        actions.move_by_offset(x, y)
        time.sleep(1)
        actions.click()





from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import math
from pages.locators import MainPageLocators, ProductPageLocator


class BasePage():
    def __init__(self, browser: webdriver.Chrome, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        except:
            return False
        return True

    def open(self):
        self.browser.get(self.url)

    def move_to_element(self, how, what):
        element = self.browser.find_element(how, what)
        webdriver.ActionChains(self.browser).move_to_element(element).perform()

    def click_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def check_title(self, how, what, title):
        get_title = self.browser.find_element(how, what).text
        assert get_title == title, 'Title incorrect'


    def add_product_to_basket(self, how, what):
        add_to_basket_btn = self.browser.find_element(how, what)
        add_to_basket_btn.click()


    def get_product_price(self, how, what):
        product_price = self.browser.find_element(how, what)
        return product_price.text

    def open_basket(self):
        basket_btn = self.browser.find_element(*MainPageLocators.LINK_BAG_HEADER)
        basket_btn.click()


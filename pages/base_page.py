from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import MainPageLocators


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

    def move_to_element(self):
        element = self.browser.find_element(*MainPageLocators.CUSTOMERS_LINK)
        webdriver.ActionChains(self.browser).move_to_element(element).perform()

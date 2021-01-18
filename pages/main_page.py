from .base_page import BasePage
from .locators import MainPageLocators
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_by_link_about_us(self, browser:webdriver.Chrome, index, messages):
        assert self.browser.find_elements(*MainPageLocators.LEFT_HEADER_MENU_list)[index].text == messages,\
               f'Link about us in header top menu does not exist, menu has link: ' \
            f'{browser.find_elements(*MainPageLocators.LEFT_HEADER_MENU_list)[0].text}'



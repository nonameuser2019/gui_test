from .base_page import BasePage
from .locators import MainPageLocators
from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def should_by_link_left_header(self, browser: webdriver.Chrome, index, messages):
        assert self.browser.find_elements(*MainPageLocators.LEFT_HEADER_MENU_list)[index].text == messages, \
            f'Link about us in header top menu does not exist, menu has link: ' \
            f'{browser.find_elements(*MainPageLocators.LEFT_HEADER_MENU_list)[0].text}'

    def should_by_link_in_customers_drop_down(self, browser: webdriver.Chrome, index, messages):
        assert self.browser.find_elements(*MainPageLocators.CUSTOMERS_LINK_LIST[index].text) == messages, \
            f'Link: {messages} does not found in customers list in header left-top menu'

    def should_by_title_in_block_choice_auto(self, browser: webdriver.Chrome):
        assert self.browser.find_element(
            *MainPageLocators.TITLE_BLOCK_CHOICE_CAR).text == 'НАЧНИТЕ С ВЫБОРА АВТОМОБИЛЯ', \
            f'Wrong title in title block of choise auto'

    def should_by_subtitle_in_block_choice_auto(self, browser: webdriver.Chrome):
        assert self.browser.find_element(
            *MainPageLocators.SUBTITLE_BLOCK_CHOICE_CAR).text == 'Выбор автомобиля позволяет отобразить только те запчасти, которые подходят к вашему автомобилю', \
        'Wrong subtitle in block choice auto'

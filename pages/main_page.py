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
        assert self.browser.find_elements(*MainPageLocators.CUSTOMERS_LINK_LIST)[index].text == messages, \
            f'Link: {messages} does not found in customers list in header left-top menu'

    def should_by_title_in_block_choice_auto(self, browser: webdriver.Chrome):
        assert self.browser.find_element(
            *MainPageLocators.TITLE_BLOCK_CHOICE_CAR).text == 'НАЧНИТЕ С ВЫБОРА АВТОМОБИЛЯ', \
            f'Wrong title in title block of choise auto'

    def should_by_subtitle_in_block_choice_auto(self, browser: webdriver.Chrome):
        assert self.browser.find_element(
            *MainPageLocators.SUBTITLE_BLOCK_CHOICE_CAR).text == 'Выбор автомобиля позволяет отобразить только те запчасти, которые подходят к вашему автомобилю', \
        'Wrong subtitle in block choice auto'


    def should_be_title_block_actual_action(self, browser: webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.TITLE_BLOCK_ACTUAL_ACTIONS).text == 'АКТУАЛЬНЫЕ АКЦИИ',\
        'Wrong title in block Actual news'


    def should_be_link_to_list_all_news_block_actual_action(self, browser: webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.LINK_TO_ALL_NEWS_BLOCK_ACTUAL_ACTIONS).text == 'К списку всех акций',\
        'Wrong text of link to list all action'


    def should_be_title_in_block_popular_services(self, browser:webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.TITLE_POPULAR_SERVICESES).text == 'ПОПУЛЯРНЫЕ УСЛУГИ',\
        'Wrong title in block Popular services'


    def should_be_link_to_all_services_block_popular_services(self, brwoser:webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.LINK_TO_ALL_SERVICES_BLOCK_POPULAR_SERVICES).text == 'К списку всех услуг', \
        'Wrong text of link to list popular serveces'


    def should_be_title_block_feedback(self, browser:webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.TITLE_FEEDBACK).text == 'ОТЗЫВЫ КЛИЕНТОВ', \
        'Wrong title of block feedbacks clients'


    def should_be_link_to_all_feedbacks(self, browser):
        assert self.browser.find_element(*MainPageLocators.LINK_TO_ALL_FEEDBACKS).text == 'К списку всех отзывов', \
        'Wrong text of link to all feedbacks'


    def should_be_title_block_useful_articles(self, browser:webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.TITLE_BLOCK_USEFUL_ARTICLES).text == 'ПОЛЕЗНЫЕ СТАТЬИ', \
        'The title is wrong in block of usual articles'


    def should_be_link_to_all_articles(self, browser:webdriver.Chrome):
        assert self.browser.find_element(*MainPageLocators.LINK_TO_ALL_LIST_ARTICLES).text == 'К списку всех новостей', \
        'The link all articlse has wrong text'



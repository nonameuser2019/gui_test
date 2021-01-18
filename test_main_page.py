from selenium import webdriver
import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
import time

@pytest.mark.parametrize('index, messages', [(0, 'О нас'), (1, 'Покупателям'), (2, 'Сотрудничество'), (3, 'АвтоГид'), (4, 'Акции'), (5, 'Контакты')])
def test_check_about_us_in_header_top_menu(browser, index, messages):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_by_link_about_us(browser, index, messages)

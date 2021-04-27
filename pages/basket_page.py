from pages.base_page import BasePage
from pages1.locators import BasketPageLocator
from selenium import webdriver


class BasketPage(BasePage):
    def basket_is_empty(self, browser: webdriver.Chrome):
        self.open_basket()
        empty_text = browser.find_element(*BasketPageLocator.EMPTY_BUTTON_TEST)
        assert 'нет товаров' in empty_text.text.lower(), f'product basket is not empty'

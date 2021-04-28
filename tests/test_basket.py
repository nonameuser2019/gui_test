from pages.basket_page import BasketPage
from pages.locators import MainPageLocators, ProductPageLocator, BasketPageLocator
from selenium import webdriver
import time
import pytest


def test_check_bag_is_empty(browser: webdriver.Chrome):
    # при открытии сайта корзина пустая
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.basket_is_empty(browser)


def test_check_adding_product_to_basket(browser: webdriver.Chrome):
    # проверям что цена соответствует цене в карточке
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    product_price = page.get_product_price(*ProductPageLocator.PRODUCT_PRICE)
    page.open_basket()
    time.sleep(0.5)
    basket_price = browser.find_element(*BasketPageLocator.PRICE_ITEM).text
    assert product_price in basket_price, f'Wrong price actual price is {basket_price}'


def test_click_btn_checkout_order(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.click_button(*BasketPageLocator.CHECK_OUT_ORDER_BTN)
    assert browser.current_url == BasketPageLocator.CHECKOUT_URL, f'Do not redirect to checkout page'


def test_add_one_more_product(browser: webdriver.Chrome):
    # добавить 2 товара в корзину
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '5028837')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    product_list = browser.find_elements(*BasketPageLocator.PRODUCT_LIST_BASKET)
    assert len(product_list) == 2, 'Wrong count of product in basket'



def test_check_add_count_product_in_basket(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.add_product_count()
    basket_price = page.get_price()
    product_count = int(page.get_product_count(browser))
    total_sum = page.get_total_sum()
    assert product_count == 2, 'Wrong count goods in basket'
    assert (product_count * basket_price) == total_sum, 'Wrong total sum of order'


def test_check_reduce_count_product_in_basket(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.add_product_count()
    page.add_product_count()
    page.reduce_count()
    assert page.get_product_count(browser) == '2', 'Wrong count goods in basket'


def test_check_delete_all_product(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.delete_product()
    assert browser.current_url != BasketPageLocator.CHECKOUT_URL, 'Is imposiible redirect to checkout page without any goods '


def test_check_posibility_delete_product(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '5028837')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.delete_product()
    product_list = browser.find_elements(*BasketPageLocator.PRODUCT_LIST_BASKET)
    assert len(product_list) == 1, 'Wrong count of product in basket'


@pytest.mark.test
@pytest.mark.xfail
def test_check_possibility_checkout_order_with_empty_bag(browser: webdriver.Chrome):
    page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
    page.open()
    page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
    page.open_basket()
    page.delete_product()
    page.click_button(*BasketPageLocator.CHECK_OUT_ORDER_BTN)
    assert browser.current_url == BasketPageLocator.CHECKOUT_URL, f'Do not redirect to checkout page'



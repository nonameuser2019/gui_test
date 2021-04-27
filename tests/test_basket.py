from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from selenium import webdriver


# def test_check_bag_is_empty(browser: webdriver.Chrome):
#     page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL)
#     page.open()
#     page.basket_is_empty(browser)
#
#
# def test_check_adding_product_to_basket(browser: webdriver.Chrome):
#     # проверям что цена соответствует цене в карточке
#     page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL + '282799')
#     page.open()
#     page.add_product_to_basket(*ProductPageLocator.BUTTON_BUY)
#     product_price = page.get_product_price(*ProductPageLocator.PRODUCT_PRICE)
#     page.open_basket()
#     time.sleep(0.5)
#     basket_price = browser.find_element(*BasketPageLocator.PRICE_ITEM).text
#     assert product_price in basket_price, f'Wrong price actual price is {basket_price}'


class TestBasket(BasketPage):
    def test_check_bag_is_empty(self, browser: webdriver.Chrome):
        page = BasketPage(browser, MainPageLocators.MAIN_PAGE_URL)
        page.open()
        page.basket_is_empty(browser)




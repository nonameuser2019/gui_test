from selenium import webdriver
import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
import time

@pytest.mark.parametrize('index, messages', [(0, 'О нас'), (1, 'Покупателям'), (2, 'Сотрудничество'), (3, 'АвтоГид'),
                                             (4, 'Акции'), (5, 'Контакты')])
def test_check_about_us_in_header_top_menu(browser, index, messages):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_by_link_left_header(browser, index, messages)

@pytest.mark.n
@pytest.mark.parametrize('index, messages', [(0, 'Отзывы о компании')])
# тест не работает, доделать на свежую голову
def test_check_all_link_in_customers_dropdown_menu(browser, index, messages):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.move_to_element()
    page.should_by_link_in_customers_drop_down(browser, index, messages)


# проверка что элемент выбора валюты присутствоует на странице
def test_should_be_currency_dropdown(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_CURRENCY)


# проверка что элемент выбора языка присутствоует на странице
def test_should_be_language_dropdown(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_LANGUAGE)


# проверка наличия ссылки входа в лк
def test_should_be_link_personal_account(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_PERSONAL_ACCOUNT)


# проверка наличия лого компангии в хедере
def test_should_be_companylogo(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LOGO_MAIN_PAGE)


# проверка наличия ссылки смены города
def test_should_be_change_city(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_CITY)


# првоерка наличия блока с номерами телефона в хедер
def test_should_be_block_contact_phones(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_PHONES_HEADER)


# проверка наличия поля поиска в хедер
def test_should_be_search_field_header(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.SEARCH_FIELD_HEADER)


# проверка наличия кнопки записаться на диагностику
def test_should_be_button_to_diagnostik(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BUTTON_TO_DIAGNOSTIC)


# проверка наличия кнопки сравнение в хедер
def test_should_be_link_comparison(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_COMPAIRSON_HEADER)


# проверка наличия кнопки избранное в хедер
def test_should_be_link_favorites(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_FAFORITES_HEADER)


# проверка наличия ссылки корзины в хедер
def test_should_be_link_bag(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_BAG_HEADER)


#проверка наличия иконки корзины покупок
def test_should_be_image_shopping_cart(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.IMAGE_SHOPPING_CART)


# проверка наличия блока карусели на главной
def test_should_be_block_carousel(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_CAROUSEL)


# проверка наличия блока баннер в карусели
def test_should_be_banner_in_carousel(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_BANNER_IN_CAROUSEL)


# проверка наличия блока выбора автомобиля
def test_should_be_block_choise_car(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_CHOICE_CAR)


# проверка title блока выбор автомобиля
def test_check_title_in_block_choice_auto(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    browser.execute_script("window.scrollBy(0, 200)", "")
    page.should_by_title_in_block_choice_auto(browser)


# проверка subtitle блока выбора авто
def test_check_subtitle_in_block_choice_auto(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_by_subtitle_in_block_choice_auto(browser)


@pytest.mark.test
def test_should_be_block_actual_news(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_ACTUAL_NEWS)






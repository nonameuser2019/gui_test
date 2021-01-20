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


# проверка наличия иконки корзины покупок
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


# проверка наличия блока актуальные акции
def test_should_be_block_actual_action(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_ACTUAL_ACTIONS)


# проверка тайтла блока актуальные акции
def test_check_title_in_block_actual_action(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_title_block_actual_action(browser)


# проверка ссылки к списку всех акций
def test_check_link_to_all_actions_block_actual_actions(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_link_to_list_all_news_block_actual_action(browser)


# проверка наличия блока каталог товаров
def test_should_be_block_catalog_of_goods(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_CATALOG_OF_GOODS)

# проверка наличия блока популярные услуги
def test_should_be_block_popular_services(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_POPULAR_SERVICES)


# проверка тайтла блока популярные услуги
def test_check_title_in_block_popular_services(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_title_in_block_popular_services(browser)


@pytest.mark.xfail
# проверка ссылки к списку всех услуг
def test_check_link_to_list_all_services_in_block_popular_services(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_link_to_all_services_block_popular_services()


# Проверка наличия блока подписаться на нас
def test_should_be_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_SUBSCRIBE)


# Првоерка наличия текстового поля в блоке подписатьтся на нас
def test_should_be_text_inp_in_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.TEXT_INPUT_SUBSCRIBE)


# проверка наличия кнопка подписаться в блоке подписаться на нас
def test_should_be_button_subscribe_in_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BUTTON_SUBSCRIBE)


# проверка наличия блока отзывы клиентов
def test_should_be_block_feedback(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_FEEDBACK)


# проверка тайтл блока отзывы клиентов
def test_check_title_block_feedback(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_title_block_feedback(browser)


# проверка сслки к списку все отзывов
def test_check_link_to_all_feedbacs(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_link_to_all_feedbacks(browser)


# проверка наличия блока полезные статьи
def test_should_be_block_useful_articles(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_USEFUL_ARTICLES)


# Прверка тайтла блока полезные статьи
def test_check_title_block_useful_articles(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_title_block_useful_articles(browser)


# проверка ссылки к списку всех новостей
def test_check_link_to_all_articles_block_useful_articles(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_be_link_to_all_articles(browser)


# проверка наличия блока о компании(мастер сервис разборка)
def test_should_be_block_about_company(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_ABOUT_US)


# проверка наличия блока контактов в футер
def test_should_be_block_cotacts_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_FOOTER_CONTACTS)


@pytest.mark.test
# проверка наличия логотипа компания в футер
def test_should_be_logo_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_LOGO)










from selenium import webdriver
import pytest
from .pages.main_page import MainPage
from .pages.locators import MainPageLocators
import time


@pytest.mark.parametrize('index, messages', MainPageLocators.LINK_LIST_IN_HEADER_TOP)
@pytest.mark.smoke
def test_check_all_link_in_header_top_menu(browser, index, messages):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.should_by_link_left_header(browser, index, messages)


@pytest.mark.smoke
@pytest.mark.parametrize('index, messages', MainPageLocators.LINK_LIST_DROPDOWN_HEADER)
# проверка всех ссылок в выпадающем меню покупателям в хедер
def test_check_all_link_in_customers_dropdown_menu(browser, index, messages):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.move_to_element()
    page.should_by_link_in_customers_drop_down(browser, index, messages)


@pytest.mark.smoke
# проверка что элемент выбора валюты присутствоует на странице
def test_should_be_currency_dropdown(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_CURRENCY)


@pytest.mark.smoke
# проверка что элемент выбора языка присутствоует на странице
def test_should_be_language_dropdown(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_LANGUAGE)


@pytest.mark.smoke
# проверка наличия ссылки входа в лк
def test_should_be_link_personal_account(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_PERSONAL_ACCOUNT)


@pytest.mark.smoke
# проверка наличия лого компании в хедере
def test_should_be_companylogo(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LOGO_MAIN_PAGE)


@pytest.mark.smoke
# проверка наличия ссылки смены города
def test_should_be_change_city(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.DROPDOWN_CHANGE_CITY)


@pytest.mark.smoke
# првоерка наличия блока с номерами телефона в хедер
def test_should_be_block_contact_phones(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_PHONES_HEADER)


@pytest.mark.smoke
# проверка наличия поля поиска в хедер
def test_should_be_search_field_header(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.SEARCH_FIELD_HEADER)


@pytest.mark.smoke
# проверка наличия кнопки записаться на диагностику
def test_should_be_button_to_diagnostik(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BUTTON_TO_DIAGNOSTIC)


@pytest.mark.smoke
# проверка наличия кнопки сравнение в хедер
def test_should_be_link_comparison(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_COMPAIRSON_HEADER)


@pytest.mark.smoke
# проверка наличия кнопки избранное в хедер
def test_should_be_link_favorites(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_FAFORITES_HEADER)


@pytest.mark.smoke
# проверка наличия ссылки корзины в хедер
def test_should_be_link_bag(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.LINK_BAG_HEADER)


@pytest.mark.smoke
# проверка наличия иконки корзины покупок
def test_should_be_image_shopping_cart(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.IMAGE_SHOPPING_CART)


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
# проверка наличия блока каталог товаров
def test_should_be_block_catalog_of_goods(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_CATALOG_OF_GOODS)

@pytest.mark.smoke
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


@pytest.mark.smoke
# Проверка наличия блока подписаться на нас
def test_should_be_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_SUBSCRIBE)


@pytest.mark.smoke
# Првоерка наличия текстового поля в блоке подписатьтся на нас
def test_should_be_text_inp_in_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.TEXT_INPUT_SUBSCRIBE)


@pytest.mark.smoke
# проверка наличия кнопка подписаться в блоке подписаться на нас
def test_should_be_button_subscribe_in_block_subscribe(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BUTTON_SUBSCRIBE)


@pytest.mark.smoke
# проверка наличия блока отзывы клиентов
def test_should_be_block_feedback(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_FEEDBACK)


@pytest.mark.smoke
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


@pytest.mark.smoke
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


@pytest.mark.smoke
# проверка наличия блока о компании(мастер сервис разборка)
def test_should_be_block_about_company(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_ABOUT_US)


@pytest.mark.smoke
# проверка наличия блока контактов в футер
def test_should_be_block_cotacts_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.BLOCK_FOOTER_CONTACTS)


@pytest.mark.smoke
# проверка наличия логотипа компания в футер
def test_should_be_logo_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_LOGO)


@pytest.mark.smoke
# проверка наличия блока социальных сетей в футере
def test_should_be_block_social_networks_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_SOCIAL_NETWORK_BLOCK)


@pytest.mark.test
# проверка наличия иконки facebook в футер
def test_should_be_facebook_icon_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.is_element_present(*MainPageLocators.FOOTER_FACEBOOK_ICON)


@pytest.mark.test
# проверка наличия иконки youtube в футер
def test_should_be_youtube_icon_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.is_element_present(*MainPageLocators.FOOTER_YOUTUBE_ICON)

@pytest.mark.test
# проверка наличия иконки instagram в футер
def test_should_be_insta_icon_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.is_element_present(*MainPageLocators.FOOTER_INSTA_ICON)


@pytest.mark.smoke
# проверка наличия блока контакты в футер
def test_should_be_block_contacts_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_CONTACTS_BLOCK)


@pytest.mark.smoke
# проверка наличия блока график работы в футер
def test_should_be_block_shedule_work_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_SHEDULE_WORK_BLOCK)


@pytest.mark.smoke
# проверка наличия блока метода оплаты в футер
def test_should_be_block_pays_method_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_PAYS_METHOD_BLOCK)


# проверка наличия блока с ссылками в нижней части футера
def test_should_be_block_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_BLOCK)


# проверка наличия блока информация в нижней части футера первый блок
def test_should_be_block_information_first_in_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_INFORMATION_BLOCK_FIRST)


# проверка наличия блока информация в нижней части футера второй блок
def test_should_be_block_information_second_in_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_INFORMATION_BLOCK_SECOND)


# проверка наличия блока товары в нижней части футера
def test_should_be_block_goods_in_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_GOODS_BLOCK)


# проверка наличия блока ремонт автомобиля в нижней части футера
def test_should_be_block_repair_car_in_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_REPAIR_CAR_BLOCK)


# проверка наличия блока ремонт агрегатов в нижней части футера
def test_should_be_block_repair_agregates_in_footer_nav(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_NAV_REPAIR_AGREGATE_BLOCK)


@pytest.mark.smoke
@pytest.mark.test
# проверка наличия блока копирайт
def test_should_be_block_copywrite_in_footer(browser):
    page = MainPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    assert page.is_element_present(*MainPageLocators.FOOTER_COPYWRITE_BLOCK)

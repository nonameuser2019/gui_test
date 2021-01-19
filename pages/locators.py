from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_URL = 'https://qa.platform.masterservice.company/'
    LEFT_HEADER_MENU_list = (By.CSS_SELECTOR, 'ul.header-desktop__nav>li')
    CUSTOMERS_LINK_LIST = (By.CSS_SELECTOR, '.dropdown__items>a')
    CUSTOMERS_LINK = (By.CSS_SELECTOR, 'ul.header-desktop__nav>li:nth-child(2)')
    DROPDOWN_CHANGE_CURRENCY = (By.CSS_SELECTOR, '.header-desktop__dropdowns-group>span:nth-child(1)')
    DROPDOWN_CHANGE_LANGUAGE = (By.CSS_SELECTOR, '.header-desktop__dropdowns-group>span:nth-child(2)')
    LINK_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'a.header-desktop__nav-link.auth-btn')
    LOGO_MAIN_PAGE = (By.CSS_SELECTOR, '.contacts__logo')
    DROPDOWN_CHANGE_CITY = (By.CSS_SELECTOR, 'div.contacts__city')
    BLOCK_PHONES_HEADER = (By.CSS_SELECTOR, '.contacts__phone')
    SEARCH_FIELD_HEADER = (By.CSS_SELECTOR, 'div.contacts__search>div.form__block')
    BUTTON_TO_DIAGNOSTIC = (By.CSS_SELECTOR, '.contacts__button.button__primary_default')
    LINK_COMPAIRSON_HEADER = (By.CSS_SELECTOR, 'ul.menu-block__list._right>li:nth-child(1)')
    LINK_FAFORITES_HEADER = (By.CSS_SELECTOR, 'ul.menu-block__list._right>li:nth-child(2)')
    LINK_BAG_HEADER = (By.CSS_SELECTOR, 'ul.menu-block__list._right>li:nth-child(3)')
    IMAGE_SHOPPING_CART = (By.CSS_SELECTOR, 'div.cart-btn__container>i.ms-icon-shopping-cart')
    BLOCK_CAROUSEL = (By.CSS_SELECTOR, 'div.VueCarousel.main-slider__block')
    BLOCK_BANNER_IN_CAROUSEL = (By.CSS_SELECTOR, 'div.banner')
    BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, 'div.tabs-block.tabs-block_type_main-filter')
    TITLE_BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, '.header-block__title.text_header_s.text_700.text_uppercase')
    SUBTITLE_BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, '.header-block__subtitle')
    BLOCK_ACTUAL_NEWS = (By.CSS_SELECTOR, '#main-page>div._container>section:nth-child(4)')

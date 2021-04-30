from selenium.webdriver.common.by import By


class MainPageLocators():
    MAIN_PAGE_URL = 'https://qa.platform.masterservice.company/ru/'
    LINK_LIST_IN_HEADER_TOP = [(0, 'О нас'), (1, 'Покупателям'), (2, 'Сотрудничество'), (3, 'АвтоГид'),
                                             (4, 'Акции'), (5, 'Контакты')]
    LINK_LIST_DROPDOWN_HEADER = [(0, 'Отзывы о компании'), (1, 'Производители автозапчастей'), (2, 'Форум'),
                                 (3, 'Доставка и оплата'), (4, 'Гарантия и возврат'), (5, 'Вопросы и ответы')]
    LEFT_HEADER_MENU_list = (By.CSS_SELECTOR, 'ul.header__nav>li')
    CUSTOMERS_LINK_LIST = (By.CSS_SELECTOR, '.dropdown__items>a')
    CUSTOMERS_LINK = (By.CSS_SELECTOR, 'ul.header__nav>li:nth-child(2)')
    DROPDOWN_CHANGE_CURRENCY = (By.CSS_SELECTOR, '.header__dropdown-element:nth-child(1)')
    DROPDOWN_CHANGE_LANGUAGE = (By.CSS_SELECTOR, '.header__dropdown-element:nth-child(2)')
    LINK_PERSONAL_ACCOUNT = (By.CSS_SELECTOR, 'button.header__nav-link')
    LOGO_MAIN_PAGE = (By.CSS_SELECTOR, '.contacts__logo')
    DROPDOWN_CHANGE_CITY = (By.CSS_SELECTOR, 'div.contacts__city')
    BLOCK_PHONES_HEADER = (By.CSS_SELECTOR, '.contacts__phone')
    SEARCH_FIELD_HEADER = (By.CSS_SELECTOR, 'input[name="search"]')
    BUTTON_TO_DIAGNOSTIC = (By.CSS_SELECTOR, '.contacts__button.button__primary_default')
    LINK_COMPAIRSON_HEADER = (By.CSS_SELECTOR, 'ul.menu-block__list.menu-block__list_right>a:nth-child(1)')
    LINK_FAFORITES_HEADER = (By.CSS_SELECTOR, 'ul.menu-block__list.menu-block__list_right>a:nth-child(2)')
    LINK_BAG_HEADER = (By.CSS_SELECTOR, 'li.menu-block__item.cart-btn')
    IMAGE_SHOPPING_CART = (By.CSS_SELECTOR, 'div.cart-btn__container>i.ms-icon-shopping-cart')
    BLOCK_CAROUSEL = (By.CSS_SELECTOR, 'div.VueCarousel.main-slider__block')
    BLOCK_BANNER_IN_CAROUSEL = (By.CSS_SELECTOR, 'div.banner')
    BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, 'div.tabs-block.tabs-block_type_main-filter')
    TITLE_BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, '.header-block__title.text_header_s.text_700.text_uppercase')
    SUBTITLE_BLOCK_CHOICE_CAR = (By.CSS_SELECTOR, '.header-block__subtitle')
    BLOCK_ACTUAL_ACTIONS = (By.CSS_SELECTOR, '#car-catalog-trigger')
    TITLE_BLOCK_ACTUAL_ACTIONS = (By.CSS_SELECTOR, '#car-catalog-triggerh1')
    LINK_TO_ALL_NEWS_BLOCK_ACTUAL_ACTIONS = (By.CSS_SELECTOR, '#car-catalog-trigger>a')
    BLOCK_CATALOG_OF_GOODS = (By.CSS_SELECTOR, '.tabs-block.tabs-block_type_main-catalog')
    BLOCK_POPULAR_SERVICES = (By.CSS_SELECTOR, '#popular-services')
    TITLE_POPULAR_SERVICESE = (By.CSS_SELECTOR, '#popular-services>h1')
    LINK_TO_ALL_SERVICES_BLOCK_POPULAR_SERVICES = (By.CSS_SELECTOR, '#popular-services>a')
    BLOCK_SUBSCRIBE = (By.CSS_SELECTOR, 'section.subscribe-container')
    TEXT_INPUT_SUBSCRIBE = (By.CSS_SELECTOR, '.subscribe__input>input')
    BUTTON_SUBSCRIBE = (By.CSS_SELECTOR, 'button.subscribe__button')
    BLOCK_FEEDBACK = (By.CSS_SELECTOR, '#main-page>div._container>section:nth-child(1)')
    TITLE_FEEDBACK = (By.CSS_SELECTOR, '#main-page>div._container>section:nth-child(1)>div>div>h1')
    LINK_TO_ALL_FEEDBACKS = (By.CSS_SELECTOR, '#main-page>div._container>section:nth-child(1)>div>div>a')
    BLOCK_USEFUL_ARTICLES = (By.CSS_SELECTOR, '#useful-articles')
    TITLE_BLOCK_USEFUL_ARTICLES = (By.CSS_SELECTOR, '#useful-articles>h1')
    LINK_TO_ALL_LIST_ARTICLES = (By.CSS_SELECTOR, '#useful-articles>h1>a')
    BLOCK_ABOUT_US = (By.CSS_SELECTOR, '.about-container')
    BLOCK_FOOTER_CONTACTS = (By.CSS_SELECTOR, 'div.footer__block')
    FOOTER_LOGO = (By.CSS_SELECTOR, '.footer__logo')
    FOOTER_SOCIAL_NETWORK_BLOCK = (By.CSS_SELECTOR, '.footer__row._container>div:nth-of-type(1)')
    FOOTER_CONTACTS_BLOCK = (By.CSS_SELECTOR, '.footer__row._container>div:nth-of-type(2)')
    FOOTER_SHEDULE_WORK_BLOCK = (By.CSS_SELECTOR, '.footer__row._container>div:nth-of-type(3)')
    FOOTER_PAYS_METHOD_BLOCK = (By.CSS_SELECTOR, '.footer__row._container>div:nth-of-type(4)')
    FOOTER_NAV_BLOCK = (By.CSS_SELECTOR, '.footer__nav._container')
    FOOTER_NAV_INFORMATION_BLOCK_FIRST = (By.CSS_SELECTOR, '.footer__nav._container>nav:nth-child(1)')
    FOOTER_NAV_INFORMATION_BLOCK_SECOND = (By.CSS_SELECTOR, '.footer__nav._container>nav:nth-child(2)')
    FOOTER_NAV_GOODS_BLOCK = (By.CSS_SELECTOR, '.footer__nav._container>nav:nth-child(3)')
    FOOTER_NAV_REPAIR_CAR_BLOCK = (By.CSS_SELECTOR, '.footer__nav._container>nav:nth-child(4)')
    FOOTER_NAV_REPAIR_AGREGATE_BLOCK = (By.CSS_SELECTOR, '.footer__nav._container>nav:nth-child(5)')
    FOOTER_COPYWRITE_BLOCK = (By.CSS_SELECTOR, '.footer__copyright')
    FOOTER_FACEBOOK_ICON = (By.CSS_SELECTOR, '.item__links>a:nth-child(1)>img')
    FOOTER_YOUTUBE_ICON = (By.CSS_SELECTOR, '.item__links>a:nth-child(2)>img')
    FOOTER_INSTA_ICON = (By.CSS_SELECTOR, '.item__links>a:nth-child(3)>img')


class FormOfLoggin():

    TEXT_INPUT_LOGIN = (By.CSS_SELECTOR, 'input[type="email"]')
    TEXT_INPUT_PASSWORD = (By.CSS_SELECTOR, 'input[type=password]')
    CHECK_REMEMBER_ME = (By.CSS_SELECTOR, '#remind')
    BUTTON_LOGIN = (By.CSS_SELECTOR, '.auth__login-block>div>div.button__primary_default')


class DiagnosticPageLocator():
    TITLE_DIAGNOSTIC_TAB = (By.CSS_SELECTOR, '.tabs-block_type_diagnostic>div.modal-header-section>h3')
    CHOICE_SYSTEM_LIST = (By.CSS_SELECTOR, 'div.node>div.node__content>div.node__content-item:nth-child(1)')
    CHOICE_SYSTEM_ITEM = (By.CSS_SELECTOR, 'span[data-value="system1"]')
    CHOICED_SYSTEM_TEXT = (By.CSS_SELECTOR, '.diagnostic-total-block__value')
    CHOISE_COMPONENT_ITEM = (By.CSS_SELECTOR, 'span[data-value="Диагностика ходовой"]')
    CHOICE_COMPONENT_LIST = (By.CSS_SELECTOR, 'div.node>div.node__content>div.node__content-item:nth-child(2)')
    DIAGNOSTIC_BUTTON = (By.CSS_SELECTOR, '.diagnostic__button-container')
    SUB_TITLE_DIAGNOSTIC = (By.CSS_SELECTOR, 'div.title-block>span:nth-child(1)')
    CALENDAR_DAY = (By.CSS_SELECTOR, '.calendar__day-wrapper>div.calendar__day-container>span')
    DIAGNOSTIC_BUTTON_DATE = (By.CSS_SELECTOR, 'div.diagnostic__button-container>div.button__primary_default')


class ProductPageLocator:
    BUTTON_BUY = (By.CSS_SELECTOR, 'div.buy-block__custom-button>button.card__button')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.buy-block__block.buy-block__block_card>div.buy-block__price.price>span.price__quantity')


class BasketPageLocator:
    CHECKOUT_URL = 'https://qa.platform.masterservice.company/checkout-order'
    EMPTY_BUTTON_TEST = (By.CSS_SELECTOR, 'div.empty-cart-container.element-container-show>div>span')
    PRICE_ITEM = (By.CSS_SELECTOR, '.item-cart__price')
    COUNT_ITEM_BTN = (By.CSS_SELECTOR, '#cart-edit-quantity-plus')
    REDUCE_ITEM_BTN = (By.CSS_SELECTOR, '#cart-edit-quantity-minus')
    DELETE_ITEM_BTN = (By.CSS_SELECTOR, '#cart-delete-product')
    CHECK_OUT_ORDER_BTN = (By.CSS_SELECTOR, '#checkout-order-inside-cart')
    PRODUCT_LIST_BASKET = (By.CSS_SELECTOR, 'div.tab-content.cart__content>div>li')
    PRODUCT_COUNT_VALUE = (By.CSS_SELECTOR, '.item-cart__counter.counter>div')
    ORDER_TOTAL = (By.CSS_SELECTOR, '.total-cart__price-amount')
    EXCEL_BTN = (By.CSS_SELECTOR, '#download-excel')


class CheckOutLocators:
    CHECKOUT_ORDER_CONFIRM = (By.CSS_SELECTOR, '#checkout-order-confirm')
    PRODUCT_SEARCH_FIELD = (By.CSS_SELECTOR, 'checkout-order-search-products')
    ADD_COUNT_ITEM = (By.CSS_SELECTOR, '.counter__plus')
    REDUCE_COUNT_ITEM = (By.CSS_SELECTOR, '.counter__minus')
    DELETE_ITEM_BTN = (By.CSS_SELECTOR, 'i.ms-icon-trash')
    NAME_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Имя Фамилия"]')
    PHONE_FIELD = (By.CSS_SELECTOR, 'input[placeholder="Телефон"]')
    EMAIL_FIELD = (By.CSS_SELECTOR, 'input[name="email"]')
    RADIO_BTN_IAM = (By.CSS_SELECTOR, 'input#i-am')
    RADIO_BTN_OTHER_PEOPLE = (By.CSS_SELECTOR, 'input#another-man')
    FIELD_YOUR_NAME = (By.CSS_SELECTOR, 'input[placeholder="Ваше имя"]')
    FIELD_YOUR_PHONE_NUMBER = (By.CSS_SELECTOR, 'div.new-client__form>input[placeholder="Телефон"]')
    CHECKBOX_TERMS = (By.CSS_SELECTOR, '#termsOfService')
    ACTIVE_TAB_TITLE = (By.CSS_SELECTOR, '.tab__title.tab__title_active')













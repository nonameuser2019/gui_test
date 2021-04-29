import pytest
from pages.main_page import MainPage
from pages.diagnostics_page import DiagnosticsPage
from pages.locators import MainPageLocators, DiagnosticPageLocator


# проверка что при нажатии на кнопку записаться на регистрацию открывается окно с регистарцией
def test_open_window_to_diagnostic(browser):
    RIGHT_TITLE_TEXT = 'ЗАПИСАТЬСЯ НА ДИАГНОСТИКУ'
    page = DiagnosticsPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.click_button(*MainPageLocators.BUTTON_TO_DIAGNOSTIC)
    page.check_title(*DiagnosticPageLocator.TITLE_DIAGNOSTIC_TAB, RIGHT_TITLE_TEXT)

@pytest.mark.test
def test_register_to_diagnostic(browser):
    page = DiagnosticsPage(browser, MainPageLocators.MAIN_PAGE_URL)
    page.open()
    page.click_button(*MainPageLocators.BUTTON_TO_DIAGNOSTIC)
    page.change_system(browser)

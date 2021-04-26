import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--headless', action='store_true', help='enable headless mod for supported browsers.')


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    if browser_name == 'chrome':
        print(' \nStart browser chrome for test')
        options = Options()
        #options.headless = True
        browser = webdriver.Chrome(options=options)
        browser.set_window_size(1920, 1080)
        browser.implicitly_wait(5)
    elif browser_name == 'firefox':
        print(' \nStart browser firefox for test')
        fp = webdriver.FirefoxProfile()
        browser = webdriver.Firefox(firefox_profile=fp)
        browser.implicitly_wait(5)
    else:
        raise pytest.UsageError('--browser_name should be chrome or firefox')
    yield browser
    print('\nBroser closed for test')
    browser.quit()
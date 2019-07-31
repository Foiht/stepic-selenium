import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store',
                     default=None, help='Choose your language: ru, en, fr.. ets.')

@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    opt = Options()
    opt.add_experimental_option('prefs', {'intl.accept_languages' : user_language})
    browser = webdriver.Chrome(options=opt)
    yield browser
    print('\nquit browser')
    browser.quit()

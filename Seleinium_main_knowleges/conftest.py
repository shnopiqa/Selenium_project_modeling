import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help='Choose browser: chrome or firefox')
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help="Choose language: ru, en, ... (etc.)")


# options = Options()
# options.add_experimental_option(
#     'prefs',
#     {'intl.accept_languages': "language"})
#
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", "language")


@pytest.fixture(scope="function")
def browser(request):

    user_language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # browser = webdriver.Firefox()
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
@pytest.fixture(scope='function')
def language(request):

    user_language = request.config.getoption('language')
    # Инициализируются опции браузера
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()


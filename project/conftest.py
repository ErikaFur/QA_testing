import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                      help = "Choose language please")

@pytest.fixture(scope='function')
def browser(request):
    options = Options()
    user_language = request.config.getoption("language")
    options.add_experimental_option('prefs', {'intl.accept_languages':user_language})
    browser = webdriver.Chrome(executable_path=r'C:\Users\KAMUz\Desktop\chromedriver\chromedriver.exe', options=options)
    yield browser
    print("\nClose browser")
    browser.quit()
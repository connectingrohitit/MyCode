import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope='module')
def init_driver():
    global driver
    print("----------------- Setup--------------------")
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com/")
    yield
    print("----------------- Setup--------------------")
    driver.quit()


@pytest.mark.usefixtures("inti_driver")
def test_title():
    assert driver.title == 'Google'


@pytest.mark.usefixtures("inti_driver")
def test_url():
    assert driver.current_url == 'https://www.google.com/'

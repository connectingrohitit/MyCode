from selenium import webdriver
import pytest


@pytest.fixture(params=['chrome', 'ff'], scope='class')
def init_driver(request):
    global w_driver
    if request.param == 'chrome':
        w_driver = webdriver.Chrome()
    if request.param == 'ff':
        w_driver = webdriver.Firefox()
    request.cls.driver = w_driver
    yield
    w_driver.close()
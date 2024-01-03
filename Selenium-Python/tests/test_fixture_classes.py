from selenium import webdriver
import pytest


@pytest.fixture(params=['chrome', 'ff'], scope='class')
def init_driver(request):
    if request.param == 'chrome':
        w_driver = webdriver.Chrome()
    if request.param == 'ff':
        w_driver = webdriver.Firefox()
    request.cls.driver = w_driver
    yield
    w_driver.close()


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass


class Test_Fixture(BaseTest):
    def test_fixture_param(self):
        self.driver.get('http://www.google.com/')
        assert self.driver.title == 'Google'

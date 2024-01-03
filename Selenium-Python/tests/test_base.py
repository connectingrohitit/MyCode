from selenium import webdriver

driver = None
def setup():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.delete_all_cookies()
    driver.get("http://www.google.com/")

def tear_down():
    driver.quit()

def test_title():
    assert driver.title == 'Google'

def test_url():
    assert driver.current_url == 'https://www.google.com/'
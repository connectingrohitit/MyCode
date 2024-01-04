from selenium import webdriver


def test_google():
    driver = webdriver.Chrome()
    driver.get("http://www.google.com/")
    driver.quit()


def test_gmail():
    driver = webdriver.Chrome()
    driver.get("http://www.gmail.com/")
    driver.quit()


def test_facebook():
    driver = webdriver.Chrome()
    driver.get("http://www.facebook.com/")
    driver.quit()


def test_instagram():
    driver = webdriver.Chrome()
    driver.get("http://www.instagram.com/")
    driver.quit()


def test_youtube():
    driver = webdriver.Chrome()
    driver.get("http://www.youtube.com/")
    driver.quit()

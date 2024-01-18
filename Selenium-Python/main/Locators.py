from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.relative_locator import with_tag_name

url = "https://practicetestautomation.com/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

# Relative locator - Element above another element
element = driver.find_element(By.CLASS_NAME, "wp-block-image")
print(driver.find_element(with_tag_name("h1").above(element)).text)

# Multiple locator with same tag + Relative locator left / right
menuLinks = driver.find_elements(By.TAG_NAME, "li")
for menuItem in menuLinks:
    if menuItem.text=='COURSES':
        driver.find_element(with_tag_name('a').to_right_of(menuItem)).click()
        break

driver.close()

# Write single function with variable number of parameters to select all 3 filters on https://www.t-mobile.com/tablets
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from selenium import webdriver

url = 'https://www.t-mobile.com/tablets'


def filter_func(*params):
    l = len(params)
    if l <= 1:
        return "Invalid Input"
    else:
        for i in range(l):
            if i == 0:
                if str(params[i]).upper() == 'BRANDS':
                    brands = driver.find_element(By.XPATH, "//span[@class='mat-content ng-tns-c113-16']")
                    brands.click()
                elif str(params[i]).upper() == 'DEALS':
                    deals = driver.find_element(By.XPATH, "//span[@class='mat-content ng-tns-c113-14']")
                    deals.click()
                elif str(params[i]).upper() == 'OPERATING SYSTEM':
                    os = driver.find_element(By.XPATH, "//span[@class='mat-content ng-tns-c113-18']")
                    os.click()
                else:
                    break
                continue
            item = driver.find_element(By.XPATH, f"//span[@class='filter-display-name'][normalize-space()='{params[i]}']")
            chk_box = driver.find_element(locate_with(By.TAG_NAME, "input").near(item))
            if not chk_box.is_selected():
                chk_box.send_keys(Keys.SPACE)
        return "Invalid Input"


driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get(url)
sleep(10)
filter_func('Deals', 'New')
sleep(5)
driver.quit()

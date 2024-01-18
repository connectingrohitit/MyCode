import datetime

from selenium import webdriver

#Initialize driver & launch Chrome browser
url = "https://www.rohitshrivastava.com/"
driver = webdriver.Chrome()
driver.get(url)

#save screenshots
filename = datetime.datetime.now().strftime("%d-%m-%y-%H-%M-%S")+".png"
driver.save_screenshot('images/' + filename)

#close & quit the driver
driver.close()
driver.quit()
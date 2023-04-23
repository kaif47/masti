from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print("sample test case started")
driver = webdriver.Chrome(r"C:\Users\Kaif Bijali\PycharmProjects\seleniumtest2\Browsers\chromedriver.exe")

driver.maximize_window()
driver.get("https://www.google.com/")
kaif = driver.find_element("name","q")
kaif.send_keys("Lord Rinku Singh")
time.sleep(3)
kaif = driver.find_element("name","btnK")
kaif.send_keys(Keys.ENTER)
time.sleep(3)
#close the browser
driver.close()
print("sample test case successfully completed")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")


data = driver.find_element(By.NAME, "fName")
data.send_keys("")
data = driver.find_element(By.NAME, "lName")
data.send_keys("")
data = driver.find_element(By.NAME, "email")
data.send_keys("")
data.send_keys(Keys.ENTER)

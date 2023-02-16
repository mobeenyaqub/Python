from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

timeout = time.time() + 5  # 5 minutes from now

chrome_driver_path = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")
cursor = driver.find_element(By.CSS_SELECTOR, "#rightPanel #store #buyCursor")
money = int(driver.find_element(By.ID, "money").text)
cost_of_cursor = int(driver.find_element(By.CSS_SELECTOR, "#buyCursor b").text.split('-')[1])
click = 0
while True:
    cookie.click()
    click += 1

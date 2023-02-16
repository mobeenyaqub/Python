from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = Service("C:/chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("https://www.python.org/")

dates = [
         driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/time').text,
         driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]/time').text,
         driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]/time').text,
         driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]/time').text,
         driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]/time').text
]

for i in range(0, 5):
    dates[i] = "2022-" + dates[i]


title = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")


events = {}

for i in range(len(dates)):
    events[i] = {
        'time': dates[i],
        'name': title[i].text
    }

print(events)

driver.quit()



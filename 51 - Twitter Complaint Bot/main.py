from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("C:/chromedriver.exe")

PROMISED_DOWN = 100
PROMISED_UP = 50

LOGIN_CREDENTIALS = ["", ""]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '1]/a/span[4]')
        go_button.click()
        time.sleep(40)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                             '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div['
                                           '3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com")
        time.sleep(2)
        sign_in_button = self.driver.find_element(By.XPATH,
                                                  '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                  '1]/div/div[3]/div[5]/a/div/span/span')
        sign_in_button.click()
        time.sleep(10)
        email = self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div['
                                         '2]/div/div/div/div[5]/label/div/div[2]/div/input')
        email.send_keys(LOGIN_CREDENTIALS[0])
        email.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH,
                                            '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                            '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(LOGIN_CREDENTIALS[1])
        password.send_keys(Keys.ENTER)
        time.sleep(5)
        tweet = self.driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                         '2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                         '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                         '1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet.click()
        tweet.send_keys(
            f"Promised speed was {PROMISED_DOWN}down/{PROMISED_UP}up, but I'm getting {self.down}down/{self.up}up")
        tweet_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div['
                                                          '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                          '3]/div/div/div[2]/div[3]/div')
        tweet_button.click()
        time.sleep(10)
        self.driver.quit()


get_speed = InternetSpeedTwitterBot()

get_speed.get_internet_speed()
get_speed.tweet_at_provider()
print("Tweet was successful.")

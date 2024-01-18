import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

TWITTER_NICKNAME = os.getenv("TWITTER_NICKNAME")
TWITTER_PASSWORD = os.getenv("TWITTER_PASSWORD")
PROMISED_DOWN = 200
PROMISED_UP = 180

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InternetSpeedTwitterBot:

    def __init__(self, browser_options):
        self.driver = webdriver.Chrome(options=browser_options)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_btn = self.driver.find_element(By.CSS_SELECTOR, value=".start-button a")
        go_btn.click()

        # Waiting for getting the speed results
        time.sleep(70)

        # Getting up/down speed
        download_element = self.driver.find_element(By.CSS_SELECTOR, value=".result-container-data .download-speed").text
        upload_element = self.driver.find_element(By.CSS_SELECTOR, value=".result-container-data .upload-speed").text
        self.down = float(download_element)
        self.up = float(upload_element)
        # print(f"Down speed is {self.down}.")
        # print(f"UP speed is {self.up}.")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")

        time.sleep(2)
        email_element = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label')
        email_element.send_keys(TWITTER_NICKNAME)
        email_element.send_keys(Keys.ENTER)

        time.sleep(2)
        password_element = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password_element.send_keys(TWITTER_PASSWORD)
        password_element.send_keys(Keys.ENTER)

        time.sleep(5)

        if self.down < PROMISED_DOWN or self.up < PROMISED_UP:
            tweet_text = (f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up "
                          f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}")
            tweet_post_element = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
            tweet_post_element.send_keys(tweet_text)

            publish_btn_element = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div[3]/div/span/span')
            publish_btn_element.click()

            time.sleep(5)
            self.driver.quit()
        else:
            print(f"The actual speed {self.down}down/{self.up}up is better than the promised {PROMISED_DOWN}down/{PROMISED_UP} one.")
            time.sleep(5)
            self.driver.quit()


twitter_bot = InternetSpeedTwitterBot(chrome_options)
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()
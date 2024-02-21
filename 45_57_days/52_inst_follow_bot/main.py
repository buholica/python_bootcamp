from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from dotenv import load_dotenv
import time

load_dotenv("C:\\Users\\Oksana\\Desktop\\passwords.env.txt")

SIMILAR_ACCOUNT = 'bmw'
INSTAGRAM_NICKNAME = os.getenv("INSTAGRAM_NICKNAME")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


class InstaFollower:

    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        time.sleep(3)
        username_element = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_element.send_keys(INSTAGRAM_NICKNAME)

        password_element = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_element.send_keys(INSTAGRAM_PASSWORD)
        password_element.send_keys(Keys.ENTER)

        time.sleep(3)
        # close_popup_element = self.driver.find_element(By.XPATH, value="//div[contains(text(), 'Не сейчас')]")
        # close_popup_element.click()
        #
        # time.sleep(3)
        # notif_popup_element = self.driver.find_element(By.XPATH, value="//button[contains(text(), 'Не сейчас')]")
        # notif_popup_element.click()

    def find_followers(self):
        search_btn = self.driver.find_element(By.XPATH, value="//span[contains(text(), 'Поисковый запрос')]")
        search_btn.click()

        search_input = self.driver.find_element(By.XPATH, value="//input[contains(text(), 'Поиск')]")
        search_input.send_keys(SIMILAR_ACCOUNT)

        account_element = self.driver.find_element(By.XPATH, value=f"//input[contains(text(), {SIMILAR_ACCOUNT})]")
        account_element.click()


    def follow(self):
        pass


inst_follow_bot = InstaFollower()
inst_follow_bot.login()
inst_follow_bot.find_followers()
inst_follow_bot.follow()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re


def check_store_prices():
    money_element = driver.find_element(By.ID, value="money").text
    if "," in money_element:
        money_element = money_element.replace(",", "")
    cookie_count = int(money_element)

    store_section = driver.find_elements(By.CSS_SELECTOR, value="#store div")
    store_collection = [item.text.split('\n', 1)[0] for item in store_section]
    store_collection = store_collection[:-1]
    store_items = {item.split(' -', 1)[0]: int(re.sub('\D', '', item)) for item in store_collection}
    # store_items = [item.split(' -', 1)[0] for item in store_collection]
    # store_prices = [int(re.sub('\D', '', item)) for item in store_collection]

    expensive_item = None

    for item, price in store_items.items():
        if cookie_count >= price:
            if expensive_item is None or store_items[item] > store_items[expensive_item]:
                expensive_item = item

    if expensive_item is not None:
        return expensive_item
    else:
        return None


def buy_the_item():
    affordable_item = check_store_prices()
    item_selector = f"#store #buy{affordable_item}"
    affordable_item_element = driver.find_element(By.CSS_SELECTOR, value=item_selector)
    return affordable_item_element.click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

game_on = True

timeout = time.time() + 10
two_min = time.time() + 60*2

while game_on:
    cookie.click()

    if time.time() > timeout:
        check_store_prices()
        buy_the_item()

        timeout = time.time() + 10

    if time.time() > two_min:
        cookie_per_sec = driver.find_element(By.CSS_SELECTOR, value="#saveMenu #cps").text
        print(cookie_per_sec)
        driver.quit()
        break
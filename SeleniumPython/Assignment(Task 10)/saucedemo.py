
from selenium import webdriver
from selenium.webdriver.common import by
import time

from selenium.webdriver.common.by import By

#setup driver
driver=webdriver.Chrome()

#Open website
driver.get("https://www.saucedemo.com/")

#login page
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(5)

#1. Title of the webpage
title = driver.title
print("Title:", title)

#2.current url of the webpage
current_url = driver.current_url
print("Current URL:", current_url)

#3. Extract the page content of the webpage
page_content = driver.find_element(By.TAG_NAME, "body").text
print("Page Content:", page_content)

#save to file
with open("Webpage_task_11.txt","w", encoding="utf-8") as f:
    f.write(page_content)
    print("Page content:", page_content)
driver.quit()
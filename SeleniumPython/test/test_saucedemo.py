import pytest
from selenium.webdriver.common.by import By

USERNAME = "standard_user"
PASSWORD = "secret_sauce"

#Positive testcase for title
def test_title_positive(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title == "Swag Labs"

#negative test case for title
def test_title_negative(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.title != "Wrong Title"


#positive test case for homepage url
def test_homepage_url_positive(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url == "https://www.saucedemo.com/"

#negative test case for homepage url
def test_homepage_url_negative(driver):
    driver.get("https://www.saucedemo.com/")
    assert driver.current_url != "https://www.google.com/"

#positive test case for dashboard url
def test_dashboard_url_positive(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" in driver.current_url

#negative test case for dashboard url
def test_dashboard_url_negative(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory.html" not in driver.current_url




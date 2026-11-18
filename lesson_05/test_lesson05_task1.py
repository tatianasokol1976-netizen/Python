from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    base_url = "https://httpbin.qa-territory.online/"
    driver.get(base_url)
    sleep(1)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()
    sleep(1)
    assert "/forms/post" in driver.current_url

    driver.back()
    sleep(1)
    assert driver.current_url == base_url

    driver.quit()
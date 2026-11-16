from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(1)
    base_url=driver.current_url
    
    driver.find_element(By.NAME, "custname").send_keys("Татьяна")
    sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()
    sleep(1)
    
    current_url = driver.current_url
    assert current_url != base_url, f"URL не изменился: {current_url}"

    driver.quit()

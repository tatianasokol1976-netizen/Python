from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://www.saucedemo.com/")
        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".login_wrapper"))
        )

        driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

        items = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        for item in items:
            btn_locator = (
                By.XPATH,
                f"//div[@class='inventory_item_description'] [.//div[text()='{item}']]//button",
            )
            wait.until(EC.element_to_be_clickable(btn_locator)).click()

        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()

        checkout_btn = (By.CSS_SELECTOR, "#checkout")
        wait.until(EC.element_to_be_clickable(checkout_btn))
        driver.find_element(*checkout_btn).click()

        wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".checkout_info"))
        )
        fields = {
            "first-name": "Maria",
            "last-name": "Pesto",
            "postal-code": "234869",
        }
        for field_name, value in fields.items():
            field = driver.find_element(By.CSS_SELECTOR, f"#{field_name}")
            field.clear()
            field.send_keys(value)

        driver.find_element(By.CSS_SELECTOR, "#continue").click()

        total_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".summary_total_label"))
        )
        total_text = total_element.text

        assert "$58.29" in total_text, (
            f"Итоговая сумма должна быть $58.29, а вышло: '{total_text}'"
        )

    finally:
        driver.quit()

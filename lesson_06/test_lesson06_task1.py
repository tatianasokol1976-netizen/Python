from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    expected = "Hello World!"

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_btn = driver.find_element(By.CSS_SELECTOR, "#start button")
        start_btn.click()

        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#finish"), expected),
            "Текст 'Hello World!' не появился на странице",
        )
        driver.save_screenshot("lesson_06/screenshots/full_screen.png")

        finish_element = driver.find_element(By.CSS_SELECTOR, "#finish")
        assert finish_element.is_displayed(), (
            "Элемент с текстом не отображается на экране"
        )
        assert finish_element.text.strip() == expected, (
            f"Ожидался текст '{expected}', но получено '{finish_element.text.strip()}'"
        )

    finally:
        driver.quit()

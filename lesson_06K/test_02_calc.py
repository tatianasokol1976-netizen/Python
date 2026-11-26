from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_calculator():
    driver = webdriver.Chrome()

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        delay_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#delay"))
        )
        delay_input.clear()
        delay_input.send_keys("45")

        buttons = ["7", "+", "8", "="]
        for btn in buttons:
            driver.find_element(
                By.XPATH, f"//div[@class='keys']//span[text()='{btn}']"
            ).click()

        screen_locator = (By.CSS_SELECTOR, ".screen")
        WebDriverWait(driver, 50).until(
            EC.text_to_be_present_in_element(screen_locator, "15"),
            "За 50 секунд результат '15' на экране не появился",
        )

        result_text = driver.find_element(*screen_locator).text.strip()
        assert result_text == "15", (
            f"Ожидался результат '15', а получено '{result_text}'"
        )

    finally:
        driver.quit()

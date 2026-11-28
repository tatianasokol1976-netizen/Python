from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_data_types_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
            )
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "input[name='first-name']")
            )
        )
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro",
        }

        for field_name, value in fields.items():
            field = driver.find_element(
                By.CSS_SELECTOR, f"input[name='{field_name}']"
            )
            field.clear()
            field.send_keys(value)

        submit_btn = driver.find_element(By.CLASS_NAME, "mt-3")
        submit_btn.click()

        zip_code_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#zip-code"))
        )
        assert "alert-danger" in zip_code_element.get_attribute("class"), (
            "Поле zip-code не подсвечено красным"
        )

        for field_name in fields:
            field_element = driver.find_element(
                By.CSS_SELECTOR, f"#{field_name}"
            )
            assert "alert-success" in field_element.get_attribute("class"), (
                f"Поле {field_name} не подсвечено зеленым"
            )

    finally:
        driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://gitflic.ru/")

        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "YzlkOWM3ZDAtODQyZi00MGZjLThmMzctZWU4NGEzZDIwNWRk",
                "domain": "gitflic.ru",
            }
        )
        driver.refresh()

        driver.get("https://gitflic.ru/project/")

        profile_link = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.profile-page__profile-name")
            )
        )
        profile_link.click()

        user1_url = driver.current_url
        print("URL 1:", user1_url)

        driver.delete_all_cookies()

        driver.add_cookie(
            {
                "name": "SESSION",
                "value": "MzliODQxMDItNTM5OC00Yjg3LTg4YWItZTllMGY4MmI1MDFk",
                "domain": "gitflic.ru",
            }
        )
        driver.refresh()

        driver.get("https://gitflic.ru/project/")

        profile_link = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "a.profile-page__profile-name")
            )
        )
        profile_link.click()

        user2_url = driver.current_url
        print("URL 2:", user2_url)

        assert user1_url != user2_url, f"URL пользователей совпадают: {user1_url}"

    finally:
        driver.delete_all_cookies()
        driver.quit()

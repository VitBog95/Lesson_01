from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # === Пользователь 1 ===
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "OGNkMGNkNDItNDYxYy00YmYwLWFkNWEtNjhlYzViNTM4YjJl",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/ИМЯ_ПОЛЬЗОВАТЕЛЯ_1")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/user/")
    )
    url_user1 = driver.current_url
    print("URL пользователя 1:", url_user1)

    # === Пользователь 2 ===
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
        "name": "SESSION",
        "value": "NGVlNjg3MGIzZTA2OS00MDc2LThkMmUtZTE2M2EzYWY0ZWY3",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/ИМЯ_ПОЛЬЗОВАТЕЛЯ_2")

    WebDriverWait(driver, 10).until(
        EC.url_contains("/user/")
    )
    url_user2 = driver.current_url
    print("URL пользователя 2:", url_user2)

    # Проверка
    assert url_user1 != url_user2, "URL пользователей совпадают!"
    print("✅ URL пользователей различаются")

    driver.quit()


test_session_storage_auth()

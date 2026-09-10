from selenium import webdriver
from time import sleep


def test_session_storage_auth():
    driver = webdriver.Chrome()

    # === Пользователь 1 ===
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZGQ5ZDVlZmYtY2NhNy00N2YyLTk0NjMtYzhhNWE1OTcyYmQ0",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/ИМЯ_ПОЛЬЗОВАТЕЛЯ_1")
    url_user1 = driver.current_url
    print("URL пользователя 1:", url_user1)
    sleep(2)

    # === Пользователь 2 ===
    driver.delete_all_cookies()
    driver.get("https://gitflic.ru/")
    driver.add_cookie({
        "name": "SESSION",
        "value": "ZDViOGZiYjktY2I2Yi00MTVlLWFjZWYtYmQ5YzIyZmFjNWM5",
        "domain": "gitflic.ru"
    })
    driver.refresh()

    driver.get("https://gitflic.ru/user/ИМЯ_ПОЛЬЗОВАТЕЛЯ_2")
    url_user2 = driver.current_url
    print("URL пользователя 2:", url_user2)
    sleep(2)

    assert url_user1 != url_user2, "URL пользователей совпадают!"
    print("✅ URL пользователей различаются")

    driver.quit()


test_session_storage_auth()

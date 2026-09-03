from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.qa-territory.online")
    sleep(2)

    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    expected_url = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url == expected_url, (
        f"Ожидался URL {expected_url}, получен {driver.current_url}"
    )

    driver.back()

    original_url = "https://httpbin.qa-territory.online/"
    assert driver.current_url == original_url, (
        f"Ожидался URL {original_url}, получен {driver.current_url}"
    )

    driver.quit()


test_navigation()

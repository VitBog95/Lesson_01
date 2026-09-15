from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")
    sleep(2)

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Виталий")
    sleep(1)

    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[text()='Submit order']")
        )
    )
    submit_button.click()
    sleep(2)

    WebDriverWait(driver, 10).until(
        EC.url_to_be("https://httpbin.qa-territory.online/post")
    )
    assert driver.current_url == "https://httpbin.qa-territory.online/post", (
        "URL не изменился"
    )

    driver.quit()


test_form_submission()

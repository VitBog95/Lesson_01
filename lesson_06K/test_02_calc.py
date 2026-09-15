from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calc():

    driver = webdriver.Chrome()

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    delay_field = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_field.clear()
    delay_field.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    WebDriverWait(driver, 60).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, ".screen"), "15"
        )
    )

    result = driver.find_element(By.CSS_SELECTOR, ".screen").text
    assert result == "15", f"Ожидался '15', получен '{result}'"

    driver.quit()

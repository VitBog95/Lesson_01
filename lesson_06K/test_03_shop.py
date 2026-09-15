from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


def test_shop():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "inventory_list"))
    )

    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-backpack"
    ).click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-onesie"
    ).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
    )

    driver.find_element(By.ID, "checkout").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )

    driver.find_element(By.ID, "first-name").send_keys("Виталий")
    driver.find_element(By.ID, "last-name").send_keys("Богатырев")
    driver.find_element(By.ID, "postal-code").send_keys("123456")

    driver.find_element(By.ID, "continue").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    )

    total_text = driver.find_element(
        By.CLASS_NAME, "summary_total_label"
    ).text

    driver.quit()

    assert total_text == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total_text}'"
    )

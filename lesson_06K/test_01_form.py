from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def test_form():
    driver = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install())
    )

    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    # Zip code оставляем пустым
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "zip-code"))
    )

    zip_code = driver.find_element(By.ID, "zip-code")
    zip_class = zip_code.get_attribute("class")
    assert "alert-danger" in zip_class, (
        f"Zip code должен быть красным, класс: {zip_class}"
    )

    green_fields = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in green_fields:
        field = driver.find_element(By.ID, field_id)
        field_class = field.get_attribute("class")
        assert "alert-success" in field_class, (
            f"Поле {field_id} должно быть зелёным, класс: {field_class}"
        )

    driver.quit()

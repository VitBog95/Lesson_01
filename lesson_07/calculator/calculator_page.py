from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def open(self):
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds):
        """Устанавливает задержку калькулятора."""
        field = self.driver.find_element(*self.delay_field)
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, text):
        """Нажимает кнопку калькулятора по её тексту."""
        button = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button).click()

    def get_result(self, expected_text, timeout=60):
        """Ждёт появления результата и возвращает его."""
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )
        return self.driver.find_element(*self.screen).text

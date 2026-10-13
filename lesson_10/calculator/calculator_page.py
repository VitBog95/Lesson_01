from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CalculatorPage:
    """Класс для работы со страницей калькулятора."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.screen = (By.CSS_SELECTOR, ".screen")

    def open(self) -> None:
        """Открывает страницу калькулятора."""
        self.driver.get(self.url)

    def set_delay(self, seconds: int) -> None:
        """
        Устанавливает задержку калькулятора.

        :param seconds: Количество секунд задержки.
        """
        field = self.driver.find_element(*self.delay_field)
        field.clear()
        field.send_keys(str(seconds))

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора по её тексту.

        :param text: Текст на кнопке (например, "7", "+", "=").
        """
        button = (By.XPATH, f"//span[text()='{text}']")
        self.driver.find_element(*button).click()

    def get_result(self, expected_text: str, timeout: int = 60) -> str:
        """
        Ждёт появления результата и возвращает его.

        :param expected_text: Ожидаемый текст результата.
        :param timeout: Максимальное время ожидания в секундах.
        :return: Текст результата.
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )
        return self.driver.find_element(*self.screen).text

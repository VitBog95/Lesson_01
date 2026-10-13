from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы оформления заказа.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет форму оформления заказа.

        :param first_name: Имя.
        :param last_name: Фамилия.
        :param postal_code: Почтовый индекс.
        """
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        self.driver.find_element(*self.continue_button).click()

    def get_total(self) -> str:
        """
        Возвращает итоговую стоимость заказа.

        :return: Текст с итоговой суммой.
        """
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.total_label)
        )
        return self.driver.find_element(*self.total_label).text

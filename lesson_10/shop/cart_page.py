from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы корзины.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def get_items_count(self) -> int:
        """
        Возвращает количество товаров в корзине.

        :return: Количество товаров.
        """
        return len(self.driver.find_elements(*self.cart_items))

    def click_checkout(self) -> None:
        """Нажимает кнопку Checkout и ждёт загрузки формы."""
        self.driver.find_element(*self.checkout_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class MainPage:
    """Класс для работы с главной страницей магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация главной страницы магазина.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.

        :param item_id: ID товара (например, "sauce-labs-backpack").
        """
        button = (By.ID, f"add-to-cart-{item_id}")
        self.driver.find_element(*button).click()

    def go_to_cart(self) -> None:
        """Переходит в корзину."""
        self.driver.find_element(*self.cart_link).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cart_list")
            )
        )

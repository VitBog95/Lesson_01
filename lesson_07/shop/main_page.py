from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")

    def add_to_cart(self, item_id):
        """Добавляет товар в корзину по его ID."""
        button = (By.ID, f"add-to-cart-{item_id}")
        self.driver.find_element(*button).click()

    def go_to_cart(self):
        """Переходит в корзину."""
        self.driver.find_element(*self.cart_link).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart_list"))
        )

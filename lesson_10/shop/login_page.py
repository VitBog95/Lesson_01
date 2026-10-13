from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы авторизации.

        :param driver: Экземпляр WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = "https://www.saucedemo.com/"
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def open(self) -> None:
        """Открывает страницу авторизации."""
        self.driver.get(self.url)

    def login(self, username: str, password: str) -> None:
        """
        Авторизует пользователя.

        :param username: Имя пользователя.
        :param password: Пароль.
        """
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

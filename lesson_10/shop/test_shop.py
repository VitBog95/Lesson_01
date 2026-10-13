import allure
from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


@allure.title("Проверка оформления заказа в магазине")
@allure.description(
    "Тест проверяет полный цикл: авторизация, добавление товаров, "
    "оформление заказа и итоговую сумму $58.29"
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop():
    driver = webdriver.Chrome()

    with allure.step("Авторизоваться как standard_user"):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить 3 товара в корзину"):
        main_page = MainPage(driver)
        main_page.add_to_cart("sauce-labs-backpack")
        main_page.add_to_cart("sauce-labs-bolt-t-shirt")
        main_page.add_to_cart("sauce-labs-onesie")
        main_page.go_to_cart()

    with allure.step("Перейти к оформлению заказа"):
        cart_page = CartPage(driver)
        assert cart_page.get_items_count() == 3
        cart_page.click_checkout()

    with allure.step("Заполнить форму и получить итоговую сумму"):
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Виталий", "Богатырев", "123456")
        total = checkout_page.get_total()

    with allure.step("Проверить итоговую сумму: $58.29"):
        assert total == "Total: $58.29", (
            f"Ожидалось 'Total: $58.29', получено '{total}'"
        )

    driver.quit()

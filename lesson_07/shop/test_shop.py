from selenium import webdriver
from login_page import LoginPage
from main_page import MainPage
from cart_page import CartPage
from checkout_page import CheckoutPage


def test_shop():
    driver = webdriver.Firefox()

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    main_page = MainPage(driver)
    main_page.add_to_cart("sauce-labs-backpack")
    main_page.add_to_cart("sauce-labs-bolt-t-shirt")
    main_page.add_to_cart("sauce-labs-onesie")
    main_page.go_to_cart()

    cart_page = CartPage(driver)
    assert cart_page.get_items_count() == 3
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Виталий", "Богатырев", "123456")
    total = checkout_page.get_total()

    driver.quit()

    assert total == "Total: $58.29", (
        f"Ожидалось 'Total: $58.29', получено '{total}'"
    )

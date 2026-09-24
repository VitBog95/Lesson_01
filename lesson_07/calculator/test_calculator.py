from selenium import webdriver
from calculator.calculator_page import CalculatorPage


def test_calculator():
    driver = webdriver.Chrome()
    page = CalculatorPage(driver)

    page.open()
    page.set_delay(45)
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")

    result = page.get_result("15", timeout=60)
    assert result == "15", f"Ожидался '15', получен '{result}'"

    driver.quit()

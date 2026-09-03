from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")
    sleep(2)

    links = driver.find_elements(By.TAG_NAME, "a")
    print(f"Найдено ссылок: {len(links)}")
    sleep(1)

    assert len(links) == 9, (
        f"Ожидалось 9 ссылок, найдено {len(links)}"
    )
    print("✅ Количество ссылок верное")

    for link in links:
        assert link.is_displayed(), (
            f"Ссылка с текстом '{link.text}' не отображается"
        )
    print("✅ Все ссылки отображаются")

    assert links[0].text == "1", (
        f"Текст первой ссылки должен быть '1', "
        f"получено '{links[0].text}'"
    )
    print("✅ Текст первой ссылки равен '1'")

    sleep(3)
    driver.quit()


test_multiple_elements()

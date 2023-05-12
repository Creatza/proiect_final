from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    # Setare path-ul pentru driver-ul Chrome
    driver_path = "./drivers/chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(driver_path, options=options)

    # Navigare către pagina de pornire
    driver.get("https://www.selenium.dev/")

    yield driver
    driver.quit()


def test_title(browser):
    # Verificare titlu pagină
    expected_title = "SeleniumHQ Browser Automation"
    actual_title = browser.title
    assert expected_title == actual_title
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/")

# действия теста

driver.quit()
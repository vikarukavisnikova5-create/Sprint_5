import pytest
from selenium import webdriver

@pytest.fixture

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://stellarburgers.education-services.ru")
    yield driver
    driver.quit()
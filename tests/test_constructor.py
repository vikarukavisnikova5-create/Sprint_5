from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url import MAIN_URL
from locators import Locators
class TestConstructor:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(MAIN_URL)
    def teardown_method(self):
        self.driver.quit()
    # Проверяем переключение на «Булки»
    def test_buns_tab(self):
        # Находим таб «Соусы»
        sauces = self.wait.until(
            EC.presence_of_element_located(
                Locators.SAUCES
            )
        )
        # Нажимаем «Соусы»
        self.driver.execute_script(
            "arguments[0].click();",
            sauces
        )
        # Находим таб «Булки»
        buns = self.wait.until(
            EC.presence_of_element_located(
                Locators.BUNS
            )
        )
        # Нажимаем «Булки»
        self.driver.execute_script(
            "arguments[0].click();",
            buns
        )
        # Проверяем, что «Булки» стали активными
        self.wait.until(
            lambda driver:
            "tab_tab_type_current" in buns.get_attribute("class")
        )
        assert "tab_tab_type_current" in buns.get_attribute("class")
    # Проверяем переключение на «Соусы»
    def test_sauces_tab(self):
        sauces = self.wait.until(
            EC.presence_of_element_located(
                Locators.SAUCES
            )
        )
        # Нажимаем «Соусы»
        self.driver.execute_script(
            "arguments[0].click();",
            sauces
        )
        # Проверяем, что «Соусы» стали активными
        self.wait.until(
            lambda driver:
            "tab_tab_type_current" in sauces.get_attribute("class")
        )
        assert "tab_tab_type_current" in sauces.get_attribute("class")
    # Проверяем переключение на «Начинки»
    def test_fillings_tab(self):
        fillings = self.wait.until(
            EC.presence_of_element_located(
                Locators.FILLINGS
            )
        )
        # Нажимаем «Начинки»
        self.driver.execute_script(
            "arguments[0].click();",
            fillings
        )
        # Проверяем, что «Начинки» стали активными
        self.wait.until(
            lambda driver:
            "tab_tab_type_current" in fillings.get_attribute("class")
        )
        assert "tab_tab_type_current" in fillings.get_attribute("class")
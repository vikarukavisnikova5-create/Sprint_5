from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

class TestConstructor:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://stellarburgers.education-services.ru"
        )

        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self):
        self.driver.quit()

    def test_go_to_buns_section(self):

        login_page = LoginPage(self.driver)

        login_page.click_buns()

        assert "Булки" in self.driver.page_source

    def test_go_to_sauces_section(self):

        login_page = LoginPage(self.driver)

        login_page.click_sauces()

        assert "Соусы" in self.driver.page_source

    def test_go_to_fillings_section(self):

        login_page = LoginPage(self.driver)

        login_page.click_fillings()

        assert "Начинки" in self.driver.page_source
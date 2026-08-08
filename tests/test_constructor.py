from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

class TestConstructor:

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
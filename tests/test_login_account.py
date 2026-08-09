from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage
from data import EMAIL, PASSWORD
from pages.url import (
    MAIN_URL,
    REGISTER_URL,
    LOGIN_URL,
    FORGOT_PASSWORD,
    ACCOUNT_URL
)

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(MAIN_URL)

    def teardown_method(self):
        self.driver.quit()

    # Вход через кнопку "Войти в аккаунт" на главной странице
    def test_login_from_main_page(self):

        login_page = LoginPage(self.driver)

        login_page.click_login_button_main()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку "Личный кабинет"
    def test_login_from_personal_account(self):

        login_page = LoginPage(self.driver)

        login_page.click_personal_account()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку "Войти" в форме регистрации
    def test_login_from_register_form(self):

        login_page = LoginPage(self.driver)

        self.driver.get(REGISTER_URL)

        self.wait.until(
            lambda driver: REGISTER_URL in driver.current_url
        )

        assert REGISTER_URL in self.driver.current_url

        login_page.click_login_from_register()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form(self):

        login_page = LoginPage(self.driver)

        login_page.click_login_button_main()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.click_forgot_password()

        self.wait.until(
            lambda driver: FORGOT_PASSWORD in driver.current_url
        )

        assert FORGOT_PASSWORD in self.driver.current_url

        login_page.click_login_from_forgot_password()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Выход из аккаунта через кнопку "Выйти"
    def test_logout_from_personal_account(self):

        login_page = LoginPage(self.driver)

        # Вход в аккаунт
        login_page.click_login_button_main()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

        # Переходим в личный кабинет
        login_page.click_personal_account()

        self.wait.until(
            lambda driver: ACCOUNT_URL in driver.current_url
        )

        assert ACCOUNT_URL in self.driver.current_url

        # Выходим
        login_page.click_logout()

        self.wait.until(
            lambda driver: LOGIN_URL in driver.current_url
        )

        assert LOGIN_URL in self.driver.current_url
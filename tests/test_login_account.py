from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
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
        self.locators = Locators(self.driver)
        self.driver.get(MAIN_URL)

    def teardown_method(self):

        self.driver.quit()

    # Вход через кнопку "Войти в аккаунт" на главной странице

    def test_login_from_main_page(self):

        self.locators.click_login_button_main()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )
        assert LOGIN_URL in self.driver.current_url

        self.locators.set_email(EMAIL)
        self.locators.set_password(PASSWORD)
        self.locators.click_login()

        assert self.locators.is_constructor_visible()

    # Вход через кнопку "Личный кабинет"

    def test_login_from_personal_account(self):

        self.locators.click_personal_account()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url

        self.locators.set_email(EMAIL)
        self.locators.set_password(PASSWORD)
        self.locators.click_login()

        assert self.locators.is_constructor_visible()

    # Вход через кнопку "Войти" в форме регистрации

    def test_login_from_register_form(self):

        self.driver.get(REGISTER_URL)
        self.wait.until(

            lambda driver: REGISTER_URL in driver.current_url

        )

        assert REGISTER_URL in self.driver.current_url

        self.locators.click_login_from_register()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url

        self.locators.set_email(EMAIL)
        self.locators.set_password(PASSWORD)
        self.locators.click_login()

        assert self.locators.is_constructor_visible()

    # Вход через кнопку "Войти" в форме восстановления пароля

    def test_login_from_forgot_password_form(self):

        self.locators.click_login_button_main()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url

        self.locators.click_forgot_password()
        self.wait.until(

            lambda driver: FORGOT_PASSWORD in driver.current_url

        )

        assert FORGOT_PASSWORD in self.driver.current_url

        self.locators.click_login_from_forgot_password()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url

        self.locators.set_email(EMAIL)
        self.locators.set_password(PASSWORD)
        self.locators.click_login()

        assert self.locators.is_constructor_visible()

    # Выход из аккаунта через кнопку "Выйти"

    def test_logout_from_personal_account(self):

        # Вход в аккаунт

        self.locators.click_login_button_main()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url

        self.locators.set_email(EMAIL)
        self.locators.set_password(PASSWORD)
        self.locators.click_login()

        assert self.locators.is_constructor_visible()

        # Переходим в личный кабинет

        self.locators.click_personal_account()
        self.wait.until(

            lambda driver: ACCOUNT_URL in driver.current_url

        )

        assert ACCOUNT_URL in self.driver.current_url

        # Выходим

        self.locators.click_logout()
        self.wait.until(

            lambda driver: LOGIN_URL in driver.current_url

        )

        assert LOGIN_URL in self.driver.current_url
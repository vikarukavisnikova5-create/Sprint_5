from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

EMAIL = "victoria_rukavishnikova_50_666@ya.ru"
PASSWORD = "password1234"

class TestLogin:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://stellarburgers.education-services.ru"
        )

    def teardown_method(self):
        self.driver.quit()

    # Вход через кнопку "Войти в аккаунт" на главной странице

    def test_login_from_main_page(self):

        login_page = LoginPage(self.driver)

        login_page.click_login_button_main()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку "Личный кабинет"

    def test_login_from_personal_account(self):

        login_page = LoginPage(self.driver)

        login_page.click_personal_account()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку "Войти" в форме регистрации

    def test_login_from_register_form(self):

        login_page = LoginPage(self.driver)

        self.driver.get(
            "https://stellarburgers.education-services.ru/register"
        )

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/register" in driver.current_url
        )

        assert "/register" in self.driver.current_url

        login_page.click_login_from_register()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Вход через кнопку в форме восстановления пароля

    def test_login_from_forgot_password_form(self):

        login_page = LoginPage(self.driver)

        # Переходим на страницу входа
        login_page.click_login_button_main()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

        # Нажимаем "Восстановить пароль"
        login_page.click_forgot_password()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/forgot-password" in driver.current_url
        )

        assert "/forgot-password" in self.driver.current_url

        # Нажимаем "Войти" в форме восстановления пароля
        login_page.click_login_from_forgot_password()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

    # Выход из аккаунта через кнопку "Выйти"
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://stellarburgers.education-services.ru"
        )

    def teardown_method(self):
        self.driver.quit()

    def test_logout_from_personal_account(self):

        login_page = LoginPage(self.driver)

        # Вход в аккаунт
        login_page.click_login_button_main()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

        # Переходим в личный кабинет
        login_page.click_personal_account()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/profile" in driver.current_url
        )

        assert "/profile" in self.driver.current_url

        # Выходим
        login_page.click_logout()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        assert "/login" in self.driver.current_url

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from pages.login_page import LoginPage

EMAIL = "victoria_rukavishnikova_50_666@ya.ru"
PASSWORD = "password1234"

class TestNavigation:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(
            "https://stellarburgers.education-services.ru"
        )

    def teardown_method(self):
        self.driver.quit()

    # Переход в личный кабинет

    def test_go_to_personal_account(self):

        login_page = LoginPage(self.driver)

        # Нажимаем "Войти в аккаунт"
        login_page.click_login_button_main()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        # Проверяем вход
        assert login_page.is_constructor_visible()

        # Переходим в личный кабинет
        login_page.click_personal_account()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/profile" in driver.current_url
        )

        assert "/profile" in self.driver.current_url

    # Переход из личного кабинета в Конструктор

    def test_go_to_constructor_from_personal_account(self):

        login_page = LoginPage(self.driver)

        # Авторизация
        login_page.click_login_button_main()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/login" in driver.current_url
        )

        login_page.set_email(EMAIL)
        login_page.set_password(PASSWORD)

        login_page.click_login()

        assert login_page.is_constructor_visible()

        # Открываем личный кабинет
        login_page.click_personal_account()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/profile" in driver.current_url
        )

        # Нажимаем "Конструктор"
        login_page.click_constructor()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/" in driver.current_url
        )

        assert "/profile" not in self.driver.current_url

    # Переход по логотипу Stellar Burgers

    def test_go_to_constructor_by_logo(self):

        login_page = LoginPage(self.driver)

        # Авторизация
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

        # Нажимаем логотип
        login_page.click_logo()

        WebDriverWait(self.driver, 10).until(
            lambda driver: "/profile" not in driver.current_url
        )

        assert "/profile" not in self.driver.current_url


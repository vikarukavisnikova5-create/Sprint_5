from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from data import EMAIL, PASSWORD
from pages.url import MAIN_PAGE_URL, ACCOUNT_URL
class TestNavigation:
    # Проверяем переход в личный кабинет
    def test_go_to_personal_account(self, driver):
        locators = Locators(driver)
        # Нажимаем «Войти в аккаунт»
        locators.click_login_button_main()
        # Вводим email
        locators.set_email(EMAIL)
        # Вводим пароль
        locators.set_password(PASSWORD)
        # Нажимаем «Войти»
        locators.click_login()
        # Ждём успешного входа
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url != "https://stellarburgers.education-services.ru/login"
        )
        # Нажимаем «Личный кабинет»
        locators.click_personal_account()
        # Ждём переход в личный кабинет
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url == ACCOUNT_URL
        )
        # Проверяем переход в личный кабинет
        assert driver.current_url == ACCOUNT_URL
    # Проверяем переход из личного кабинета в конструктор
    def test_go_to_constructor_from_personal_account(self, driver):
        locators = Locators(driver)
        # Нажимаем «Войти в аккаунт»
        locators.click_login_button_main()
        # Вводим email
        locators.set_email(EMAIL)
        # Вводим пароль
        locators.set_password(PASSWORD)
        # Нажимаем «Войти»
        locators.click_login()
        # Ждём успешного входа
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url != "https://stellarburgers.education-services.ru/login"
        )
        # Открываем личный кабинет
        locators.click_personal_account()
        # Ждём открытия личного кабинета
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url == ACCOUNT_URL
        )
        # Нажимаем «Конструктор»
        locators.click_constructor()
        # Проверяем переход на главную страницу
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url == MAIN_PAGE_URL
        )
        assert driver.current_url == MAIN_PAGE_URL
    # Проверяем переход в конструктор через логотип
    def test_go_to_constructor_by_logo(self, driver):
        locators = Locators(driver)
        # Нажимаем «Войти в аккаунт»
        locators.click_login_button_main()
        # Вводим email
        locators.set_email(EMAIL)
        # Вводим пароль
        locators.set_password(PASSWORD)
        # Нажимаем «Войти»
        locators.click_login()
        # Ждём успешного входа
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url != "https://stellarburgers.education-services.ru/login"
        )
        # Открываем личный кабинет
        locators.click_personal_account()
        # Ждём открытия личного кабинета
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url == ACCOUNT_URL
        )
        # Нажимаем на логотип Stellar Burgers
        locators.click_logo()
        # Проверяем переход на главную страницу
        WebDriverWait(driver, 10).until(
            lambda driver: driver.current_url == MAIN_PAGE_URL
        )
        assert driver.current_url == MAIN_PAGE_URL
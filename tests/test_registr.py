from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url import REGISTER_URL, LOGIN_URL
from helpers import GoodPassword

class TestSuccessfulRegistration:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(REGISTER_URL)

    def teardown_method(self):
        self.driver.quit()

    def test_success_registration(self):

        # Генерируем уникальный email
        email = GoodPassword.generate_email()

        # Генерируем корректный пароль
        password_value = GoodPassword.generate_password()

        # Имя
        name = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//label[text()='Имя']/following-sibling::input")
            )
        )

        name.send_keys("Вика")

        # Email
        email_input = self.driver.find_element(
            By.XPATH,
            "//label[text()='Email']/following-sibling::input"
        )

        email_input.send_keys(email)

        # Пароль
        password = self.driver.find_element(
            By.XPATH,
            "//input[@type='password']"
        )

        password.send_keys(password_value)

        # Кнопка регистрации
        register_button = self.driver.find_element(
            By.XPATH,
            "//button[text()='Зарегистрироваться']"
        )

        register_button.click()

        # Проверяем переход на страницу входа
        self.wait.until(
            EC.url_to_be(LOGIN_URL)
        )

        assert self.driver.current_url == LOGIN_URL
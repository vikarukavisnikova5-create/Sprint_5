from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class TestRegistration:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

        self.driver.get(
            "https://stellarburgers.education-services.ru/register"
        )

    def teardown_method(self):
        self.driver.quit()

    def test_success_registration(self):

        # Уникальный email
        email = f"vika_50_666_{random.randint(1000,9999)}@yandex.ru"

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
        password.send_keys("123456")

        # Кнопка регистрации
        register_button = self.driver.find_element(
            By.XPATH,
            "//button[text()='Зарегистрироваться']"
        )
        register_button.click()

        # Проверка перехода после регистрации
        self.wait.until(
            EC.url_contains("/login")
        )

        assert "/login" in self.driver.current_url

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url import REGISTER_URL
from helpers import BadPassword

class TestRegistrationBadPassword:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get(REGISTER_URL)

    def teardown_method(self):
        self.driver.quit()

    def test_registration_with_incorrect_password(self):
        # Генерируем уникальный email
        email = BadPassword.generate_email()
        # Генерируем некорректный пароль
        password = BadPassword.generate_password()
        # Поле «Имя»

        name = self.wait.until(
            EC.visibility_of_element_located(

                (By.XPATH, "//label[text()='Имя']/following-sibling::input")

            )
        )
        name.send_keys("Вика")

        # Поле «Email»

        email_input = self.driver.find_element(
            By.XPATH,
            "//label[text()='Email']/following-sibling::input"
        )

        email_input.send_keys(email)
        # Поле «Пароль»
        password_input = self.driver.find_element(
            By.XPATH,
            "//input[@type='password']"
        )

        password_input.send_keys(password)

        # Кнопка «Зарегистрироваться»

        register_button = self.driver.find_element(
            By.XPATH,
            "//button[text()='Зарегистрироваться']"
        )

        register_button.click()
        # Проверяем сообщение о некорректном пароле
        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[text()='Некорректный пароль']")

            )
        )

        assert error.text == "Некорректный пароль"
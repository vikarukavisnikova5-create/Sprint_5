from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.url import REGISTER_URL
from locators import Locators
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

                Locators.NAME
            )
        )

        name.send_keys("Вика")

        # Поле «Email»

        email_input = self.wait.until(

            EC.visibility_of_element_located(

                Locators.REGISTER_EMAIL_FIELD
            )
        )

        email_input.send_keys(email)

        # Поле «Пароль»

        password_input = self.wait.until(

            EC.visibility_of_element_located(

                Locators.REGISTER_PASSWORD_FIELD
            )
        )

        password_input.send_keys(password)

        # Кнопка «Зарегистрироваться»

        register_button = self.wait.until(

            EC.element_to_be_clickable(

                Locators.REGISTER_BUTTON
            )
        )

        register_button.click()

        # Проверяем сообщение о некорректном пароле

        error = self.wait.until(

            EC.visibility_of_element_located(

                Locators.INVALID_PASSWORD
            )
        )

        assert error.text == "Некорректный пароль"
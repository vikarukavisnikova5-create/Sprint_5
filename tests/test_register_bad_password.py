from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class TestRegistrationBadPassword:

    def test_registration_with_incorrect_password(self):

        # Уникальный email
        email = f"vika_50_{random.randint(1000,9999)}@yandex.ru"

        # Поле Имя
        self.driver.find_element(
            By.XPATH,
            "//label[text()='Имя']/following-sibling::input"
        ).send_keys("Вика")

        # Поле Email
        self.driver.find_element(
            By.XPATH,
            "//label[text()='Email']/following-sibling::input"
        ).send_keys(email)

        # Некорректный пароль (меньше 6 символов)
        self.driver.find_element(
            By.XPATH,
            "//input[@type='password']"
        ).send_keys("12345")

        # Кнопка регистрации
        self.driver.find_element(
            By.XPATH,
            "//button[text()='Зарегистрироваться']"
        ).click()

        # Проверяем ошибку
        error = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[text()='Некорректный пароль']")
            )
        )

        assert error.text == "Некорректный пароль"
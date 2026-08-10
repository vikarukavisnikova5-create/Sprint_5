from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Locators:

    # Главная страница

    LOGO = (By.XPATH,"//header//a")
    CONSTRUCTOR_BUTTON = (By.XPATH,"//p[text()='Конструктор']")
    LOGIN_MAIN_BUTTON = (By.XPATH,"//button[contains(text(),'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH,"//a[contains(@href,'account')]")

    # Страница регистрации
   

    NAME = (By.XPATH,"//label[text()='Имя']/following-sibling::input")
    REGISTER_EMAIL_FIELD = (By.XPATH,"//label[text()='Email']/following-sibling::input")
    REGISTER_PASSWORD_FIELD = (By.XPATH,"//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH,"//button[text()='Зарегистрироваться']")
    LOGIN_FROM_REGISTER = (By.XPATH,"//a[contains(text(),'Войти')]")

    # Страница входа

    EMAIL_FIELD = (By.XPATH,"//input[@type='text']")
    PASSWORD_FIELD = (By.XPATH,"//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH,"//button[contains(text(),'Войти')]")
    CONSTRUCTOR = (By.XPATH,"//p[contains(text(),'Конструктор')]")
    FORGOT_PASSWORD_LINK = (By.XPATH,"//a[contains(text(),'Восстановить пароль')]")
    LOGIN_FROM_FORGOT_PASSWORD = (By.XPATH,"//a[contains(text(),'Войти')]")
    LOGOUT_BUTTON = (By.XPATH,"//button[text()='Выход']")
    INVALID_PASSWORD = (By.XPATH,"//*[text()='Некорректный пароль']")

    # Конструктор

    BUNS = (By.XPATH,"//span[text()='Булки']/parent::div")
    SAUCES = (By.XPATH,"//span[text()='Соусы']/parent::div")
    FILLINGS = (By.XPATH,"//span[text()='Начинки']/parent::div")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_login_button_main(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_MAIN_BUTTON)
        ).click()

    def click_personal_account(self):
         self.wait.until(
        EC.element_to_be_clickable(self.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    def click_register_link(self):
        self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_LINK)
        ).click()

    def click_login_from_register(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_FROM_REGISTER)
        ).click()

    def set_email(self, email):
        field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_FIELD)
        )
        field.clear()
        field.send_keys(email)

    def set_password(self, password):
        field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD_FIELD)
        )
        field.clear()
        field.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def click_logout(self):
       self.wait.until(
        EC.element_to_be_clickable(self.LOGOUT_BUTTON)
    ).click()

    def is_constructor_visible(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CONSTRUCTOR)
        ).is_displayed()
    
    def click_forgot_password(self):
       self.wait.until(
        EC.element_to_be_clickable(self.FORGOT_PASSWORD_LINK)
    ).click()

    def click_login_from_forgot_password(self):
     self.wait.until(
        EC.element_to_be_clickable(
            self.LOGIN_FROM_FORGOT_PASSWORD
        )
    ).click()
       
    def click_constructor(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONSTRUCTOR_BUTTON)
        ).click()

    def click_logo(self):
      self.wait.until(
        EC.element_to_be_clickable(self.LOGO)
    ).click()
      
    def click_buns(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.BUNS)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
    def click_sauces(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.SAUCES)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
    def click_fillings(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.FILLINGS)
        )
        self.driver.execute_script(
            "arguments[0].click();",
            element
        )
    def is_buns_selected(self):
     return self.wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'tab_tab_type_current')]//span[text()='Булки']"
            )
        )
    ).is_displayed()

     return element.is_displayed()
    
    def is_sauces_selected(self):
     return self.wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'tab_tab_type_current')]//span[text()='Соусы']"
            )
        )
    ).is_displayed()

    
    def is_fillings_selected(self):
     return self.wait.until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                "//div[contains(@class,'tab_tab_type_current')]//span[text()='Начинки']"
            )
        )
    ).is_displayed()
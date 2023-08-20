from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class LoginPage(BasePage):

    """Под каждую страницу мы пишем отдельный PageObject"""

    def get_url(self) -> str:
        return 'http://tutorialsninja.com/demo/index.php?route=account/login'

    def get_email_field(self) -> WebElement:
        """Идентификация элемента EMAIL FIELD на странице"""
        # ВАЖНО!
        # Единственное место во всей тестовой инфраструктуре,
        # где мы задаем, как мы будем искать EMAIL FIELD.
        email_field = self.driver.find_element(By.ID, 'input-email')
        return email_field

    def get_password_field(self) -> WebElement:
        """Идентификация элемента PASSWORD FIELD на странице"""
        return self.driver.find_element(By.ID, 'input-password')

    def get_login_button(self) -> WebElement:
        """Поиск элемента LOGIN BUTTON"""
        return self.driver.find_element(By.CSS_SELECTOR, '[value=Login]')

    def get_alert_text(self) -> str:
        """Считать со страницы текст ошибки"""
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        return alert_text.text

    def get_notification_text(self) -> str:
        """Считать со страницы текст уведомления"""
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-success')
        return alert_text.text

    def enter_email(self, email: str):
        """Ввести EMAIL"""
        email_field = self.get_email_field()
        email_field.send_keys(email)

    def clear_email(self):
        """Очистить EMAIL"""
        email_field = self.get_email_field()
        email_field.clear()

    def enter_password(self, password: str):
        """Ввести PASSWORD"""
        password_field = self.get_password_field()
        password_field.send_keys(password)

    def clear_password(self):
        """Очистить PASSWORD"""
        self.get_password_field().clear()

    def login(self):
        """Войти в систему"""
        self.get_login_button().click()

    def go_to_password_recovery_page(self):
        """Перейти на страницу восстановления пароля"""
        forgot_password_link = self.driver.find_element(By.LINK_TEXT, 'Forgotten Password')
        forgot_password_link.click()

    def login_with(self, email: str, password: str):
        """Залогиниться с нужными параметрами"""
        self.clear_password()
        self.clear_email()
        self.enter_email(email)
        self.enter_password(password)
        self.login()

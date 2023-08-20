from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from pageobject.base_page import BasePage


class ForgotPasswordPage(BasePage):

    """Под каждую страницу мы пишем отдельный PageObject"""

    def get_url(self) -> str:
        return 'http://tutorialsninja.com/demo/index.php?route=account/forgotten'

    def get_email_field(self) -> WebElement:
        return self.driver.find_element(By.ID, 'input-email')

    def get_continue_button(self) -> WebElement:
        return self.driver.find_element(By.CSS_SELECTOR, '[value=Continue]')

    def get_alert_text(self) -> str:
        """Считать со страницы текст ошибки"""
        alert_text = self.driver.find_element(By.CLASS_NAME, 'alert-danger')
        return alert_text.text

    def enter_email(self, email: str):
        """Ввести EMAIL"""
        email_field = self.get_email_field()
        email_field.send_keys(email)

    def clear_email(self):
        """Очистить EMAIL"""
        email_field = self.get_email_field()
        email_field.clear()

    def restore_password(self):
        """Восстанавливает пароль"""
        self.get_continue_button().click()

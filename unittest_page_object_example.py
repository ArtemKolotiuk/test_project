import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pageobject.account_page import AccountPage
from pageobject.forgot_password_page import ForgotPasswordPage
from pageobject.login_page import LoginPage
from pageobject.shopping_cart_page import ShoppingCartPage


class LoginTests(unittest.TestCase):

    def setUp(self) -> None:
        """Действия до теста"""
        self.email = 'test+19apr1@example.com'
        self.email_incorrect = 'test+19aprasdfasdfasdfasd@example.com'
        self.password = 'asdfasdf'
        self.password_incorrect = '123123'
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self) -> None:
        """Действия после теста"""
        self.driver.close()

    def testOK(self):
        """Успешный вход существующим пользователем"""

        # Находим page object для страницы Логина
        # Передаем объекту в конструкторе ссылку на Selenium WebDriver.
        login_page = LoginPage(self.driver)

        # self.driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
        login_page.open()

        # email_field = self.driver.find_element(By.ID, 'input-email')
        # email_field.send_keys(self.email)
        login_page.enter_email(self.email)

        # password_field = self.driver.find_element(By.ID, 'input-password')
        # password_field.send_keys(self.password)
        login_page.enter_password(self.password)

        # login_button = self.driver.find_element(By.CSS_SELECTOR, '[value=Login]')
        # login_button.click()
        login_page.login()

        # Нам нужно проверить, успешно ли мы вошли?
        # edit_account_link = self.driver.find_elements(By.LINK_TEXT, 'Edit your account information')
        # Сообщаем о том, прошел тест или нет.
        # self.assertEqual(1, len(edit_account_link))
        # assert 1 == len(edit_account_link)
        account_page = AccountPage(self.driver)
        self.assertTrue(account_page.is_present())

    def test_ok_very_short(self):
        """Тест логина одной высокоуровневой операцией"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.login_with(self.email, self.password)
        account_page = AccountPage(self.driver)
        self.assertTrue(account_page.is_present())

    def test_not_ok(self):
        """Проверка на неправильный пароль"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.enter_email(self.email)
        login_page.enter_password(self.password_incorrect)
        login_page.login()
        self.assertEqual(
            'Warning: No match for E-Mail Address and/or Password.',
            login_page.get_alert_text()
        )

    def test_password_recovery(self):
        """Восстановление пароля"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.go_to_password_recovery_page()
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.enter_email(self.email)
        forgot_password_page.restore_password()
        actual_text = login_page.get_notification_text()
        expected_text = 'An email with a confirmation link has been sent your email address.'

        self.assertEqual(
            expected_text,
            actual_text
        )

    def test_password_recovery_not_fount(self):
        """Восстановление пароля на несуществующий почта"""
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.go_to_password_recovery_page()
        forgot_password_page = ForgotPasswordPage(self.driver)
        forgot_password_page.enter_email(self.email_incorrect)
        forgot_password_page.restore_password()
        actual_text = forgot_password_page.get_alert_text()

        # Сообщаем о том, прошел тест или нет.
        expected_text = 'Warning: The E-Mail Address was not found in our records, please try again!'

        self.assertEqual(
            expected_text,
            actual_text
        )

    def test_shopping_cart(self):
        shopping_cart = ShoppingCartPage(self.driver)
        shopping_cart.open()

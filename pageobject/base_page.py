from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:

    """Базовый (родительский) класс PageObject,
    который содержит общие для всех страниц методы."""

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_url(self) -> str:
        # Обязательно реализовать в дочерних классах.
        raise NotImplementedError

    def open(self):
        """Открыть страницу account."""
        self.driver.get(self.get_url())

    def save_screenshot(self):
        pass

    def click_via_script(self, element: WebElement):
        """
        Метод осуществляет клик по элементу через JS скрипт
        :param element: экземпляр класса WebElement
        """
        self.driver.execute_script("arguments[0].click();", element)


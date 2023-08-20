from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By


def test_search():
    service = Service(executable_path="/path/to/chromedriver")
    driver = webdriver.Chrome(service=service)

    driver.get('https://www.selenium.dev/')
    search = driver.find_element(By.LINK_TEXT, 'Documentation')
    search.click()
    title = driver.find_element(By.XPATH, "//h1[contains(text(),'The Selenium Browser Automation Project')]")
    assert title

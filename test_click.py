from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.1irs.net')
title = driver.title
assert title == 'Home — First Institute of Reliable Software'
join = driver.find_element(By.XPATH,"//b[contains(text(),'Join!')]").text
assert join == "Join!"
cert = driver.find_element(By.XPATH, "//a[contains(text(),'Certification for Fortifier')]")
certif = cert.text
assert cert.is_displayed()
assert certif == 'Certification for Fortifier'


# login_btn = driver.find_element(By.CLASS_NAME, "btn btn-primary btn-lg px-4 me-md-2")
# login_btn.click()

driver.close()
# driver.findElement(By.className("className"));
# driver.findElement(By.cssSelector(".className"));
# driver.findElement(By.id("elementId"));
# driver.findElement(By.linkText("linkText"));
# driver.findElement(By.name("elementName"));
# driver.findElement(By.partialLinkText("partialText"));
# driver.findElement(By.tagName("elementTagName"));
# driver.findElement(By.xpath("xPath"));

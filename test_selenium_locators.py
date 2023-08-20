from datetime import date
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
First_Name_input: str = 'John'
Last_Name_input: str = 'Smith'
nick_name_input: str = 'the_white_rabbit'
FirstName_locator: str = "//input[@id='firstName']"
LastName_locator: str = "//input[@id='lastName']"
UserName_locator: str = "//input[@id='username']"
Email_locator: str = "//input[@id='email']"
MAIL_input: str = 'first@second.com'
ADDRESS_input: str = "123 Really Main St."
Address_locator: str = "//input[@id='address']"
Country_locator = "//select[@id='country']"
us_dropdown_locator = "//option[contains(text(),'United States')]"
california_locator = "//option[contains(text(),'California')]"
State_locator = "//select[@id='state']"
ZIP_locator = "//input[@id='zip']"
ZIP_value_input = 90210
today = date.today()
CC_NAME = "Cardholder's Name"
CC_NUMBER = '1234 4567 8901 2345'
CC_EXPIRATION = '12/24'
CC_CVV = '951'
second_product_css_locator = '/html/body/div[2]/div[2]/div[1]/ul/li[2]/span'
PROMO_CODE = '1IRS'
copyrights_locator = "//span[contains(text(),'© 2017—2023 First Institute of Reliable Software')]"


# 1. Открыть сайт https://www.1irs.net/education/selenium-playground
def test_selenium():
    driver.get("https://www.1irs.net/education/selenium-playground")
    driver.fullscreen_window()

    # 2. В поле First Name и Last Name ввести ваше имя и фамилию. Здесь и далее можно вводить вымышленную информацию,
    # чтобы сберечь вашу приватность.
    first_name_field = driver.find_element(By.XPATH, FirstName_locator)
    first_name_field.send_keys(First_Name_input)

    last_name_field = driver.find_element(By.XPATH, LastName_locator)
    last_name_field.send_keys(Last_Name_input)

    # 3. В поле Username ввести ваш никнейм.
    user_name_field = driver.find_element(By.XPATH, UserName_locator)
    user_name_field.send_keys(nick_name_input)

    # 4. В поле Email ввести вашу почту. (Напомню, что можно вымышленную.)
    email = driver.find_element(By.XPATH, Email_locator)
    email.send_keys(MAIL_input)

    # 5. Заполнить Address.
    address = driver.find_element(By.XPATH, Address_locator)
    address.send_keys(ADDRESS_input)

    # 6. В поле Country выбрать United States.
    country = driver.find_element(By.XPATH, Country_locator)
    us_dropdown = country.find_element(By.XPATH, us_dropdown_locator)
    us_dropdown.click()

    # 7. В поле State выбрать California.
    state = driver.find_element(By.XPATH, State_locator)
    state_dropdown = state.find_element(By.XPATH, california_locator)
    state_dropdown.click()

    # 8. В поле Zip ввести число и дату в формате ДДММ.
    # Якщо день має значення < 10 тоді додаємо нуль до цифри.
    if today.day < 10:
        day = '0' + str(today.day)
    else:
        day = str(today.day)
    # Якщо місяць має значення < 10 тоді додаємо нуль до цифри.
    if today.month < 10:
        month = '0' + str(today.month)
    else:
        month = str(today.month)

    zip_code = driver.find_element(By.XPATH, ZIP_locator)
    zip_code.send_keys(f"{ZIP_value_input} {day}{month}")

    # 9. Выбрать галочку Save this information for next time.

    save_info: WebElement = driver.find_element(By.ID, "save-info")
    WebDriverWait(driver, 5).until(visibility_of(save_info))
    save_info.click()

    # 10. Выбрать Debit card как способ оплаты.
    #credit_card: WebElement = driver.find_element(By.XPATH, '//*[@id="credit"]')
    #ActionChains(driver)\
    #.move_to_element(credit_card)\
    #.perform()
    debit_card: WebElement = driver.find_element(By.XPATH, '//*[@id="debit"]')
    WebDriverWait(driver, 5).until(visibility_of(debit_card))
    debit_card.click()

    # Name
    # 11. Заполнить информацию о кредитной карте.
    cc_name = driver.find_element(By.ID, "cc-name")
    cc_name.send_keys(CC_NAME)
    # Number
    cc_number = driver.find_element(By.ID, "cc-number")
    cc_number.send_keys(CC_NUMBER)
    # Expiration
    cc_expiration = driver.find_element(By.ID, "cc-expiration")
    cc_expiration.send_keys(CC_EXPIRATION)
    # CVV
    cc_cvv = driver.find_element(By.ID, "cc-cvv")
    cc_cvv.send_keys(CC_CVV)

    # 12. Ввести промокод: 1IRS.
    promo_code = driver.find_element(By.XPATH, "//input[@placeholder='Promo code']")
    promo_code.send_keys(PROMO_CODE)

    # 13. Прочитать со страницы стоимость Second product и распечатать на экране.
    second_product_price = driver.find_element(By.XPATH, second_product_css_locator)
    price = second_product_price.text
    print(f"Стоимость Second product: {price}")

    # 14. Прочитать со страницы и распечатать текст копирайта (© 2021 First Institute of Reliable Software).
    copyrights = driver.find_element(By.XPATH, copyrights_locator)
    copyrights_text = copyrights.text
    print(f"Текст копирайта: {copyrights_text}")
    driver.close()

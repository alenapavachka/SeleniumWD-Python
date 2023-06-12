from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import time
from faker import Faker
from selenium.webdriver.common.keys import Keys

fake = Faker()

driver = webdriver.Chrome()

driver.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

driver.find_element(By.ID, "input-firstname").send_keys(fake.first_name())
driver.find_element(By.ID, "input-lastname").send_keys(fake.last_name())
driver.find_element(By.ID, "input-email").send_keys(fake.email())
driver.find_element(By.ID, "input-telephone").send_keys(fake.phone_number())

fakePassword = fake.password()

driver.find_element(By.ID, "input-password").send_keys(fakePassword)

driver.find_element(By.ID, "input-confirm").send_keys(fakePassword)

driver. find_element(By.XPATH, "//label[contains(text(),'Yes')]").click()

driver.find_element(By.XPATH, "//label[contains(text(), 'I have read and agree')]").click()

driver.find_element(By.XPATH, "//input[@value='Continue']").click()

try:
    assert driver.title == 'Your Account Has Been Created!'
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('Title has been changed. The new title is: ', driver.title)

driver.find_element(By.XPATH, '//*[@class="btn btn-primary"]').click()

try:
    assert driver.title == 'My Account'
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('The title of the page is different. Current title is: ', driver.title)

driver.find_element(By.XPATH, '//i[@class="fas fa-2x mb-1 fa-user-edit"]')

driver.find_element(By.LINK_TEXT, "Edit Account").click()
time.sleep(1)

try:
    assert driver.title == 'My Account Information'
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('The title of the page is different. Current title is: ', driver.title)

# double-click the First Name field = select all text
firstName = driver.find_element(By.ID, "input-firstname")
action = ActionChains(driver)
action.double_click(on_element=firstName)
action.perform()

# press delete on the keyboard
firstName.send_keys(Keys.BACKSPACE)

firstName.send_keys(fake.first_name())

# double-click the Last Name field = select all text

lastName = driver.find_element(By.ID, "input-lastname")
action = ActionChains(driver)
action.double_click(on_element=lastName)
action.perform()

# press delete on the keyboard
lastName.send_keys(Keys.BACKSPACE)

lastName.send_keys(fake.last_name())

driver.find_element(By.XPATH, "//input[@value='Continue']").click()

driver.find_element(By.XPATH, "//div[contains(text(), ' Success: Your account has been successfully updated.')]")

driver.find_element(By.XPATH,"//i[@class = 'fas fa-check-circle']")

driver.find_element(By.LINK_TEXT,'Address Book').click()

try:
    assert driver.title == 'Address Book'
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('The title is different. Current title is: ', driver.title)

try:
    assert driver.current_url == 'https://ecommerce-playground.lambdatest.io/index.php?route=account/address'
    print('The address book page URL is correct. Current URL is: ', driver.current_url)
except AssertionError:
    print('The Url of the current page has been changes. Current Url is: ', driver.current_url)

driver.find_element(By.XPATH, '//h1[contains(text(), "Address Book Entries")]')

driver.find_element(By.XPATH, '//a[contains(text(), "New Address")]').click()
driver.find_element(By.XPATH, '//a[contains(text(), "Back")]').click()

time.sleep(1)

driver.find_element(By.XPATH, '//span[contains(text(), "Home")]').click()

try:
    assert driver.title == "Your Store"
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('The title of the page is different. Current title is: ', driver.title)

try:
    assert driver.find_element(By.XPATH, '//img[@alt = "Canon DSLR camera"]')
    print("Canon DSLR camera photo is present.")
except AssertionError:
    print("The photo is not found")

driver.quit()




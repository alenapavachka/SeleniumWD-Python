import random
import time
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

fake = Faker('en_US')
driver = webdriver.Chrome()

driver.get('http://www.123formbuilder.com/form-5012215/online-order-form')

driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

try:
    assert driver.title == 'Online Order Form'
    print('The title is correct. Current title is: ', driver.title)
except AssertionError:
    print('The title of the page is different. Current title is: ', driver.title)

driver.find_element(By.XPATH, '//h1[contains(text(), "Order Form")]')
print("This is an Order Form")

# first name
driver.find_element(By.XPATH, "//input[@placeholder = 'First']").send_keys(fake.first_name())

# last name
driver.find_element(By.XPATH, "//input[@placeholder = 'Last']").send_keys(fake.last_name())

# email
driver.find_element(By.XPATH, "//input[@type = 'email']").send_keys(fake.email())

# phone
driver.find_element(By.XPATH, "//input[@placeholder = '### ### #### ']").send_keys(fake.msisdn())

# choose
driver.find_element(By.XPATH, '//span[contains(text(), "# Product 3")]').click()

# quantity
driver.find_element(By.XPATH, "//input[@type = 'number' and @data-role ='i123-input']").send_keys(
    random.randint(1, 999))

time.sleep(1)

text = driver.find_element(By.ID, 'dropdown-00000015-acc')
action = ActionChains(driver)
action.move_to_element(text).perform()

# date
driver.find_element(By.XPATH, "//div[@data-role = 'expander']").click()
time.sleep(0.5)
driver.find_element(By.XPATH, "//div[@data-day = '29']").click()

# delivery address
driver.find_element(By.XPATH, "//input[@placeholder = 'Street Address']").send_keys(fake.address())
driver.find_element(By.XPATH, "//input[@placeholder = 'City']").send_keys(fake.city())
driver.find_element(By.XPATH, '//input[@placeholder = "Region"]').send_keys(fake.state())
driver.find_element(By.XPATH, "//input[@placeholder = 'Postal / Zip Code']").send_keys(fake.postcode())

driver.find_element(By.XPATH, "//input[@placeholder = 'Country']").click()
driver.find_element(By.XPATH, "//input[@placeholder = 'Country']").send_keys("United States", Keys.ARROW_DOWN,
                                                                             Keys.ENTER)
time.sleep(0.5)
text = driver.find_element(By.ID, 'captcha-00000004-acc')
action = ActionChains(driver)
action.move_to_element(text).perform()

# dropdown
driver.find_element(By.XPATH, "//div[@data-type = 'dropdown']").click()
driver.find_element(By.XPATH, "//option[@value = 'Choice3']").click()
time.sleep(0.5)

# multiple choice
driver.find_element(By.XPATH, '//span[contains(text(), "Choice 2")]').click()
driver.find_element(By.XPATH, '//span[contains(text(), "Choice 3")]').click()

# verification we can't do


text = driver.find_element(By.XPATH, '//div[@class= "abuse-disclaimer"]')
action = ActionChains(driver)
action.move_to_element(text).perform()

driver.find_element(By.XPATH, '//button[@type= "submit"]').click()

time.sleep(1)

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

try:
    assert driver.find_element(By.XPATH, '//label[contains(text(), "Please prove that you are not a robot.")]')
    print("'Please prove that you are not a robot.' is present on the page. Form was filled out successfully exept "
          "the reCAPTCHA field.")
except AssertionError:
    print("No such a text found. Double check the form.")

driver.quit()

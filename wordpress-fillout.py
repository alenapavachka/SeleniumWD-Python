import string

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import random
import time
from faker import Faker
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

fake = Faker()

driver.get(' https://qasvus.wordpress.com')

driver.maximize_window()
driver.minimize_window()
driver.maximize_window()

try:
    assert driver.title == "California Real Estate – QA at Silicon Valley Real Estate"
    print("The title is correct. current title is: ", driver.title)
except AssertionError:
    print("The title has been changed. current title is: ", driver.title)

text = driver.find_element(By.XPATH, '//button[@type = "submit"]')
action = ActionChains(driver)
action.move_to_element(text).perform()

driver.find_element(By.ID, "g2-name").send_keys(fake.first_name())
driver.find_element(By.ID, "g2-email").send_keys(fake.email())
res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits + string.ascii_uppercase, k=300))

driver.find_element(By.ID, "contact-form-comment-g2-message").send_keys(res)

driver.find_element(By.XPATH, '//button[@type = "submit"]').click()

time.sleep(0.5)

try:
    assert driver.find_element(By.ID, 'contact-form-success-header')
    print('"Your message has been sent" confirmation is on the page.')
except AssertionError:
    print("Expected message is missing.")

driver.find_element(By.LINK_TEXT, 'Go back'). click()

try:
    assert driver.title == 'California Real Estate – QA at Silicon Valley Real Estate'
    print("The title is correct. Current title is: ", driver.title)
except AssertionError:
    print("The title has been changed. Current title is: ", driver.title)

try:
    assert driver.find_element(By.XPATH, '//img[@class = "wp-block-cover__image-background wp-image-54"]')
    print("You can check the picture by click on the following link: "
          "https://qasvus.files.wordpress.com/2019/09/key-2323278_1920.jpg")
except AssertionError:
    print('The image was not found')


try:
    assert driver.find_element(By.LINK_TEXT,'California Real Estate')
    print('"California Real Estate" link is present on the page.')
except AssertionError:
    print("The link is missing")


try:
    assert driver.find_element(By.XPATH,"//p[@class = 'site-description']")
    print('"QA at Silicon Valley Real Estate" paragraph is present on the page.')
except AssertionError:
    print("The paragraph is missing")

driver.quit()
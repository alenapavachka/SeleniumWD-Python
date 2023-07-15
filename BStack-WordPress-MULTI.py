# coding=utf8
import random
from dotenv import load_dotenv
import os
from faker import Faker
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.safari.options import Options as SafariOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from threading import Thread
from selenium.common.exceptions import WebDriverException
import my_key as key


load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "xxxxxxxxx"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "os": "OS X",
        "osVersion": "Ventura",
        "sessionName": "BStack WordPress Multi",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
{
        "browserName": "Firefox",
        "browserVersion": "112.0",
        "os": "Windows",
        "osVersion": "10",
        "sessionName": "BStack WordPress Multi",
        "buildName": BUILD_NAME,
    },
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "OS X",
        "osVersion": "Catalina",
        "sessionName": "BStack WordPress Multi",  # test name
        "buildName": BUILD_NAME,  # Your tests will be organized within this build
    },
]


def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        "firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        "safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)

    time.sleep(2)

    try:
        time.sleep(random.randint(1, 3))

        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        time.sleep(random.randint(1, 3))

        # Do assertion for driver title after main page getting open
        # Print driver title with custom explanation string
        try:
            assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
            print("The title of the target page is correct. Current title is: ", driver.title)
        except AssertionError:
            print("The title of the target page is INCORRECT. Current title is: ", driver.title)

        # Clear fields: Text area, Name, Email
        # Fill out all fields and click on Submit button
        driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.PAGE_DOWN)

        search = driver.find_element(By.ID, "g2-name")
        search.clear()
        search.send_keys(fake.first_name())

        search = driver.find_element(By.ID, "g2-email")
        search.clear()
        search.send_keys(fake.email())

        search = driver.find_element(By.ID, "contact-form-comment-g2-message")
        search.clear()
        search.send_keys(fake.text())

        driver.find_element(By.XPATH, '//button[@type = "submit"]').click()

        time.sleep(random.randint(1, 3))

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")
        # driver.quit()

        if "California Real Estate – QA at Silicon Valley Real Estate" in driver.title:
            driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": '
                '"The test has PASSED! The scrip is fully executed!"}}')


    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')
    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')
    # Stop the driver
    driver.quit()


for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()

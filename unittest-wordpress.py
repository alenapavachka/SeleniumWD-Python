from faker import Faker
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import random
import unittest
import time
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service


def delay():
    time.sleep(random.randint(1, 3))


class ChromeSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_wordpress_chrome(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def test_wordpress_chrome_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

    def test_wordpress_edge(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def test_wordpress_edge_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()

    def test_wordpress_firefox(self):
        driver = self.driver
        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def test_wordpress_firefox_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get("https://qasvus.wordpress.com/")

        fake = Faker()

        delay()

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

        delay()

        # Use "wait.until" method for visibility of "Go Back" link
        wait = WebDriverWait(driver, 5)
        wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Go back')))
        print("'Go back' link is visible")

        assert "California Real Estate – QA at Silicon Valley Real Estate" in driver.title
        print("The title is: ", driver.title)

        wait.until(EC.visibility_of_element_located((By.ID, "contact-form-success-header")))
        print("'Your message has been sent' is present on the page")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

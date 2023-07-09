from selenium import webdriver
import requests
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
import helpers as hp

hp.delay_1_5()


class ChromeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()

    def test_wiki_bread_chrome(self):
        driver = self.driver

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, "searchInput")))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def test_wiki_bread_chrome_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, hp.sb_loc)))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def tearDown(self):
        self.driver.quit()


class EdgeSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()

    def test_wiki_bread_edge(self):
        driver = self.driver

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, hp.sb_loc)))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def test_wiki_bread_edge_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, hp.sb_loc)))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def tearDown(self):
        self.driver.quit()


class FirefoxSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.minimize_window()
        self.driver.maximize_window()

    def test_wiki_bread_firefox(self):
        driver = self.driver

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, hp.sb_loc)))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def test_wiki_bread_firefox_1820x1050(self):
        driver = self.driver
        driver.set_window_size(1820, 1050)

        driver.get(hp.g_url)

        wait = WebDriverWait(driver, 3)

        try:
            wait.until(EC.visibility_of_element_located((By.NAME, "q")))
            print("The search bar is present on the page.")
        except TimeoutException:
            print("The loading of the page took too long (more than 3 seconds).")
            driver.get_screenshot_as_file("google_page_loading_error.png")

        assert "Google" in driver.title
        print("The title is correct. Current title is: ", driver.title)

        print("Google URL has", requests.get(hp.g_url).status_code, "as a status code")
        code = requests.get(hp.g_url).status_code
        try:
            assert code == 200
            print("API response is 200")
        except AssertionError:
            print("API response is not 200. It is: ", code)

        hp.delay_1_5()

        search_bar = driver.find_element(By.NAME, 'q')
        search_bar.clear()
        search_bar.send_keys("wikipedia", Keys.RETURN)

        driver.implicitly_wait(5)

        wait.until(EC.element_to_be_clickable((By.XPATH, hp.wiki_loc)))
        print("'Wikipedia' link is clickable.")
        driver.find_element(By.XPATH, hp.wiki_loc).click()

        hp.delay_1_5()

        self.assertIn('Wikipedia', driver.title)
        print("Wikipedia has ", driver.title, " as the page title")

        code_wiki = requests.get(hp.wiki_link).status_code
        print("Wikipedia  has", code_wiki, "as a status code")

        try:
            assert code_wiki == 200
            print("API response from Wikipedia page is as expected. It is: ", code_wiki)
        except AssertionError:
            print("API response is not 200. It is: ", code_wiki)

        hp.delay_1_5()

        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, hp.logo_loc)))
        print("The central Wiki logo is visible.")
        wait.until(EC.visibility_of_element_located((By.XPATH, hp.heading_loc)))
        print("'Wikipedia' heading is present on the yop of the page.")
        wait.until(EC.visibility_of_element_located((By.ID, hp.sb_loc)))
        print("Wiki search bar is visible.")

        search_bar_wiki = driver.find_element(By.ID, hp.sb_loc)
        search_bar_wiki.clear()
        search_bar_wiki.send_keys("bread", Keys.RETURN)

        wait.until(EC.visibility_of_element_located((By.XPATH, hp.b_heading_loc)))
        print("The bread page has its heading:",
              driver.find_element(By.XPATH, hp.b_heading_loc).text)

        hp.delay_1_5()

        self.assertIn("Bread - Wikipedia", driver.title)
        print("The page has", driver.title, " as the title")
        if "Bread - Wikipedia" not in driver.title:
            raise Exception("Wikipedia BREAD page title is INCORRECT!")

        driver.find_element(By.XPATH, hp.b_pic_loc).click()

        hp.delay_1_5()

        try:
            wait.until(EC.presence_of_element_located(
                (By.XPATH, hp.b_pic_loc)))
            print("Wikipedia Bread Pic is visible.")
            driver.get_screenshot_as_file('Screenshot_Bread.png')
        except TimeoutException:
            print("Can't find the Element.")
            driver.get_screenshot_as_file('bread_page_loading_error.png')
            driver.implicitly_wait(5)

        assert "Korb mit Brötchen - Bread - Wikipedia" in driver.title
        print("The title of the current page is: ", driver.title)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

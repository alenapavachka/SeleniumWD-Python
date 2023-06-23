from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException as WDE


driver = webdriver.Chrome()

driver.get("https://www.google.com/")
driver.maximize_window()
driver.minimize_window()
driver.maximize_window()


# check the URL
try:
    assert driver.current_url == "https://www.google.com/"
    print("The URL is correct. Current URL is: ", driver.current_url)
except AssertionError:
    print("The URL is not matching. Current URL is: ", driver.current_url)

# check the logo
print("This is page central logo -", driver.find_element(By.TAG_NAME, "img").get_attribute("src"))

# check the Google search button presence
print("This is the button - ", driver.find_element(By.NAME, "btnK").get_attribute("value"))

# check the Google search button presence
print("This is the button - ", driver.find_element(By.NAME, "btnI").get_attribute("value"))

driver.implicitly_wait(2)

driver.find_element(By.XPATH, "//textarea[@name = 'q']").send_keys("abc", Keys.ENTER)

# find the link
driver.find_element(By.PARTIAL_LINK_TEXT, "ABC Home Page - ABC.com").click()

time.sleep(2)

try:
    assert "ABC Home Page - ABC.com" in driver.title
    print("The page title is correct.Current title is: ", driver.title)
except AssertionError:
    print("The title is different. Current title is:  ", driver.title)

print("The abc logo is present: ", driver.find_element(By.XPATH, "//img[@class = 'sitelogo']").get_attribute("src"))

driver.set_page_load_timeout(5)

driver.find_element(By.TAG_NAME, "html").send_keys(Keys.ESCAPE)
time.sleep(2)

driver.find_element(By.LINK_TEXT, "Browse").click()
time.sleep(1)

driver.find_element(By.LINK_TEXT, "The Bachelorette").click()

# the show assertion
try:
    assert "Watch The Bachelorette TV Show - ABC.com" in driver.title and "https://abc.com/shows/the-bachelorette" == driver.current_url
    print("The title of the page is correct. Current title is: ", driver.title)
    print("The URL of the page is correct. Current URL is: ", driver.current_url)
except AssertionError:
    print("The title of the page is incorrect. Current title is: ", driver.title)
    print("The URL of the page is incorrect. Current URL is: ", driver.current_url)

# the logo
print("The logo of the show is present: ", driver.find_element(By.XPATH, "//img[@class = 'Header__Logo__img' ]").get_attribute("src"))

try:
    assert driver.find_element(By.XPATH, "//div[contains(text(),'SEASON PREMIERE MON JUNE 26')]")
    print("SEASON PREMIERE MON JUNE 26")
except AssertionError:
    print("The release date ios not present or was changed.")


driver.quit()

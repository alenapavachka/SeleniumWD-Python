# SeleniumWD-Python
Automated Selenium scripts.
SELENIUM COMMANDS


from selenium import webdriver (always the first one)
from faker import Faker (the library when we need to input data: name, email,etc)
from selenium.webdriver.common.by import By (search by a locator)
driver = webdriver.Chrome() (a variable that is gonna do all the actions; Chrome() - is a method here)
driver.get(“https://www.google.com") (go to a certain page/ url; Default wait time is 30 sec)
driver.maximize_window() (to enlarge the window)
print(driver.title) (to print the tile of the the page)
print(driver.current_url) (to print the URL of the page)
driver.find_element(By.XPATH, ‘//img[@alt="Google"]') (By is a separate library, here we are asking to find an element by. Its Path)
driver.quit() (fully exits the browser/ we can you use ‘close’ but this one will only close the current tab)
driver.find_element(By.ID, “input-firstname”).first_name.send_keys(fake.first_name()) (find and element and input data in it)
random_email = str(random.randint(0, 99999)) + “myemail@example.com" (creating manuals a random email address: random.randint (0, 99999) turning into a string and then concatenating it with the remaining part)
time.sleep(0.5) (gives time to an element to appear or page to open)

# SeleniumWD-Python
Automated Selenium scripts.

## SELENIUM LIBRARIES 


- **from selenium import webdriver** *(always the first one)*
- **from faker import Faker** *(the library when we need to input data: name, email,etc)*
- f**rom selenium.webdriver.common.by import By** *(search by a locator)*
- **from selenium.webdriver import ActionChains** *(actions such as double click)*
- **from selenium.webdriver.common.keys import Keys** *(keybord entries)*

## **SELENIUM COMMANDS**

**driver** = webdriver.Chrome()** *(a variable that is gonna do all the actions; Chrome() - is a method here)*
- **driver.get**(“https://www.xxxxx.com") *(go to a certain page/ url; Default wait time is 30 sec)*
- **driver.maximize_window()** *(to enlarge the window)*
- **driver.title** *(to print the tile of the the page)*
- **driver.current_url** (*to print the URL of the page)*
- **driver.find_element(By.XPATH, ‘//img[@alt="Google"]')** *(By is a separate library, here we are asking to find an element by its XPath)*
- **driver.quit()** *(fully exits the browser/ we can you use ‘close’ but this one will only close the current tab)*
- r**andom_email = str(random.randint(0, 99999)) + “myemail@example.com"** *(creating manuals a random email address: random.randint (0, 99999) turning into a string and then concatenating it with the remaining part)*
- **time.sleep(0.5)** *(gives time to an element to appear or page to open)*
- ***element* = driver.find_element(By.ID, "input-element")  
action = ActionChains(driver)  
action.double_click(on_element=*element*)  
action.perform**() *(to double-click an element)*
- **res = ''.join(random.choices(string.ascii_lowercase +  
string.digits + string.ascii_uppercase, k=N))** *(randomly generated string)*

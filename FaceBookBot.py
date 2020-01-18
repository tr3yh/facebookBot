# -------------------------------------------------------------------#
# Facebook bot v1.0: Make a single statically defined facebook post. #
#--------------------------------------------------------------------#
#  To do list: 
#   * Build SQL backend for future posts
#   * Build in SQL post scheduler 

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.firefox.options import Options

# Headless mode not currently working
options = Options()
options.headless = True
# Load firefox driver. If using Chrome or another browser, that respective driver will need to be loaded.
driver = webdriver.Firefox(executable_path=r'C:\Scripts\FacebookBot\geckodriver.exe') # Make this path match your install location or statically assign the PATH variable for the driver
driver.get('https://facebook.com')
# Define the username, password, and login button fields
emailElement = driver.find_element(By.XPATH,'.//*[@id="email"]')
pwElement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
loginButton = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]') 
# Enter your credentials <INPUT YOUR CREDS HERE>. This of course can be improved upon by utilizing a more secure credential storing method...
emailElement.send_keys('your email here')
pwElement.send_keys('your password here')
# Login
loginButton.click()

# Define the status typing field
statusElement = driver.find_element(By.XPATH, './/*[@name="xhpc_message"]')
time.sleep(5)
# Statically assigned post. This is what the bot will type.
statusElement.send_keys('This is a sample post')
time.sleep(5)

# Define the post button and post the status
postButton = driver.find_elements_by_tag_name('button')
time.sleep(5)
for postButtons in postButton:
    if postButtons.text == 'Post':
        postButtons.click()
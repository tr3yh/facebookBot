#!/usr/bin/env python3
# -------------------------------------------------------------------#
# Facebook bot v1.1: Make a single statically defined facebook post. #
#--------------------------------------------------------------------#
# Updates:                                                           #
# Added credential storage into environmental variables              #
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
import pprint
import os

# Define environmental variable and credentials
env_var = os.environ
fb_user = (env_var['FB_USER'])
fb_pass = (env_var['FB_PASS'])

# Load firefox driver in headless mode.
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.get('https://facebook.com')

# Define the username, password, and login button fields
emailElement = driver.find_element(By.XPATH,'.//*[@id="email"]')
pwElement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
loginButton = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]') 

# Grab credentials from env_var and login
emailElement.send_keys(fb_user)
pwElement.send_keys(fb_pass)
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

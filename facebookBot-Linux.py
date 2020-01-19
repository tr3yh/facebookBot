#!/usr/bin/env python3
# -------------------------------------------------------------------#
# Facebook bot v1.1: Post Random Quote from The Office               #
#--------------------------------------------------------------------#
# Updates:                                                           #
# * Added credential storage into environmental variables            #
# * Built mysql backend for future posts                             #
# -------------------------------------------------------------------# 
# To do:                                                             #
# * Build in post scheduler for 1x each day                          #
# * Add mysql creds to env_var                                       #
# * Clean up code with methods                                       #
#--------------------------------------------------------------------#
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.firefox.options import Options
import pprint
import os
import mysql.connector

# Define environmental variable and credentials
env_var = os.environ
fb_user = (env_var['FB_USER'])
fb_pass = (env_var['FB_PASS'])

# Load firefox driver in headless mode.
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()
driver.get('https://facebook.com')

# Define the username, password, and login button fields
emailElement = driver.find_element(By.XPATH,'.//*[@id="email"]')
pwElement = driver.find_element(By.XPATH,'.//*[@id="pass"]')
loginButton = driver.find_element(By.XPATH,'.//*[@id="loginbutton"]') 

# Grab credentials from env_var and login
emailElement.send_keys(fb_user)
pwElement.send_keys(fb_pass)
loginButton.click()
print("Logged in")
# Define the status typing field
statusElement = driver.find_element(By.XPATH, './/*[@name="xhpc_message"]')
print("Time to sleep")
time.sleep(3)
print("Done sleeping, let's connect to DB")
# Statically assigned post. This is what the bot will type.
#statusElement.send_keys('This is a sample post')
#time.sleep(5)

# Connect to DB and post a random quote from The Office
import mysql.connector
config = {
  'user': 'username',
  'password': 'password',
  'host': '127.0.0.1',
  'database': 'osint',
  'raise_on_warnings': True
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()
query = ("SELECT quote, quotee FROM theOffice ORDER BY RAND() LIMIT 1;")
cursor.execute(query)
results = cursor.fetchall()

for result in results:
    list = "%s ~ %s" % result

print("Time to print the results")
statusElement.send_keys(list)
print("Napping for 3")
time.sleep(3)
print("Alright! Time to hit the post button")
# Define the post button and post the status
postButton = driver.find_elements_by_tag_name('button')
time.sleep(5)
for postButtons in postButton:
    if postButtons.text == 'Post':
        postButtons.click()

cursor.close()
cnx.close()

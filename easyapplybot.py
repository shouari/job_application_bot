from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import json

with open('credential.json') as f:
    credential = json.loads(f.read())
username = credential['username']
password = credential['password']

chromedriver_autoinstaller.install()

browser = webdriver.Chrome()
browser.get("http://www.linkedin.com")

userElem = browser.find_element_by_id('session_key')
userElem.send_keys(username)
passwordElm = browser.find_element_by_id('session_password')
passwordElm.send_keys(password)
passwordElm.submit()
browser.implicitly_wait(10)
browser.find_element_by_id('ember367').click()
browser.implicitly_wait(3)
jobElem = browser.find_element_by_id('ember29')
jobElem.click()

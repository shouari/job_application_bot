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

# def start_linkedin():

chromedriver_autoinstaller.install()
browser = webdriver.Chrome()
browser.get("http://www.linkedin.com")


userElem = browser.find_element_by_id('session_key')
userElem.send_keys(username)
passwordElm = browser.find_element_by_id('session_password')
passwordElm.send_keys(password)
passwordElm.submit()

browser.implicitly_wait(3)
jobElem = browser.find_element_by_id('ember29')
jobElem.click()

    # todo Find a way to close the message pop up.
    # browser.implicitly_wait(5)
    # closeMessage = browser.find_elements_by_class_name('msg-overlay-bubble-header__control msg-overlay-bubble-header__control--new-convo-btn artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--1 artdeco-button--tertiary ember-view')
    # closeMessage.click()
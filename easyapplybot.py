from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
import json
import time


with open('data.json') as f:
    data = json.loads(f.read())
username = data['username']
password = data['password']
job_title = data['job_title']
city =data['city']
country = data['country']
# def start_linkedin():

chromedriver_autoinstaller.install()
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
#Disable webdriver flags or you will be easily detectable
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")

browser = webdriver.Chrome()
browser.get("http://www.linkedin.com")



userElem = browser.find_element_by_id('session_key')
userElem.send_keys(username)
time.sleep(1)
passwordElm = browser.find_element_by_id('session_password')
passwordElm.send_keys(password)
time.sleep(1)
passwordElm.submit()

browser.implicitly_wait(4)
jobElem = browser.find_element_by_id('ember29')
jobElem.click()

#todo: find a way to minimize the message popup
# closeMessage = browser.find_elements_by_xpath("//button[contains(@id,'msg-overlay-bubble-header__control')]")
# closeMessage.click()
job_titleElem = browser.find_element_by_xpath("//input[starts-with(@id,'jobs-search-box-keyword-id')]")
time.sleep(2)
job_titleElem.send_keys(job_title + Keys.TAB)
time.sleep(2)

job_locationElem = browser.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-location-id')]")
job_locationElem.send_keys(city + ',' + country + Keys.TAB + Keys.ENTER)
URL= browser.current_url
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all(class_="mr1"))


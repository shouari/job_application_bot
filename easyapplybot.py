from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
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
city = data['city']
country = data['country']
# def start_linkedin():

chromedriver_autoinstaller.install()
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--ignore-certificate-errors")
options.add_argument('--no-sandbox')
options.add_argument("--disable-extensions")
# Disable webdriver flags or you will be easily detectable
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

try:
    if browser.find_element_by_class_name('msg-overlay-list-bubble--is-minimized') is not None:
        pass
except NoSuchElementException:
    try:
        if browser.find_element_by_class_name('msg-overlay-bubble-header') is not None:
            browser.find_element_by_class_name('msg-overlay-bubble-header').click()
    except NoSuchElementException:
        pass

browser.get('https://www.linkedin.com/jobs/')


job_titleElem = browser.find_element_by_xpath("//input[starts-with(@id,'jobs-search-box-keyword-id')]")
time.sleep(2)
job_titleElem.send_keys(job_title + Keys.TAB)
time.sleep(2)

job_locationElem = browser.find_element_by_xpath("//input[starts-with(@id, 'jobs-search-box-location-id')]")
job_locationElem.send_keys(city + ',' + country + Keys.TAB + Keys.ENTER)


# def get_easy_apply_button():
#     try :
#         button = browser.find_elements_by_xpath(
#                     '//button[contains(@label, "LinkedIn Features")]/span[1]'
#                     )
#         button.click()
#
#         EasyApplyButton = button [0]
#     except :
#         EasyApplyButton = False
#
#     return EasyApplyButton

def get_job_description( jobID):

    job = 'https://www.linkedin.com/jobs/view/' + str(jobID)
    browser.get(job)

    job_des = browser.find_element_by_xpath("//*[@id='job-details']")
    job_description = job_des.get_attribute('innerHTML')
    soup = BeautifulSoup(job_description.strip())

    return soup.get_text()


def load_page(sleep=1):
    scroll_page = 0
    while scroll_page < 4000:
        browser.execute_script("window.scrollTo(0," + str(scroll_page) + " );")
        scroll_page += 200
        time.sleep(sleep)

    if sleep != 1:
        browser.execute_script("window.scrollTo(0,0);")
        time.sleep(sleep * 3)

    page = BeautifulSoup(browser.page_source, features="xml")
    return page

load_page()

links = browser.find_elements_by_xpath('//div[@data-job-id]')
# get job ID of each job link
IDs = []

for link in links:
    children = link.find_elements_by_xpath(
        './/a[@data-control-name]'
    )
    for child in children:
        temp = link.get_attribute("data-job-id")
        jobID = temp.split(":")[-1]
        IDs.append(int(jobID))
IDs = set(IDs)

print(IDs)
count_job=0
# for i, jobID in enumerate(IDs):
#     count_job +=1
#     button = get_easy_apply_button()
#     if button is not False:
#         string_easy = "has Easy Apply "
#         print(jobID, string_easy)
#     else:
#         string_easy="Does not have easy apply"
#         print(jobID, string_easy)
for jobID in IDs:
    print(get_job_description(jobID))








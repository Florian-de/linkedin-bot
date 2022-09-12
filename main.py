from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

EMAIL = ""
PASSWORD = ""

chrome_driver = ""

driver = webdriver.Chrome(executable_path=chrome_driver)
driver.get(url="https://www.linkedin.com/")

#Login process
login_button = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
login_button.click()
time.sleep(2)

email_bar = driver.find_element(By.ID, "username")
email_bar.send_keys(EMAIL)

password_bar = driver.find_element(By.ID, "password")
password_bar.send_keys(PASSWORD)

confirm_button = driver.find_element(By.CLASS_NAME, "btn__primary--large")
confirm_button.click()
time.sleep(2)
#search jobs process
search_bar = driver.find_element(By.CLASS_NAME, "search-global-typeahead__input")
search_bar.send_keys("Engineer")
search_bar.send_keys(Keys.RETURN)
time.sleep(2)

alle_jobs_button = driver.find_element(By.CLASS_NAME, "app-aware-link")
alle_jobs_button.click()
time.sleep(2)

jobs = driver.find_elements(By.CLASS_NAME, "job-card-list__title")
print(jobs)
for job in jobs:
    print(job.text)


import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://www.conferenceseries.com/past-conference-reports.php')
driver.implicitly_wait(10)
list = driver.find_elements(By.CSS_SELECTOR, 'body > div > article > section.location-conf-main > div:nth-child(2) > div.list-group > a')

for l in list:
    print(l.text)

driver.quit()




import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import unittest

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
driver.get('https://lms.ou.edu.vn/')

driver.implicitly_wait(10)

driver.execute_script('window.scrollTo(250,0)')
driver.implicitly_wait(20)
driver.execute_script('window.scrollTo(250,0)')
driver.find_element(By.CLASS_NAME, 'main-btn').click()
driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()


username = driver.find_element(By.ID, 'form-username')
password = driver.find_element(By.ID, 'form-password')

with open('data/user.json') as ac:
    user = json.load(ac)
    username.send_keys(user['username'])
    password.send_keys(user['password'])

driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()

driver.save_screenshot('anh1.png')

# khoahoc = WebDriverWait(driver, 20).until(
#     ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a > span.multiline'))
# )

# khoahoc = WebDriverWait(driver, 20).until(
#     ec.presence_of_all_elements_located((By.CLASS_NAME, 'multiline'))
# )
#
# for k in khoahoc:
#     print(k.text)

# khoahoc = WebDriverWait(driver, 20).until(
#     driver.find_element(By.CSS_SELECTOR, 'a > span.multiline[1]')
# )
driver.implicitly_wait(10)
# driver.find_element(By.CSS_SELECTOR, '#page-container-1 > div > div > div:nth-child(2) > a').click()
driver.find_element(By.XPATH, '//*[@id="page-container-1"]/div/div/div[3]/a').click()
driver.save_screenshot('monhoc.png')


driver.quit()


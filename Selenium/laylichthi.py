import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))


driver.get('https://tienichsv.ou.edu.vn/')
driver.implicitly_wait(5000)
driver.find_element(By.CLASS_NAME, 'btn.btn-success ng-star-inserted').click()

driver.set_window_position(AllWindowHandles=driver.getWindowHandles())

username = driver.find_element(By.ID, 'form-username')
password = driver.find_element(By.ID, 'form-password')
with open('data/user.json') as ac:
    user = json.load(ac)
    username.send_keys(user['username'])
    password.send_keys(user['password'])
    driver.implicitly_wait(10)
driver.save_screenshot("login2.png")

# xemlichthi = driver.find_element(By.CSS_SELECTOR, 'body > app-root > div > div > div > div.contentshow.ng-star-inserted > div > div > div.frame_right.pr-0 > app-right > div > div.card-body.py-0.px-1 > app-chucnang > div > ul:nth-child(7) > li > div.text-cus.active > a:nth-child(1)')
# xemlichthi.click()
# chitiet = driver.find_elements(By.CSS_SELECTOR, '#excel-table > tbody > tr:nth-child')
# for i in chitiet:
#     print(i.text)
# driver.implicitly_wait(10)

print("done")
driver.save_screenshot("login3.png")
driver.implicitly_wait(10)
driver.quit()
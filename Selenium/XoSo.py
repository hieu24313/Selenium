from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))


driver.get('https://www.xskthcm.com/')

ngay = "08-04-2023" #nhập ngày

so = 96  #nhập số muốn dò
driver.implicitly_wait(5)


driver.find_element(By.CLASS_NAME, 'select2-arrow').click()
driver.implicitly_wait(3)

listngay = driver.find_elements(By.CSS_SELECTOR, '#select2-results-1 > li')
dem = 0
for i in listngay:
    dem = dem + 1
    s = i.text
    if(s == ngay):
        dc = '#select2-results-1 > li:nth-child(' + str(dem) + ')'
        driver.find_element(By.CSS_SELECTOR, dc).click()
        driver.implicitly_wait(5)
        driver.save_screenshot('xoso1.png')
        driver.implicitly_wait(5)
        kqso = driver.find_elements(By.CSS_SELECTOR, '#undefined > div.wrapper-outer > div > div.wrapper > div.wrapbox > div.clearfix > div > div > div > div.dks-main.col-md-9 > div > div > div > div > div > div.dk-widget-c > div > div.xs-slider.xs-slider-extraz > div > div > div > div > div > table > tbody > tr > td:nth-child(2)')
        for s in kqso:
            # if()
            print(s.text)
        break
driver.quit()







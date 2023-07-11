import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class MyTest(unittest.TestCase):

    def __int__(self, *args, **kwargs):
        super(MyTest, self).__init__(*args, **kwargs)
        driver = webdriver.Chrome(service=Service('venv/chromedriver.exe'))
        driver.get('https://lms.ou.edu.vn/')

    def TestLMS(self):
        self.driver.implicitly_wait(8)
        self.driver.find_element(By.CLASS_NAME, 'main-btn').click()
        self.driver.find_element(By.CLASS_NAME, 'login100-form-btn').click()

        # user_type = Select(self.driver.find_element(By.ID, 'form-usertype'))
        # user_type.select_by_index(0)


        username = self.driver.find_element(By.ID, 'form-username')
        password = self.driver.find_element(By.ID, 'form-password')

        username.send_keys("2051050138")
        password.send_keys("0359505026h")

        self.driver.find_element(By.CLASS_NAME, 'm-loginbox-submit-btn').click()

        self.driver.implicitly_wait(5)
        khoahoc = WebDriverWait(self.driver, 30).until(
            ec.presence_of_all_elements_located((By.CSS_SELECTOR, 'a > span.multiline'))
        )
        # khoahoc = driver.find_elements(By.CSS_SELECTOR, 'a > span.multiline')
        for k in khoahoc:
            # self.assertTrue(k.text.find("22") >= 0)
            print(k.text)

        self.driver.execute_script("Window.scrollTo(0,250)")
        self.driver.save_screenshot('lms.png')

        self.driver.quit()





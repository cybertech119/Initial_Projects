import time

import faker
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get("https://odin-web-qa.kiwi-internal.com/")
    request.cls.driver=driver
    request.cls.wait = wait
    yield
    driver.close()


@pytest.mark.usefixtures("setup")
class TestLoginPage():
    def test_Login_with_Dealer_admin_creditial(self):
        emailAddress = self.driver.find_element(By.XPATH, "//input[@id='emailAddress']")
        emailAddress.send_keys("rohit@yopmail.com")

        password = self.driver.find_element(By.XPATH, "//input[@id='userPassword']")
        password.send_keys("Kiwi@2018")

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()
        time.sleep(3)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@placement='end'][normalize-space()='Site Home']"))
        )
        # assert "Site Home" in driver.find_element(By.XPATH, "//a[@placement='end'][normalize-space()='Site Home']")

    def test_Login_with_System_admin_creditial(self):
        emailAddress = self.driver.find_element(By.XPATH, "//input[@id='emailAddress']")
        emailAddress.send_keys("Kannan.k@kiwitech.com")

        password = self.driver.find_element(By.XPATH, "//input[@id='userPassword']")
        password.send_keys("Kiwi@2018")

        self.driver.find_element(By.XPATH, "//button[normalize-space()='Log In']").click()
        time.sleep(3)
        self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//body/app-root/app-admin/div[@class='main-container']/app-sidebar/div[@class='sidebar']/ul[@class='nav nav-pills flex-column mb-auto']/li[1]/a[1]"))
        )
        # assert "Site Home" in driver.find_element(By.XPATH, "//a[@placement='end'][normalize-space()='Site Home']")
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

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
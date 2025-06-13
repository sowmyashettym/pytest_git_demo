import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Utils:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(timeout=10, driver=driver)
    def get_element_click(self,locator):
        self.wait.until(EC.presence_of_element_located(locator)).click()

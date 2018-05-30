from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random


class MainPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def filmpage_link(self):
        return self.driver.find_element_by_css_selector("a[href='/movies/11']")
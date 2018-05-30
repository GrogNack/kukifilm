from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random


class MainPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def filmpage_link(self):
        s = self.driver.find_elements(By.CSS_SELECTOR,"a.poster")
        count = random.randint(0,11)
        return s[count]
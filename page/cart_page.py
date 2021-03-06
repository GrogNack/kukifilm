from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class CartPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @property
    def remove_button(self):
        return self.driver.find_element(By.XPATH, "//*[@id='mycart']//i")

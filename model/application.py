from selenium.common.exceptions import *
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.support.ui import WebDriverWait
from page.login_page import LoginPage
from page.main_page import MainPage
import random


class Application(object):

    def __init__(self, driver):
        self.driver = driver
        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        self.wait = WebDriverWait(driver, 10)

    def go_to_login_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/users/login")

    def go_to_film_page(self):
        self.driver.get("http://kuki.webtest2.htc-cs.com/movies/12")

    def login(self, user):
        lp = self.login_page
        lp.username_field.clear()
        lp.username_field.send_keys(user.username)
        lp.password_field.clear()
        lp.password_field.send_keys(user.password)
        lp.submit_bitton.click()

    def add_film_to_cart(self,num):
        fp = self.main_page
        fp.filmpage_link.click()
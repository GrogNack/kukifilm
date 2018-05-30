# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User

def test_login(app):
    app.go_to_home_page()
    app.login(User.Admin())
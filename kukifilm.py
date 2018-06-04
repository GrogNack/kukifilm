# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User


def test_login(app):
    app.go_to_login_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.logout()
    assert app.is_not_logged_in()

def test_Film(app):
    app.go_to_login_page()
    app.login(User.Admin())
    assert app.is_logged_in()
    app.add_film_to_cart()
    app.logout()
    assert app.is_not_logged_in()
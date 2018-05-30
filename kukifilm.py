# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import *
from fixture import app
import unittest, time, re
from model.user_data import User


def test_login(app):
    app.go_to_login_page()
    app.login(User.Admin())

def test_addFilm(app):
    app.add_film_to_cart(12)
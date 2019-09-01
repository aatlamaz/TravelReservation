from selenium import webdriver
from pages.login_page import LoginPage
from base.webdriverfactory import WebDriverFactory

import unittest
import allure
import pytest
import time

class LoginTest(unittest.TestCase): # LOGIN PART

    def test1(self): #getting into account
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()


        fp = LoginPage(driver)
        fp.login("summer2019@gmail.com", "Smmr2019")

        _name = "//button[@id='header-account-menu-signed-in']"

        name = driver.find_element_by_xpath(_name).text

        if name=="Hello, summer":
            print("TC001 is passed")
        else:
            print("TC001 is failed")



    # def test2(self): #wrong email address
    #
    #     wd = WebDriverFactory(browser="firefox")
    #     driver = wd.getWebDriverInstance()
    #
    #     _error_message = "//div[@id='gss-signin-incorrect-email-or-password']"
    #
    #     fp = LoginPage(driver)
    #     fp.login("summar2019@gmail.com", "Smmr2019")
    #
    #     errormassege = driver.find_element_by_xpath(_error_message)
    #
    #     if errormassege.is_displayed():
    #         print("TC002 is passed")
    #     else:
    #         print("TC002 is failed")
    #
    #
    # def test3(self): #wrong password
    #
    #     wd = WebDriverFactory(browser="firefox")
    #     driver = wd.getWebDriverInstance()
    #
    #     errormassege = driver.find_element_by_xpath("//div[@id='gss-signin-incorrect-email-or-password']")
    #     if errormassege.is_displayed():
    #         print("TC003 is passed")
    #     else:
    #         print("TC003 is failed")
    #
    #     fp = LoginPage(driver)
    #     fp.login("summer2019@gmail.com", "Smmer2019")

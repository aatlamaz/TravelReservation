from selenium import webdriver
from pages.flight_page_AAA import FlightPage
from base.webdriverfactory import WebDriverFactory

import unittest
import allure

import time

class FlightTest(unittest.TestCase):  # LOGIN PART

    def test(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        # baseUrl = "https://www.expedia.com/"
        # driver = webdriver.Firefox()
        # driver.maximize_window()
        # driver.get(baseUrl)
        # driver.implicitly_wait(5)




        fp = FlightPage(driver)
        fp.flight("Boston", "New York")





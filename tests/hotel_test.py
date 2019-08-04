from selenium import webdriver
from pages.hotel_page import HotelPage
from base.webdriverfactory import WebDriverFactory

import time
# import unittest

class HotelTest():
    def TC001(self):
        wd = WebDriverFactory(browser="firefox")
        driver=wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()

        element=driver.find_element_by_xpath("//button[@id='tab-hotel-tab-hp']")
        if element.is_enabled():
            print("Test Case Tc001: Pass")
        else:
            print("Test case Tc001: Fail")

    def TC002(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()
        htl.selectcitygoingtotab("new york")

        element = driver.find_element_by_xpath("//input[@id='hotel-destination-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc002: Pass")
        else:
            print("Test case Tc002: Fail")

    def TC003(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()
        htl.checkintab()
        htl.checkindate()

        element = driver.find_element_by_xpath("//input[@id='hotel-checkin-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc003: Pass")
        else:
            print("Test case Tc003: Fail")

    def TC004(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()
        htl = HotelPage(driver)
        htl.hoteltab()
        htl.checkouttab()
        htl.checkoutdate()

        element = driver.find_element_by_xpath("//input[@id='hotel-checkout-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc004: Pass")
        else:
            print("Test case Tc004: Fail")

    def TC005(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()
        htl = HotelPage(driver)
        htl.hoteltab()
        htl.checkouttab()
        htl.checkoutdate()
        htl.adulttab()
        htl.adultadd()
        htl.closeadulttab()
        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc005: Pass")
        else:
            print("Test case Tc005: Fail")

    def TC006(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()
        htl.checkouttab()
        htl.checkoutdate()
        htl.adulttab()
        htl.addroom()
        htl.closeadulttab()

        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc006: Pass")
        else:
            print("Test case Tc006: Fail")

    def TC007(self):

        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()
        htl.selectcitygoingtotab("new york")
        htl.checkintab()
        htl.checkindate()
        htl.checkouttab()
        htl.checkoutdate()
        htl.adulttab()
        htl.addroom()
        htl.closeadulttab()
        htl.seachinghotels()

        ExpectedResult = "https://www.expedia.com/Hotel-Search?destination=New+York%2C+New+York&latLong=40.75668%2C-73.98647&regionId=178293&startDate=08%2F14%2F2019&endDate=08%2F15%2F2019&rooms=2&adults=2%2C1"
        ActualResult = driver.current_url

        if ExpectedResult==ActualResult:
            print("Test Case Tc007: Pass")
        else:
            print("Test Case Tc007: Fail")


hh = HotelTest()
hh.TC001()
hh.TC002()
hh.TC003()
hh.TC004()
hh.TC005()
hh.TC006()
hh.TC007()


# ExpectedResult = "https://www.expedia.com/Hotel-Search?destination=New+York%2C+New+York&latLong=40.75668%2C-73.98647&regionId=178293&startDate=08%2F14%2F2019&endDate=08%2F15%2F2019&rooms=2&adults=3%2C1"
#         ActualResult = driver.current_url
#
#         if ExpectedResult==ActualResult:
#             print("TC001 is PASS")
#         else:
#             print("TC001 is FAIL")
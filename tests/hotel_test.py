from selenium import webdriver
from pages.hotel_page import HotelPage
import time
from base.webdriverfactory import WebDriverFactory
import unittest
# import allure


class Hoteltest(unittest.TestCase):

    #tell me what it is about
    def test_page_1(self):
        """Click Hotels Reservations Button"""

        wd=WebDriverFactory(browser="firefox")
        driver=wd.getWebDriverInstance()

        htl = HotelPage(driver)
        htl.hoteltab()

        element=driver.find_element_by_xpath("//button[@id='tab-hotel-tab-hp']")
        if element.is_enabled():
            print("Test Case Tc001: Pass")
        else:
            print("Test case Tc001: Fail")


        """Enter City Name to Going to Tab"""

        htl.selectcitygoingtotab("new york")

        element = driver.find_element_by_xpath("//input[@id='hotel-destination-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc002: Pass")
        else:
            print("Test case Tc002: Fail")


        """Select Checkin Date"""

        htl.checkintab()
        htl.checkindate()

        element = driver.find_element_by_xpath("//input[@id='hotel-checkin-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc003: Pass")
        else:
            print("Test case Tc003: Fail")


        """Select Checkout Date"""

        htl.checkouttab()
        htl.checkoutdate()

        element = driver.find_element_by_xpath("//input[@id='hotel-checkout-hp-hotel']")
        if element.is_enabled():
            print("Test Case Tc004: Pass")
        else:
            print("Test case Tc004: Fail")


        """Click Travelers Part and close travelers tab"""

        htl.adulttab()

        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc005: Pass")
        else:
            print("Test case Tc005: Fail")


        """Click Travelers and add Adult part"""

        htl.adultadd()


        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc006: Pass")
        else:
            print("Test case Tc006: Fail")


        """Click Travelers and click Room part"""

        htl.addroom()


        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc007: Pass")
        else:
            print("Test case Tc007: Fail")


        """Click Travelers and click child travelers part"""


        # htl.childadd()
        htl.closeadulttab()

        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-hotel']/div/ul/li/button")
        if element.is_enabled():
            print("Test Case Tc008: Pass")
        else:
            print("Test case Tc008: Fail")


        """Click search  and go to next hotels results page"""


        htl.seachinghotels()


        if driver.find_element_by_xpath("//legend[contains(text(),'Sort by')]").is_displayed():
            print("Test Case Tc009: Pass")
        else:
            print("Test Case Tc009: Fail")


        """Select Sort by Price and list hotels"""


        htl.sortbyprice()

        element = driver.find_element_by_xpath("//input[@id='radio-sort-price']")
        if element.is_enabled():
            print("Test Case Tc010: Pass")
        else:
            print("Test case Tc010: Fail")

    #whats going on here
    def test_page_2(self):
        """Select price and popular filters and list hotels"""

        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance_hotelsresultpage()

        htl = HotelPage(driver)
        htl.sortbyprice()
        htl.popularfiltershotel()

        element = driver.find_element_by_xpath("//input[@id='popularFilter-0-hotel']")
        if element.is_enabled():
            print("Test Case Tc011: Pass")
        else:
            print("Test case Tc011: Fail")


        """Select price and popular filters and list hotels"""

        htl.propertyclass()

        element = driver.find_element_by_xpath("//fieldset[4]//div[1]//div[1]//div[4]//label[1]//span[1]")
        if element.is_enabled():
            print("Test Case Tc012: Pass")
        else:
            print("Test case Tc012: Fail")


        """Select price and popular filters and free cancelation hotels"""

        htl.freecancelation()

        element = driver.find_element_by_xpath("//input[@id='paymentType-0-freeCancellation']")
        if element.is_enabled():
            print("Test Case Tc013: Pass")
        else:
            print("Test case Tc013: Fail")


        """Select both 2 option, pay later reserve hotels and free cancelation"""

        htl.paylater()

        element = driver.find_element_by_xpath("//input[@id='paymentType-1-payLater']")
        if element.is_enabled():
            print("Test Case Tc014: Pass")
        else:
            print("Test case Tc014: Fail")


        """Select Breakfast include tab in Amenities part """

        htl.amenities_breakfast()

        element = driver.find_element_by_xpath("//input[@id='amenities-0-16']")
        if element.is_enabled():
            print("Test Case Tc015: Pass")
        else:
            print("Test case Tc015: Fail")


        """Select Hotel part"""

        # htl.select_hotel()
        #
        # Expected_result = "https://www.expedia.com/Hotel-Elysee-by-Library-Hotel-Collection.h11162.Hotel-Information?chkin=8%2F28%2F2019&chkout=8%2F29%2F2019&regionId=178293&destination=New+York+%28and+vicinity%29%2C+New+York%2C+United+States+of+America&swpToggleOn=true&rm1=a2&rm2=a1&x_pwa=1&amenities=16&star=40&sort=price&lodging=hotel&top_dp=256&top_cur=USD&rfrr=HSR&pwa_ts=1564928149039"
        # Actual_result = driver.current_url
        # if Expected_result==Actual_result:
        #     print("Test Case Tc016: Pass")
        # else:
        #     print("Test case Tc016: Fail")

hh = Hoteltest()
hh.test_page_1()
hh.test_page_2()

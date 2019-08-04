from selenium import webdriver
from pages.flight_pages import FlightPage
from base.webdriverfactory import WebDriverFactory

import unittest
import allure


class Flight1(unittest.TestCase):
    def test_flight(self):
        global driver
        wd = WebDriverFactory(browser="chrome.driver")
        driver = wd.getWebDriverInstance()


        fp = FlightPage(driver)
        fp.flights3(" Bos")

        expectedUrl = "https://www.expedia.com/"
        currentUrl = driver.current_url
        print(currentUrl)

        if currentUrl == expectedUrl:
            print("TC007_Checking The Url Pass")
        else:
            print("TC007 Checking The Url Fail")


        print("*" * 20)


        if driver.find_element_by_xpath("//label[@id='flight-type-roundtrip-label-hp-flight']").is_enabled():
            print("TC009_Clicking Round Trip Button Pass")
        else:
            print("TC009_Clicking round Trip Button Fail")


        print("*"* 20)


        dept_area = (driver.find_element_by_xpath("//section[@id='section-flight-tab-hp']//div[contains(@class,'cols-nested ab25184-location')]//div[1]//div[1]//div[2] "))

        if dept_area.is_enabled():
            print("TC010_Selecting Depart Area Pass")
        else:
            print("TC010_Selecting Depart Area Fail")


        print("*"* 20)


        message = driver.find_element_by_xpath("//h5[@class='alert-title no-outline']")
        print(message.text)

        if message.text == "Please correct the errors below.":
            print("TC016_All Mandatory Fields Should Be Fill Out Pass")
        else:
            print("TC016_All Mandatory Fields Should Be Fill Out Fail")


        print("*" * 20)


        dept_date = driver.find_element_by_xpath(" //input[@id='flight-departing-hp-flight']")
        print(dept_date.text)

        if dept_date.text == "08/24/2019":
            print("TC012_Checking Depart Date Pass")
        else:
            print("TC012_Checking Depart Date Fail")


        print("*" * 20)

        arriv_date = driver.find_element_by_xpath("//input[@id='flight-returning-hp-flight']")
        print(arriv_date.text)

        if dept_date.text=="08/24/2019":
            print("TC013_Checking Return Date Pass")
        else:
            print("TC013_Checking Return Date Fail")

        fp = FlightPage(driver)
        fp.flights1( " New York")

        arrival_area = driver.find_element_by_xpath("//section[@id='section-flight-tab-hp']//div[contains(@class,'cols-nested ab25184-location')]//div[1]//div[1]//div[2] ")
        if arrival_area.is_enabled():
            print("TC011_Selecting The Arrival Area Pass")
        else:
            print("TC011_Selecting The Arrival Area Fail")


        print("*"* 20)





        fp= FlightPage(driver)
        fp.flights2()

        if len(driver.find_elements_by_xpath("//div[@data-test-id='listing-main']"))==0:
            print("TC014_Checking The List Of Flights Fail")
        else:
            print("TC014_Checking The List Of Flights Pass")

        print("*"*20)


        if (driver.find_element_by_xpath("//span[@class='secondary-playback-summary']")).is_displayed():
            print("TC017_Checking The Selections Present Pass")
        else:
            print("TC017_Checking The Selections Present Fail")

        print("*"* 20)


        if (driver.find_element_by_xpath("//input[@id='stopFilter_stops-0']")).is_selected():
            print("TC019_Selecting Nonstop Button Pass")
        else:
            print("TC019_Selecting Nonstop Button Fail")

        print("*"* 20)

        if ((driver.find_element_by_xpath(" //input[@id='airlineRowContainer_AA']")) and (driver.find_element_by_xpath("//input[@id='airlineRowContainer_DL']"))).is_selected():
            print("TC020_Selecting Airlines Brand Pass")
        else:
            print("TC020_Selecting Airlines Brand Fail")

        print("*"* 20)

        if(driver.find_element_by_xpath("//input[@id='leg0-morning-departure']")).is_selected():
            print("TC021_Selecting The Departure Time Pass")
        else:
            print("TC021_Selecting The Departure Time Fail")


        print("*"* 20)


        if(driver.find_element_by_xpath("//input[@id='leg0-morning-arrival']")).is_selected():
            print("TC022_Selecting Arrival Time Pass")
        else:
            print("TC022_Selecting Arrival Time Fail")


        print("*"* 20)

        #
        # if(driver.find_element_by_xpath("//input[@id='airportRowContainer_JFK']")).is_selected():
        #     print("TC023_Selecting Arrival Airport Pass ")
        # else:
        #     print("TC023_Selecting Arrival Airport Fail")
        #
        #
        # print("*"* 20)







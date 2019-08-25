

from selenium import webdriver
from pages.flight_pages import FlightPage
import time
import unittest
from base.webdriverfactory import WebDriverFactory
# import allure

class Flighttest(unittest.TestCase):
    def test_page_1(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.getWebDriverInstance()
        ft = FlightPage(driver)


        """ Click and verify flight tab  """
        ft.flight()

        element=driver.find_element_by_id("tab-flight-tab-hp")
        if element.is_enabled():
            print("Test case TC001: Pass")
        else:
            print("Test case TC001: Fail")


        """ Click and verify roundtrip tab  """
        ft.rounttrip()

        element=driver.find_element_by_xpath("//label[@id='flight-type-roundtrip-label-hp-flight']")
        if element.is_displayed():
             print("Test Case Tc002: Pass")
        else:
            print("Test case Tc002: Fail")


        """ Click and verify destination city tab  """
        ft.destinationcity("boston")

        if driver.find_element_by_xpath("//*[@id='flight-origin-hp-flight']").is_enabled():
            print("Test Case TC003: Pass")
        else:
            print("Test case TC003: Fail")


        """ Select destination city and verify """
        element=driver.find_element_by_xpath("//a[@id='aria-option-1']//span[2]")

        if driver.find_element_by_xpath("//a[@id='aria-option-1']//span[2]").is_enabled():
            ft.destinationselect()
            print("Test Case TC004: Pass")
        else:
            print("Test case TC004: Fail")


        """ Click and verify arrive city tab  """
        ft.arrivecity("new york")

        if driver.find_element_by_xpath("//*[@id='flight-destination-hp-flight']").is_enabled():
            print("Test Case TC005: Pass")
        else:
            print("Test case TC005: Fail")


        """ Select arrive city and verify  """
        element = driver.find_element_by_xpath("//*[@id='aria-option-0']/span[2]/div")
        if element.is_enabled():
            ft.arriveselect()
            print("Test Case TC006: Pass")
        else:
            print("Test case TC006: Fail")


        """ Click and verify departure calender tab  """
        ft.calenderdeparture()

        element = driver.find_element_by_id("flight-departing-hp-flight")
        if element.is_enabled():
            print("Test Case TC007: Pass")
        else:
            print("Test case TC007: Fail")


        """ Select and verify departure date  """
        element=driver.find_element_by_xpath("//button[@data-day='25' and @data-month='8']")

        if element.is_enabled():
            ft.datedeparture()
            print("Test Case TC008: Pass")
        else:
            print("Test case TC008: Fail")


        """ Click and verify arrive calender tab  """
        ft.calenderarrive()

        if driver.find_element_by_id("flight-returning-hp-flight").is_enabled():
            print("Test Case TC009: Pass")
        else:
            print("Test case TC009: Fail")


        """ Select and verify arrive date """
        element = driver.find_element_by_xpath("//button[@data-day='28' and @data-month='8']")
        if element.is_displayed():
            ft.datearrive()
            print("Test Case TC010: Pass")
        else:
            print("Test case TC010: Fail")


        """ Click and verify travelers tab  """
        ft.travelers()

        element = driver.find_element_by_xpath("//div[@id='traveler-selector-hp-flight']//div/ul/li/button")
        if element.is_enabled():
            print("Test Case TC011: Pass")
        else:
            print("Test case TC011: Fail")


        """ Select and verify travelers number """
        ft.travelers_plus()

        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button/span[1]")

        if element.is_enabled():
            print("Test Case TC012: Pass")
        else:
            print("Test case TC012: Fail")


        """ Close and verify travelers tab  """
        element = driver.find_element_by_xpath("//*[@id='traveler-selector-hp-flight']/div/ul/li/div/footer/div/div[2]/button")

        if element.is_enabled():
            ft.close_tab()
            print("Test Case TC013: Pass")
        else:
            print("Test case TC013: Fail")


        """ Select and verify search tab  """
        element = driver.find_element_by_css_selector("#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button")
        if element.is_enabled():
            print("Test Case TC014: Pass")
            ft.search()
        else:
            print("Test case TC014: Fail")


        """ Filter and verify nonstop flight  """
        ft.nonstop()

        if (driver.find_element_by_xpath("//input[@id='stopFilter_stops-0']")).is_displayed():
            print("Test Case TC015: Pass")
        else:
            print("Test case TC015: Fail")

    def test_page2(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.get2WebDriverInstance()
        ft = FlightPage(driver)

        """ Click and verify first flight option  """
        ft.firstflight()

        if driver.find_element_by_xpath("//*[@id='basic-economy-tray-content-1']/div/div/div[1]/button").is_enabled():
            ft.selectfare()
            print("Test Case TC016: Pass")
        else:
            print("Test case TC016: Fail")


        """ Click and verify second flight option  """
        ft.secondflight()

        if (driver.find_element_by_xpath("//*[@id='xsellAddHotelNow']")).is_enabled():

            print("Test Case TC017: Pass")
        else:
            print("Test case TC017: Fail")


        """ Click and verify nothanks button  """
        ft.nothanks()

        head_name=driver.find_element_by_xpath("//h1[@class='section-header-main']").text
        if head_name=="Select your return to Boston Sat, Sep 28":
            print("Test Case TC018: Pass")
        else:
            print("Test case TC018: Fail")

    def test_page3(self):
        wd = WebDriverFactory(browser="firefox")
        driver = wd.get3WebDriverInstance()
        ft=FlightPage(driver)

        """ Click and verify booking tab  """
        ft.booking()

        location_info=driver.find_element_by_xpath("//div[@class='location-info']").text
        if location_info=="Boston (BOS) to New York (JFK)":
            print("Test Case TC019: Pass")
        else:
            print("Test case TC019: Fail")


        """ Select and verify first traveler information part """
        ft.firsttr_name("AZIME")
        ft.firsttr_lastname("SUKUSU")
        ft.phonenumber("8572728900")
        ft.firsttr_gender()
        # ft.firsttr_mob()
        # ft.firsttr_mob1()
        # ft.firsttr_dob()
        # ft.firsttr_dob1()
        # ft.firsttr_yob()
        # ft.firsttr_yob1()

        if (driver.find_element_by_xpath("//input[@id='firstname[0]']")).is_displayed():
            print("Test Case TC020: Pass")
        else:
            print("Test case TC020: Fail")


        """ Select and verify select traveler information part """
        ft.secondtr_name("MERT")
        ft.secondtr_lastname("SUKUSU")
        ft.secondtr_gender()
        # ft.secondtr_mob()
        # ft.secondtr_mob1()
        # ft.secondtr_dob()
        # ft.secondtr_dob1()
        # ft.secondtr_yob()
        # ft.secondtr_yob1()

        if (driver.find_element_by_xpath("//input[@id='firstname[1]']")).is_displayed():
            print("Test Case TC021: Pass")
        else:
            print("Test case TC021: Fail")


        """ Select and verify payment part """
        ft.noinsurance()
        ft.name_oncard("AZIME SUKUSU")
        ft.card_number("5253123456723456")
        ft.expiration_month()
        ft.expiration_month1()
        ft.expiration_year()
        ft.expiration_year1()
        # ft.security_code("253")

        if (driver.find_element_by_xpath("//select[@name='creditCards[0].expiration_year']")).is_enabled():
            print("Test Case TC022: Pass")
        else:
            print("Test case TC022: Fail")


        """ Select and verify billing address part """
        ft.billing_address1("375 ACORN PARK DR")
        ft.billing_address2("APT 4301")
        ft.billingcity("BELMONT")
        ft.billing_state()
        ft.billing_state1()
        ft.billing_zipcode("02478")
        ft.conf_email("azimedalkilinc@gmail.com")
        ft.create_password("12345abcde")
        ft.confirm_password("12345abcde")

        if (driver.find_element_by_xpath("//input[@name='repeat_password']")).is_enabled():
            print("Test Case TC023: Pass")
        else:
            print("Test case TC023: Fail")


        """ Click and verify complete booking button """

        if (driver.find_element_by_xpath("//button[@id='complete-booking']")).is_enabled():
            # ft.complete_booking()
            print("Test Case TC024: Pass")
        else:
            print("Test case TC024: Fail")




ff=Flighttest()
ff.test_page_1()
ff.test_page2()
ff.test_page3()




from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumDriver
import time


class FlightPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    _flightstop = "//a[@id='primary-header-flight']"
    _flight_button = "//span[@class='tab-label'][contains(text(),'Flights')] "
    _round_trip = "//label[@id='flight-type-roundtrip-label-hp-flight']"
    _one_way = "//label[@id='flight-type-one-way-label-flp']"
    _flying_from = "#flight-origin-hp-flight"
    _flying_from_select = "//ap//b[contains(text(),'BOS')] "
    _flying_to = "//input[@id='flight-destination-hp-flight']"
    _flying_to_select = "//*[@id='aria-option-1'] "
    _depart_date_area= "//input[@id='flight-departing-hp-flight']"
    _depart_date ="//button[@data-month = '7' and @data-day = '24']"
    _return_date_area = "//input[@id='flight-returning-hp-flight']"
    _return_date = "//button[@data-month = '7' and @data-day = '30']"
    _travelers_area = "//div[@class='menu-bar gcw-travel-selector-wrapper']//button[@class='trigger-utility menu-trigger btn-utility btn-secondary dropdown-toggle theme-standard pin-left menu-arrow gcw-component gcw-traveler-amount-select gcw-component-initialized']  "
    _travelers_close= "//li[@class='open']//button[@class='close btn-text'] "
    _search_button = "//div[@class='cols-nested ab25184-submit']//button[@class='btn-primary btn-action gcw-submit']  "
    _time = "//span[@class='times segment-info-departure']"
    _nonstop_btn = "//fieldset[@id='stops']//div[3]//div[1]//label[1]"
    _airlines1 = " //fieldset[@id='airlines']//div[3]//div[1]//label[1]"
    _airlines2 = " //fieldset[@id='airlines']//div[4]//div[1]//label[1]"
    _dep_time = "//fieldset[@id='departure-times']//div[2]//div[1]//label[1]"
    _arr_time="//input[@id='leg0-morning-arrival']"
    _arr_airport="//input[@id='airportRowContainer_JFK']"


    def clickFlightstop(self):
        self.elementClick(self._flightstop,locatorType='xpath')

    def clickFlight(self):
        self.elementClick(self._flight_button,locatorType='xpath')

    def clickRoundTrip(self):
        self.elementClick(self._round_trip,locatorType='xpath')

    def clickOneWay(self):
        self.elementClick(self._one_way, locatorType='xpath')

    def sendkeyDeptCity(self, flying_from):
        self.sendKeys(flying_from, self._flying_from, locatorType='css')


    def clickflyingfrom(self):
        self.elementClick(self._flying_from_select,locatorType='xpath')

    def sendkeyDestCity(self,flying_to):
        self.sendKeys(flying_to,self._flying_to,locatorType='xpath')

    def clickdestcity(self):
        self.elementClick(self._flying_to_select,locatorType='xpath')

    def clickdeptdatearea(self):
        self.elementClick(self._depart_date_area,locatorType='xpath')

    def clickdepartdate(self):
        self.elementClick(self._depart_date,locatorType='xpath')

    def clickreturndatearea(self):
        self.elementClick(self._return_date_area,locatorType='xpath')

    def clickreturndate(self):
        self.elementClick(self._return_date,locatorType='xpath')

    def clicktravelers(self):
        self.elementClick(self._travelers_area,locatorType='xpath')

    def clicktravelersclose(self):
        self.elementClick(self._travelers_close,locatorType='xpath')

    def clicksearch(self):
        self.elementClick(self._search_button,locatorType='xpath')


    def clicknonstop(self):
        self.elementClick(self._nonstop_btn,locatorType='xpath')

    def clickairone(self):
        self.elementClick(self._airlines1, locatorType='xpath')

    def clickairtwo(self):
        self.elementClick(self._airlines2, locatorType='xpath')

    def clickdepttime(self):
        self.elementClick(self._dep_time, locatorType="xpath")

    def clickarrtime(self):
        self.elementClick(self._arr_time,locatorType='xpath')

    def clickarrairport(self):
        self.elementClick(self._arr_airport,locatorType='xpath')


    def flights1(self,flying_to):
        self.sendkeyDestCity(flying_to)
        time.sleep(2)

        self.clickdestcity()
        time.sleep(2)



    def flights2(self):

        self.clicksearch()
        time.sleep(2)

        self.clicknonstop()
        time.sleep(2)

        self.clickairone()
        time.sleep(2)

        self.clickairtwo()
        time.sleep(2)

        self.clickdepttime()
        time.sleep(2)

        self.clickarrtime()
        time.sleep(2)

        self.clickarrairport()
        time.sleep(2)

    def flights3(self, flying_from):
        self.clickFlight()
        time.sleep(2)

        self.clickRoundTrip()
        time.sleep(2)

        self.sendkeyDeptCity(flying_from)
        time.sleep(2)

        self.clickflyingfrom()
        time.sleep(2)

        self.clickdeptdatearea()
        time.sleep(2)

        self.clickdepartdate()
        time.sleep(2)

        self.clickreturndatearea()
        time.sleep(2)

        self.clickreturndate()
        time.sleep(2)

        self.clicktravelers()
        time.sleep(2)

        self.clicktravelersclose()
        time.sleep(2)

        self.clicksearch()
        time.sleep(2)




#from selenium import webdriver
from selenium.webdriver.common.by import By
#import time
from base.selenium_driver import SeleniumDriver


# class FlightPage(SeleniumDriver):
#
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.driver = driver
#
#     # Locators
#
#     _flight_tab = "//span[@class='tab-label'][contains(text(),'Flights')]"
#     _round_trip = "//label[@id='flight-type-roundtrip-label-hp-flight']"
#     # _origin_city =  "//input[@id='flight-origin-hp-flight']"
#     _origin_city = "#flight-origin-hp-flight"
#     _orig_city_select = "//ap//b[contains(text(),'BOS')]"
#     _dest_city = "//input[@id='flight-destination-hp-flight']"
#     _dest_city_select = "//*[@id='aria-option-1']"
#     _departing_date = "//button[@type='button'][contains(.,'July 26')]"
#     _returning_date = "//*[@id='flight-returning-wrapper-hp-flight']/div/div[2]/div[3]/table/tbody/tr[2]/td[3]/button"
#     _travellers = "//input[@id='flight-returning-hp-flight']"
#     _adult = "//body[@class='wrap cf aoa-enabled']/meso-native-marquee/section[@id='WizardHero']/div[@id='hero-banner']/div[@class='hero-banner-gradient native-marquee']/div[@class='cols-row hero-banner-inner']/section[@id='wizardSection']/div[@class='hero-banner-box siteId-1 cf hideClassicDcol']/div[@id='wizard-tabs']/div[@class='tabs-container col']/section[@id='section-flight-tab-hp']/form[@id='gcw-flights-form-hp-flight']/fieldset[@class='room-data']/div[@class='cols-nested']/div[@class='ab25184-traveler-wrapper-flight available-for-flights gcw-clear-both']/div[@id='traveler-selector-hp-flight']/div[@class='menu-bar gcw-travel-selector-wrapper']/ul[@class='menu-bar-inner']/li[@class='open']/div[@class='menu sticky gcw-menu']/div[@class='menu-main']/div[@class='traveler-selector-sinlge-room-data traveler-selector-room-data']/div[@class='uitk-grid step-input-outside gcw-component gcw-component-step-input gcw-step-input gcw-component-initialized']/div[@class='uitk-col all-col-shrink']/button[@class='uitk-step-input-button uitk-step-input-plus']/span[@class='uitk-icon']/*[1]"
#     # _child = ""
#     # _infant = ""
#     _search = "//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']"
#
#     # def clickAccount(self):
#     # return self.elementClick(self._account,locatorType='xpath')
#
#     # def clickSelectCreateAccount(self):
#     # return self.elementClick(self._create_account,locatorType='xpath')

    # def clickFlightTab(self):
    #     self.elementClick(self._flight_tab, locatorType='xpath')
    #
    # def clickRoundTrip(self):
    #     self.elementClick(self._round_trip, locatorType='xpath')
    #
    # def sendkeyOriginCity(self, orig_city):
    #     self.sendKeys(orig_city, self._origin_city, locatorType='css')
    #
    # def select_OriginCity(self):
    #     self.elementClick(self._orig_city_select, locatorType='xpath')
    #
    # def sendkeyDestCity(self, dest_city, ):
    #     self.sendKeys(dest_city, self._dest_city, locatorType="xpath")
    #
    # def select_DestCity(self):
    #     self.elementClick(self._dest_city_select, locatorType='xpath')
    #
    # def clickDepartDate(self):
    #     self.elementClick(self._departing_date, locatorType='xpath')
    #
    # def clickReturnDate(self):
    #     self.elementClick(self._returning_date, locatorType='xpath')
    #
    # def clickTravellers(self):
    #     self.elementClick(self._travellers, locatorType='xpath')
    #
    # def clickTravellers_adult(self):
    #     self.elementClick(self._adult, locatorType='xpath')
    #
    # # def clickTravellers_child(self):
    # # self.elementClick(self._child, locatorType='xpath')
    #
    # # def clickTravellers_infant(self):
    # # self.elementClick(self._infant, locatorType='xpath')
    #
    # def clickSearch(self):
    #     self.elementClick(locator=self._search, locatorType='xpath')
    #
    # def flight(self, orig_city, dest_city):  # This is the login functionality
    #
    #     self.clickFlightTab()
    #     time.sleep(1)
    #
    #     self.clickRoundTrip()
    #     time.sleep(1)
    #
    #     self.sendkeyOriginCity(orig_city)
    #     time.sleep(1)
    #
    #     self.select_OriginCity()
    #     time.sleep(1)
    #
    #     self.sendkeyDestCity(dest_city)
    #     time.sleep(1)
    #
    #     self.select_DestCity()
    #     time.sleep(1)
    #
    #     self.clickDepartDate()
    #     time.sleep(2)
    #
    #     self.clickReturnDate()
    #     time.sleep(2)
    #     #
    #     # self.clickTravellers()
    #     # time.sleep(2)
    #     #
    #     # self.clickTravellers_adult()
    #     # time.sleep(2)
    #
    #     self.clickSearch()
    #     time.sleep(2)
    #

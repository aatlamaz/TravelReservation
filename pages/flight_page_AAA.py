from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver

class FlightPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    _flight_tab =  "//span[@class='tab-label'][contains(text(),'Flights')]"
    _round_trip = "//label[@id='flight-type-roundtrip-label-hp-flight']"
    #_origin_city =  "//input[@id='flight-origin-hp-flight']"
    _origin_city = "#flight-origin-hp-flight"
    _city = "BOS (Logan Intl.)"
    _orig_city_select = "//a[@id='aria-option-2']//span[2]"
    _dest_city =  "//input[@id='flight-destination-hp-flight']"
    _dest_city_select = "//span[contains(.,'(EWR) Liberty Intl., Newark, NJ, United States')]"
    _departing_date ="//*[@id='flight-departing-wrapper-hp-flight']/div/div[2]/div[2]/table/tbody/tr[5]/td[4]/button"
    _returning_date = "//div[3]//table[1]//tbody[1]//tr[1]//td[6]//button[1]"
    _travellers =  "//input[@id='flight-returning-hp-flight']"
    _adult = "//body[@class='wrap cf aoa-enabled']/meso-native-marquee/section[@id='WizardHero']/div[@id='hero-banner']/div[@class='hero-banner-gradient native-marquee']/div[@class='cols-row hero-banner-inner']/section[@id='wizardSection']/div[@class='hero-banner-box siteId-1 cf hideClassicDcol']/div[@id='wizard-tabs']/div[@class='tabs-container col']/section[@id='section-flight-tab-hp']/form[@id='gcw-flights-form-hp-flight']/fieldset[@class='room-data']/div[@class='cols-nested']/div[@class='ab25184-traveler-wrapper-flight available-for-flights gcw-clear-both']/div[@id='traveler-selector-hp-flight']/div[@class='menu-bar gcw-travel-selector-wrapper']/ul[@class='menu-bar-inner']/li[@class='open']/div[@class='menu sticky gcw-menu']/div[@class='menu-main']/div[@class='traveler-selector-sinlge-room-data traveler-selector-room-data']/div[@class='uitk-grid step-input-outside gcw-component gcw-component-step-input gcw-step-input gcw-component-initialized']/div[@class='uitk-col all-col-shrink']/button[@class='uitk-step-input-button uitk-step-input-plus']/span[@class='uitk-icon']/*[1]"
    #_child = ""
    #_infant = ""
    _search = "//form[@id='gcw-flights-form-hp-flight']//button[@class='btn-primary btn-action gcw-submit']"

    #def clickAccount(self):
        #return self.elementClick(self._account,locatorType='xpath')

    #def clickSelectCreateAccount(self):
        #return self.elementClick(self._create_account,locatorType='xpath')

    def clickFlightTab(self):
         self.elementClick(self._flight_tab, locatorType='xpath')

    def clickRoundTrip(self):
        self.elementClick(self._round_trip, locatorType='xpath')

    def sendkeyOriginCity(self,orig_city):
        self.sendKeys1(orig_city, self._origin_city,locatorType = 'css')

    def select_OriginCity(self):

        self.elementClick(self._orig_city_select, locatorType='xpath')
        self.selectDropdown(self._city,optionToSelect=True)
    def sendkeyDestCity(self,dest_city,):
        self.sendKeys1(dest_city,self._dest_city, locatorType="xpath")

    def select_DestCity(self):
        self.elementClick(self._dest_city_select,locatorType='xpath')

    def clickDepartDate(self):
        self.elementClick(self._departing_date, locatorType='xpath')

    def clickReturnDate(self):
        self.elementClick(self._returning_date, locatorType='xpath')

    def clickTravellers(self):
            self.elementClick(self._travellers, locatorType='xpath')

    def clickTravellers_adult(self):
            self.elementClick(self._adult, locatorType='xpath')

    #def clickTravellers_child(self):
        #self.elementClick(self._child, locatorType='xpath')

    #def clickTravellers_infant(self):
           # self.elementClick(self._infant, locatorType='xpath')

    def clickSearch(self):
            self.elementClick(locator=self._search, locatorType='xpath')

    def flight(self, orig_city="", dest_city=""): #This is the login functionality
        
        self.clickFlightTab()
        time.sleep(1)
    
        self.clickRoundTrip()
        time.sleep(1)

        self.sendkeyOriginCity(orig_city)
        time.sleep(1)

        self.select_OriginCity()
        time.sleep(1)

        self.sendkeyDestCity(dest_city)
        time.sleep(1)

        self.select_DestCity()
        time.sleep(1)



        self.clickDepartDate()
        time.sleep(2)

        self.clickReturnDate()
        time.sleep(2)
        #
        # self.clickTravellers()
        # time.sleep(2)
        #
        # self.clickTravellers_adult()
        #time.sleep(2)

        self.clickSearch()
        time.sleep(2)


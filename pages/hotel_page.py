from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import time
import utilities
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class HotelPage(SeleniumDriver):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver

        #locators
    _hotel_tab="//button[@id='tab-hotel-tab-hp']"
    _goingto_tab="//input[@id='hotel-destination-hp-hotel']"
    _goingto_city="#aria-option-0 > span.text > span > div"
    _checkin_tab="//input[@id='hotel-checkin-hp-hotel']"
    _checkin_date="//button[@data-day='28' and @data-month='7']"
    _checkout_tab="//input[@id='hotel-checkout-hp-hotel']"
    _checkout_date="//button[@data-day='31' and @data-month='7']"
    _adult_tab="//*[@id='traveler-selector-hp-hotel']/div/ul/li/button"
    _adult_add="//body[@class='wrap cf aoa-enabled']/meso-native-marquee/section[@id='WizardHero']/div[@id='hero-banner']/div[@class='hero-banner-gradient native-marquee']/div[@class='cols-row hero-banner-inner']/section[@id='wizardSection']/div[@class='hero-banner-box siteId-1 cf hideClassicDcol']/div[@id='wizard-tabs']/div[@class='tabs-container col']/section[@id='section-hotel-tab-hp']/form[@id='gcw-hotel-form-hp-hotel']/div[@class='cols-nested ab25184-dates-travelers']/div[@id='traveler-selector-hp-hotel']/div[@class='menu-bar gcw-travel-selector-wrapper traveler-selector-multi-rooms']/ul[@class='menu-bar-inner']/li[@class='open']/div[@class='menu sticky gcw-menu']/div[@class='menu-main']/div[@class='traveler-selector-room-data']/div[@class='uitk-grid step-input-outside gcw-component gcw-component-step-input gcw-step-input gcw-component-initialized']/div[@class='uitk-col all-col-shrink']/button[@class='uitk-step-input-button uitk-step-input-plus']/span[@class='uitk-icon']/*[1]"
    _child_add="//div[@class='traveler-selector-room-data']//div[@class='children-wrapper']//button[@class='uitk-step-input-button uitk-step-input-plus']//*[@class='uitk-icon-svg uitk-step-input-icon']"
    _add_room=" //li[@class='open']//a[text()='Add another room']"
    _select_child_age="//*[@id='traveler-selector-hp-hotel']/div/ul/li/div/div/div[1]/div[3]/div[2]/label[1]/select"
    _close_travelers_tab="//li[@class='open']//button[@class='close btn-text']"
    _search_tab="//*[@id='gcw-hotel-form-hp-hotel']/div[10]/label/button"
    _sort_by_price = "//input[@id='radio-sort-price']"
    _popular_filters_hotel = "//input[@id='popularFilter-0-hotel']"
    _propertyclass= "//fieldset[4]//div[1]//div[1]//div[4]//label[1]//span[1]"
    _freecancelation= "//input[@id='paymentType-0-freeCancellation']"
    _reservenowpaylater="//input[@id='paymentType-1-payLater']"
    _amenities_breakfastinclude = "//input[@id='amenities-0-16']"
    _select_hotel= "//a[contains(text(),'Click for more information about Hotel Elysee by L')]"
    _reserve_hotel= "//body/div[@id='app']/div/div[@class='app-layer-base--active']/div[@class='page-container infosite']/main[@class='main-region infosite__main']/div[@class='infosite__content infosite__content--details']/section[@class='rooms-and-rates s-x-padding-three all-x-padding-six m-x-padding-zero xl-x-padding-zero']/ul[@class='uitk-grid all-y-gutter-three room-list l-x-padding-zero m-x-padding-zero']/li[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[2]/div[2]/div[1]/form[1]/button[1]/span[1]"
    _contact_name= "//*[@id='preferences']/section/article/fieldset/div/div/div[1]/label[2]/input"
    _phone_number="//input[@placeholder='In case we need to reach you']"
    _credit_card="//input[@id='creditCardInput']"
    _expire_month="//select[@name='creditCards[0].expiration_month']"
    _expire_year="//select[@name='creditCards[0].expiration_year']"
    _card_securit_code="//input[@id='new_cc_security_code']"
    _billing_zipcode=" //input[@name='creditCards[0].zipcode']"
    _email = "//label[@class='text invalid']//input[@name='email']"
    _create_password = "//input[@placeholder='6 - 30 characters, no spaces']"
    _booking_tab = "//button[@id='complete-booking']"

################################################################################################

    def click_hoteltab(self):
        return self.elementClick(self._hotel_tab, locatorType="xpath")
    def sendkey_goingtotab(self,_goingto_tab):
        return self.sendKeys(_goingto_tab, self._goingto_tab,locatorType="xpath")
    # def keydown(self,_goingto_tab):
    #     return self.sendKeys(_goingto_tab,self._goingto_tab)
    # def click_goingtocity(self):
    #    return self.elementClick(self._goingto_city,locatorType="css")
    def click_checkintab(self):
        return self.elementClick(self._checkin_tab,locatorType="xpath")
    def click_checkindate(self):
        return self.elementClick(self._checkin_date,locatorType="xpath")
    def click_checkouttab(self):
        return self.elementClick(self._checkout_tab,locatorType="xpath")
    def click_checkoutdate(self):
        return self.elementClick(self._checkin_date,locatorType="xpath")
    def click_adulttab(self):
        return self.elementClick(self._adult_tab,locatorType="xpath")
    def click_adultadd(self):
        return self.elementClick(self._adult_add,locatorType="xpath")
    def click_childadd(self):
        return self.elementClick(self._child_add,locatorType="xpath")
    def click_addroom(self):
        return self.elementClick(self._add_room,locatorType="xpath")
    def click_child_age_button(self):
        return self.elementClick(self._select_child_age,locatorType="xpath")
    def click_close_button(self):
        return self.elementClick(self._close_travelers_tab,locatorType="xpath")
    def click_searching_button(self):
        return self.elementClick(self._search_tab,locatorType="xpath")
    def click_sortbyprice(self):
        return self.elementClick(self._sort_by_price,locatorType="xpath")
    def click_popularfiltershotelsbutton(self):
        return self.elementClick(self._popular_filters_hotel,locatorType="xpath")
    def click_propertyclassstar(self):
        return self.elementClick(self._propertyclass,locatorType="xpath")
    def click_paylater(self):
        return self.elementClick(self._reservenowpaylater,locatorType="xpath")
    def click_freecancel(self):
        return self.elementClick(self._freecancelation,locatorType="xpath")
    def click_amenitiesbreakfast(self):
        return self.elementClick(self._amenities_breakfastinclude,locatorType="xpath")
    def click_select_hotel(self):
        return self.elementClick(self._select_hotel,locatorType="xpath")



#####################################################

    def hoteltab(self):
        self.click_hoteltab()
        time.sleep(2)
    def goingtotab(self,cityname):
        self.sendkey_goingtotab(cityname)
        time.sleep(6)
    def selectcitygoingtotab(self,cityname):
        self.sendkey_goingtotab(cityname)
        time.sleep(6)
        # self.click_goingtocity()
        self.sendkey_goingtotab(Keys.ARROW_DOWN)
        time.sleep(2)
        self.sendkey_goingtotab(Keys.ENTER)
    def checkintab(self):
        self.click_checkintab()
        time.sleep(2)
    def checkindate(self):
        self.click_checkindate()
        time.sleep(2)
    def checkouttab(self):
        self.click_checkouttab()
        time.sleep(2)
    def checkoutdate(self):
        self.click_checkoutdate()
        time.sleep(2)
    def adulttab(self):
        self.click_adulttab()
        time.sleep(2)
    def adultadd(self):
        self.click_adultadd()
        time.sleep(2)
    def addroom(self):
        self.click_addroom()
        time.sleep(2)
    def childadd(self):
        self.click_childadd()
        time.sleep(2)
    def childagebutton(self):
        self.click_child_age_button()
        time.sleep(2)
    def closeadulttab(self):
        self.click_close_button()
        time.sleep(2)
    def seachinghotels(self):
        self.click_searching_button()
        time.sleep(2)
    def sortbyprice(self):
        self.click_sortbyprice()
        time.sleep(2)
    def popularfiltershotel(self):
        self.click_popularfiltershotelsbutton()
        time.sleep(2)
    def propertyclass(self):
        self.click_propertyclassstar()
        time.sleep(2)
    def paylater(self):
        self.click_paylater()
        time.sleep(2)
    def freecancelation(self):
        self.click_freecancel()
        time.sleep(2)
    def amenities_breakfast(self):
        self.click_amenitiesbreakfast()
        time.sleep(2)
    def select_hotel(self):
        time.sleep(2)
        self.click_select_hotel()
        time.sleep(2)



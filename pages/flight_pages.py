
from selenium import webdriver
from base.selenium_driver import SeleniumDriver
import time
import utilities

class FlightPage(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver=driver

    #locators
    _flight_tab="tab-flight-tab-hp"
    _roundtrip_tab=" //label[@id='flight-type-roundtrip-label-hp-flight']"
    _destination_tab="//*[@id='flight-origin-hp-flight']"
    _destination_select="//a[@id='aria-option-1']//span[2]"
    _arrive_tab="//*[@id='flight-destination-hp-flight']"
    _arrive_select="//*[@id='aria-option-0']/span[2]/div"
    _calenderdeparture_tab="flight-departing-hp-flight"
    _datedeparture="//button[@data-day='25' and @data-month='8']"
    _calenderarrive_tab="flight-returning-hp-flight"
    _datearrive="//button[@data-day='28' and @data-month='8']"
    _travelers_tab="//div[@id='traveler-selector-hp-flight']//div/ul/li/button"
    _plus_tab="//*[@id='traveler-selector-hp-flight']/div/ul/li/div/div/div/div[1]/div[4]/button/span[1]"
    _close_tab="//*[@id='traveler-selector-hp-flight']/div/ul/li/div/footer/div/div[2]/button"
    _search_tab="#gcw-flights-form-hp-flight > div.cols-nested.ab25184-submit > label > button"
    _nonstop_tab=" //input[@id='stopFilter_stops-0']"
    _firstflight_tab="//li[@id='flight-module-2019-09-25t07:41:00-04:00-coach-bos-jfk-aa-1283_2019-09-28t23:00:00-04:00-coach-jfk-bos-aa-1278_']//div[contains(@class,'grid-container standard-padding')]//button[@class='btn-secondary btn-action t-select-btn']"
    _selectfare_tab="//*[@id='basic-economy-tray-content-1']/div/div/div[1]/button"
    _secondflight_tab="//li[@id='flight-module-2019-09-25t07:41:00-04:00-coach-bos-jfk-aa-1283_2019-09-28t23:00:00-04:00-coach-jfk-bos-aa-1278_']//div[contains(@class,'grid-container standard-padding')]//button[@class='btn-secondary btn-action t-select-btn']"
    _nothanks_tab="//a[@id='forcedChoiceNoThanks']"
    _booking_tab="bookButton"
    _firsttr_name="//input[@id='firstname[0]']"
    _firsttr_lastname="//input[@id='lastname[0]']"
    _phone_number="//input[@id='phone-number[0]']"
    _firsttr_gender="//input[@id='gender_female[0]']"
    _firsttr_mob=" #date_of_birth_month0"
    _firsttr_mob1="//select[@id='date_of_birth_month0']//option[contains(text(),'03 - Mar')]"
    _firsttr_dob="#date_of_birth_day[0]"
    _firsttr_dob1="//select[@id='date_of_birth_day[0]']//option[contains(text(),'03')]"
    _firsttr_yob="#date_of_birth_year[0]"
    _firsttr_yob1="//select[@id='date_of_birth_year[0]']//option[contains(text(),'1990')]"
    _secondtr_name=" //input[@id='firstname[1]']"
    _secondtr_lastname="//input[@id='lastname[1]']"
    _secondtr_gender="//input[@id='gender_male[1]']"
    _secondtr_mob="#date_of_birth_month1"
    _secondtr_mob1="//select[@id='date_of_birth_month1']//option[contains(text(),'06 - Jun')]"
    _secondtr_dob="#date_of_birth_day[1]"
    _secondtr_dob1="//select[@id='date_of_birth_day[1]']//option[contains(text(),'06')]"
    _secondtr_yob="#date_of_birth_year[1]"
    _secondtr_yob1="//select[@id='date_of_birth_year[1]']//option[contains(text(),'1990')]"
    _no_insurance="//input[@id='no_insurance']"
    _name_oncard="//label[@class='text cc-cardholder-name']//input[@name='creditCards[0].cardholder_name']"
    _card_number=" //input[@id='creditCardInput']"
    _expiration_month="//select[@name='creditCards[0].expiration_month']"
    _expiration_month1="//option[contains(text(),'03-Mar')]"
    _expiration_year="//select[@name='creditCards[0].expiration_year']"
    _expiration_year1="//option[contains(text(),'2024')]"
    _security_code="//*[@id='new_cc_security_code']"
    _billing_address1="//input[@placeholder='(ex. 123 Main)']"
    _billing_address2="//input[@placeholder='(ex. Suite 400, Apt. 4B)']"
    _billingcity=" //input[@name='creditCards[0].city']"
    _billing_state="//select[@name='creditCards[0].state']"
    _billing_state1="//option[contains(text(),'AL')]"
    _billing_zipcode="//input[@name='creditCards[0].zipcode']"
    _conf_email="//fieldset[contains(@class,'email-margin create-account-enabled')]//input[@name='email'] "
    _create_password="//fieldset[contains(@class,'account-creation-fieldset')]//input[@name='password']"
    _confirm_password="//input[@name='repeat_password']"
    _complete_booking="//button[@id='complete-booking']"



    def clickflight(self):
        return self.elementClick(self._flight_tab, locatorType="id")
    def clickroundtrip(self):
        return  self.elementClick(self._roundtrip_tab,locatorType="xpath")
    def sendkeysdestination(self, _destination_tab):
        return self.sendKeys(_destination_tab,self._destination_tab,locatorType="xpath")
    def clickdestselect(self):
        return self.elementClick(self._destination_select,locatorType="xpath")
    def sendkeysarrive(self,_arrive_tab):
        return self.sendKeys(_arrive_tab,self._arrive_tab,locatorType="xpath")
    def clickarriveselect(self):
        return self.elementClick(self._arrive_select,locatorType="xpath")
    def clickcalenderdeparture(self):
        return self.elementClick(self._calenderdeparture_tab,locatorType="id")
    def clickdatedeparture(self):
        return self.elementClick(self._datedeparture,locatorType="xpath")
    def clickcalenderarrive(self):
        return self.elementClick(self._calenderarrive_tab,locatorType="id")
    def clickdatearrive(self):
        return self.elementClick(self._datearrive,locatorType="xpath")
    def clicktravelers(self):
        return self.elementClick(self._travelers_tab,locatorType="xpath")
    def clickplus(self):
        return self.elementClick(self._plus_tab,locatorType="xpath")
    def clickclose(self):
        return self.elementClick(self._close_tab,locatorType="xpath")
    def clicksearch(self):
        return self.elementClick(self._search_tab,locatorType="css")
    def clicknonstop(self):
        return self.elementClick(self._nonstop_tab, locatorType="xpath")
    def clickfirstflight(self):
        return self.elementClick(self._firstflight_tab,locatorType="xpath")
    def clickselectfare(self):
        return self.elementClick(self._selectfare_tab,locatorType="xpath")
    def clicksecondflight(self):
        return self.elementClick(self._secondflight_tab,locatorType="xpath")
    def clicknothanks(self):
        return self.elementClick(self._nothanks_tab,locatorType="xpath")
    def clickbooking(self):
        return self.elementClick(self._booking_tab,locatorType="id")
    def sendkeysfirsttr_name(self,_firsttr_name):
        return self.sendKeys(_firsttr_name,self._firsttr_name, locatorType="xpath")
    def sendkeysfirsttr_lastname(self,_firsttr_lastname):
        return self.sendKeys(_firsttr_lastname,self._firsttr_lastname, locatorType="xpath")
    def sendkeys_phonenumber(self,_phonenumber):
        return self.sendKeys(_phonenumber,self._phone_number, locatorType="xpath")
    def click_firsttr_gender(self):
        return self.elementClick(self._firsttr_gender, locatorType="xpath")
    def click_firsttr_mob(self):
        return self.elementClick(self._firsttr_mob, locatorType="css")
    def click_firsttr_mob1(self):
        return self.elementClick(self._firsttr_mob1, locatorType="xpath")
    def click_firsttr_dob(self):
        return self.elementClick(self._firsttr_dob, locatorType="css")
    def click_firsttr_dob1(self):
        return self.elementClick(self._firsttr_dob1,locatorType="xpath")
    def click_firsttr_yob(self):
        return self.elementClick(self._firsttr_yob,locatorType="css")
    def click_firsttr_yob1(self):
        return self.elementClick(self._firsttr_yob1, locatorType="xpath")
    def sendkeys_secondtr_name(self,_secondtr_name):
        return self.sendKeys(_secondtr_name,self._secondtr_name, locatorType="xpath")
    def sendkeys_secondtr_lastname(self,_secondtr_lastname):
        return self.sendKeys(_secondtr_lastname,self._secondtr_lastname, locatorType="xpath")
    def click_secondtr_gender(self):
        return self.elementClick( self._secondtr_gender, locatorType="xpath")
    def click_secondtr_mob(self):
        return self.elementClick(self._secondtr_mob, locatorType="css")
    def click_secondtr_mob1(self):
        return self.elementClick(self._secondtr_mob1,locatorType="xpath")
    def click_secondtr_dob(self):
        return self.elementClick(self._secondtr_dob, locatorType="css")
    def click_secondtr_dob1(self):
        return self.elementClick(self._secondtr_dob1, locatorType="xpath")
    def click_secondtr_yob(self):
        return self.elementClick(self._secondtr_yob, locatorType="css")
    def click_secondtr_yob1(self):
        return self.elementClick(self._secondtr_yob1, locatorType="xpath")
    def click_noinsurence(self):
        return self.elementClick(self._no_insurance,locatorType="xpath")
    def sendkeys_name_oncard(self,_name_oncard):
        return self.sendKeys(_name_oncard,self._name_oncard,locatorType="xpath")
    def sendkeys_card_number(self, _card_number):
        return self.sendKeys(_card_number,self._card_number,locatorType="xpath")
    def click_expiration_month(self):
        return self.elementClick(self._expiration_month,locatorType="xpath")
    def click_expiration_month1(self):
        return self.elementClick(self._expiration_month1,locatorType="xpath")
    def click_expiration_year(self):
        return self.elementClick(self._expiration_year, locatorType="xpath")
    def click_expiration_year1(self):
        return self.elementClick(self._expiration_year1, locatorType="xpath")
    def sendkeys_security_code(self,_security_code):
        return self.sendKeys(_security_code,self._expiration_year, locatorType="xpath")
    def sendkeys_billing_address1(self,_billing_address1):
        return self.sendKeys(_billing_address1,self._billing_address1, locatorType="xpath")
    def sendkeys_billing_address2(self,_billing_address2):
        return self.sendKeys(_billing_address2,self._billing_address2, locatorType="xpath")
    def sendkeys_billingcity(self,_billingcity):
        return self.sendKeys(_billingcity,self._billingcity, locatorType="xpath")
    def click_billing_state(self):
        return self.elementClick(self._billing_state,locatorType="xpath")
    def click_billing_state1(self):
        return self.elementClick(self._billing_state1,locatorType="xpath")
    def sendkeys_billing_zipcode(self,_billing_zipcode):
        return self.sendKeys(_billing_zipcode,self._billing_zipcode,locatorType="xpath")
    def sendkeys_conf_email(self, _conf_email):
        return self.sendKeys(_conf_email,self._conf_email, locatorType="xpath")
    def sendkeys_create_password(self, _create_password):
        return self.sendKeys(_create_password,self._create_password, locatorType="xpath")
    def sendkeys_confirm_password(self, _confirm_password):
        return self.sendKeys(_confirm_password, self._confirm_password, locatorType="xpath")
    def click_complete_booking(self):
        return self.elementClick(self._complete_booking,locatorType="xpath")




    def flight(self):
        self.clickflight()
        time.sleep(2)
    def rounttrip(self):
        self.clickroundtrip()
        time.sleep(2)
    def destinationcity(self,destination):
        self.sendkeysdestination(destination)
        time.sleep(2)
    def destinationselect(self):
        self.clickdestselect()
        time.sleep(2)
    def arrivecity(self,arrive):
        self.sendkeysarrive(arrive)
        time.sleep(2)
    def arriveselect(self):
        self.clickarriveselect()
        time.sleep(2)
    def calenderdeparture(self):
        self.clickcalenderdeparture()
        time.sleep(2)
    def datedeparture(self):
        self.clickdatedeparture()
        time.sleep(2)
    def calenderarrive(self):
        self.clickcalenderarrive()
        time.sleep(2)
    def datearrive(self):
        self.clickdatearrive()
        time.sleep(2)
    def travelers(self):
        self.clicktravelers()
        time.sleep(2)
    def travelers_plus(self):
        self.clickplus()
        time.sleep(2)
    def close_tab(self):
        self.clickclose()
        time.sleep(2)
    def search(self):
        self.clicksearch()
        time.sleep(2)
    def nonstop(self):
        self.clicknonstop()
        time.sleep(2)
    def firstflight(self):
        self.clickfirstflight()
        time.sleep(2)
    def selectfare(self):
        self.clickselectfare()
        time.sleep(2)
    def secondflight(self):
        self.clicksecondflight()
        time.sleep(2)
    def nothanks(self):
        self.clicknothanks()
        time.sleep(2)
    def booking(self):
        self.clickbooking()
        time.sleep(2)
    def firsttr_name(self,firsttr_name):
        self.sendkeysfirsttr_name(firsttr_name)
        time.sleep(2)
    def firsttr_lastname(self,firsttr_lastname):
        self.sendkeysfirsttr_lastname(firsttr_lastname)
        time.sleep(2)
    def phonenumber(self,phonenumber):
        self.sendkeys_phonenumber(phonenumber)
        time.sleep(2)
    def firsttr_gender(self):
        self.click_firsttr_gender()
        time.sleep(2)
    def firsttr_mob(self):
        self.click_firsttr_mob()
        time.sleep(2)
    def firsttr_mob1(self):
        self.click_firsttr_mob1()
        time.sleep(2)
    def firsttr_dob(self):
        self.click_firsttr_dob()
        time.sleep(2)
    def firsttr_dob1(self):
        self.click_firsttr_dob1()
        time.sleep(2)
    def firsttr_yob(self):
        self.click_firsttr_yob()
        time.sleep(2)
    def firsttr_yob1(self):
        self.click_firsttr_yob1()
        time.sleep(2)
    def secondtr_name(self,secondtr_name):
        self.sendkeys_secondtr_name(secondtr_name)
        time.sleep(2)
    def secondtr_lastname(self,secondtr_lastname):
        self.sendkeys_secondtr_lastname(secondtr_lastname)
        time.sleep(2)
    def secondtr_gender(self):
        self.click_secondtr_gender()
        time.sleep(2)
    def secondtr_mob(self):
        self.click_secondtr_mob()
        time.sleep(2)
    def secondtr_mob1(self):
        self.click_secondtr_mob1()
        time.sleep(2)
    def secondtr_dob(self):
        self.click_secondtr_dob()
        time.sleep(2)
    def secondtr_dob1(self):
        self.click_secondtr_dob1()
        time.sleep(2)
    def secondtr_yob(self):
        self.click_secondtr_yob()
        time.sleep(2)
    def secondtr_yob1(self):
        self.click_secondtr_yob1()
        time.sleep(2)
    def noinsurance(self):
        self.click_noinsurence()
        time.sleep(2)
    def name_oncard(self,nameoncard):
        self.sendkeys_name_oncard(nameoncard)
        time.sleep(2)
    def card_number(self,cardnumber):
        self.sendkeys_card_number(cardnumber)
        time.sleep(2)
    def expiration_month(self):
        self.click_expiration_month()
        time.sleep(2)
    def expiration_month1(self):
        self.click_expiration_month1()
        time.sleep(2)
    def expiration_year(self):
        self.click_expiration_year()
        time.sleep(2)
    def expiration_year1(self):
        self.click_expiration_year1()
        time.sleep(2)
    def security_code(self,securitycode):
        self.sendkeys_security_code(securitycode)
        time.sleep(2)
    def billing_address1(self,address1):
        self.sendkeys_billing_address1(address1)
        time.sleep(2)
    def billing_address2(self,address2):
        self.sendkeys_billing_address2(address2)
        time.sleep(2)
    def billingcity(self,city):
        self.sendkeys_billingcity(city)
        time.sleep(2)
    def billing_state(self):
        self.click_billing_state()
        time.sleep(2)
    def billing_state1(self):
        self.click_billing_state1()
        time.sleep(2)
    def billing_zipcode(self,zipcode):
        self.sendkeys_billing_zipcode(zipcode)
        time.sleep(2)
    def conf_email(self,email):
        self.sendkeys_conf_email(email)
        time.sleep(2)
    def create_password(self,createpassword):
        self.sendkeys_create_password(createpassword)
        time.sleep(2)
    def confirm_password(self,confirmpassword):
        self.sendkeys_confirm_password(confirmpassword)
        time.sleep(2)
    def complete_booking(self):
        self.click_complete_booking()
        time.sleep(2)


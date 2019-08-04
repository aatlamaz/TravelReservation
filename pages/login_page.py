from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from base.selenium_driver import SeleniumDriver

class LoginPage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators

    _account="//button[@id='header-account-menu']"
    _sign_in="//a[@id='account-signin']"
    _email_address="#gss-signin-email"
    _password="#gss-signin-password"
    _signin="//button[@id='gss-signin-submit']"





    def clickAccount(self):
        self.elementClick(self._account, locatorType='xpath')

    def clickSign_In(self):
        self.elementClick(self._sign_in, locatorType='xpath')

    def sendkeyEmail(self, email):
        self.sendKeys(email, self._email_address, locatorType="css")

    def sendkeyPassword(self, psswrd):
        self.sendKeys(psswrd, self._password, locatorType="css")

    def clickSignIn(self):
        self.elementClick(self._signin, locatorType='xpath')



    def login(self, email="", psswrd=""):

        self.clickAccount()
        time.sleep(1)

        self.clickSign_In()
        time.sleep(1)

        self.sendkeyEmail(email)
        time.sleep(1)

        self.sendkeyPassword(psswrd)
        time.sleep(1)

        self.clickSignIn()
        time.sleep(1)





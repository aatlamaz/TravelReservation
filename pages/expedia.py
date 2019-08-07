import time
from selenium import webdriver

class Expedia123():
    def test(self):
        baseUrl = "https://www.expedia.com/"
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(2)

        click_flight = driver.find_element_by_xpath("//span[@class='tab-label'][contains(text(),'Flights')]")
        click_flight.click()

        orig_city = driver.find_element_by_xpath("//input[@id='flight-origin-hp-flight']")
        orig_city.send_keys('Bos')
        #time.sleep(2)
        #element_createAcc = driver.find_element_by_xpath("//a[@id='account-register']")
        #element_createAcc.click()
ff = Expedia()
ff.test()


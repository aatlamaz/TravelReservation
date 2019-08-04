from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# https://wiki.saucelabs.com/display/DOCS/Example+Selenium+Scripts+for+Automated+Website+Tests
# https://wiki.saucelabs.com/display/DOCS/Python+Test+Setup+Example

# The command_executor tells the test to run on Sauce, while the desired_capabilities
# parameter tells us which browsers and OS to spin up.
desired_cap = {
    'platform': "Mac OS X 10.12.6",
    'browserName': "chrome",
    'version': "31",
}
driver = webdriver.Remote(
    command_executor='http://letskodeit:a2424343-147f-4107-93de-82cedafc5b1b@ondemand.saucelabs.com:80/wd/hub',
    desired_capabilities=desired_cap)

# This is your test logic. You can add multiple tests here.
driver.implicitly_wait(10)
driver.get("https://www.google.com")
if not "Google" in driver.title:
    raise Exception("Unable to load google page!")
elem = driver.find_element_by_name("q")
elem.send_keys("Lets Kode It")
elem.submit()
print(driver.title)

# This is where you tell Sauce Labs to stop running tests on your behalf.
# It's important so that you aren't billed after your test finishes.
driver.quit()
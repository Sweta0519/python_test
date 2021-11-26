# Good example of how to start RDC Test
# Also example of dismissing/accepting an iOS alert
# author Max Dobeck

from appium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from appium.webdriver.common.touch_action import TouchAction
import os
import time
from sauceclient import SauceClient

from selenium.webdriver.support.wait import WebDriverWait

username = os.environ.get('SAUCE_USERNAME')
access_key = os.environ.get('SAUCE_ACCESS_KEY')
sauce_client = SauceClient(username, access_key)

desired_capabilities = {}
desired_capabilities['platformName'] = 'Android'
desired_capabilities['automationName'] = 'uiautomator2'
#desired_capabilities['appiumVersion'] = '1.21.0'
desired_capabilities['platformVersion'] = '6'
desired_capabilities['deviceName'] = "(Samsung Galaxy Xcover 3)||(ZTE Blade V7 lite)"
desired_capabilities['userName'] = os.getenv("SAUCE_USERNAME")
desired_capabilities['accessKey'] = os.getenv("SAUCE_ACCESS_KEY")
desired_capabilities['build'] = "build_chime112670"
desired_capabilities['phoneOnly'] = True
# 3. Where is your selected device located?
EU_endpoint = 'http://ondemand.eu-central-1.saucelabs.com/wd/hub'
US_endpoint = 'http://ondemand.us-west-1.saucelabs.com/wd/hub'
# The driver will take care of establishing the connection, so we must provide
# it with the correct endpoint and the requested capabilities.
for x in range(101):
    driver = webdriver.Remote(US_endpoint, desired_capabilities=desired_capabilities)
    test_name= "Allocate Android 6 Devices"+str(x)
    driver.execute_script("sauce:job-name=%s" % test_name)

    try:
        #driver.maximize_window()
        driver.get("https://www-1233.dmp.aig.com/personal/more-insurance/singapore-travel-assist")
        time.sleep(10)
        wait = WebDriverWait(driver, 60)
        driver.refresh()
        driver.execute_script("sauce:job-result=passed")

    except Exception as e:
        #sauce_client.jobs.update_job(driver.session_id, passed=False)
        driver.execute_script("sauce:job-result=failed")
        print(e)
        print(driver.session_id)
        driver.quit()
        exit(1)


driver.quit()


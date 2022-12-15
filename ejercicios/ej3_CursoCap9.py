import unittest
from appium import webdriver
import time

class MyTestCase(unittest.TestCase):

    def test_uso_de_xpath(self):
        desired_cap = {
            "platformName": "Android",
            "appium:automationName": "UiAutomator1",
            "appium:appPackage": "com.android.calculator2",
            "appium:appActivity": "com.android.calculator2.Calculator"
        }

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)


if __name__ == '__main__':
    unittest.main()

from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "appium:automationName": "UiAutomator1",
  "appium:appPackage": "com.android.calculator2",
  "appium:appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

driver.find_element()
#######----------DISPOSITIVO EMULADO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "9",
  "appium:deviceName": "generic_x86_arm",
  "appium:automationName": "UiAutomator1",
  "appium:appPackage": "com.android.calculator2",
  "appium:appActivity": "com.android.calculator2.Calculator"
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

# suma de dos numeros

driver.find_element(By.ID, "com.android.calculator2:id/digit_7").click()
driver.find_element(By.ID, "com.android.calculator2:id/op_add").click()
driver.find_element(By.ID, "com.android.calculator2:id/digit_5").click()
driver.find_element(By.ID, "com.android.calculator2:id/eq").click()

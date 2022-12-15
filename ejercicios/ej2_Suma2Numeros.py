#######----------DISPOSITIVO FÍSICO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "mdh15lm",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.google.android.calculator",
  "appium:appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

# suma de dos numeros

driver.find_element(By.ID, "com.google.android.calculator:id/digit_7").click()
driver.find_element(By.ID, "com.google.android.calculator:id/op_add").click()
driver.find_element(By.ID, "com.google.android.calculator:id/digit_5").click()
driver.find_element(By.ID, "com.google.android.calculator:id/eq").click()
driver.find_element(By.ID, "com.google.android.calculator:id/op_div").click()
driver.find_element(By.ID, "com.google.android.calculator:id/digit_6").click()
driver.find_element(By.ID, "com.google.android.calculator:id/eq").click()

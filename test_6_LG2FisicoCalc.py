from appium import webdriver
from selenium.webdriver.common.by import By
from funciones.Calculadoras import Calculadora
import pytest

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "mdh15lm",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.google.android.calculator",
  "appium:appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

cosa = 'com.google.android.calculator:id'

driver.find_element(By.ID, cosa + "/digit_7").click()
driver.find_element(By.ID, cosa + "/op_add").click()
driver.find_element(By.ID, cosa + "/digit_5").click()
driver.find_element(By.ID, cosa + "/eq").click()

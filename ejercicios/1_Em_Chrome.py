#######----------DISPOSITIVO EMULADO----------#######

##--------------- KHAN ACADEMY ---------------##

import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "9",
  "appium:deviceName": "generic_x86_arm",
  "appium:automationName": "UiAutomator1",
  "appium:appPackage": "com.android.chrome",
  "appium:appActivity": "com.google.android.apps.chrome.Main"
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

# cerrar inicio
time.sleep(2)
driver.find_element(By.ID, "com.android.chrome:id/terms_accept").click()
driver.find_element(By.ID, "com.android.chrome:id/negative_button").click()

# ingresar busqueda
time.sleep(1)
driver.find_element(By.ID, "com.android.chrome:id/search_box_text").click()
driver.hide_keyboard()
driver.find_element(By.ID, "com.android.chrome:id/url_bar").send_keys("https://es.khanacademy.org/science")
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.LinearLayout/android.widget.TextView[1]").click()

time.sleep(3)

#driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View").click()

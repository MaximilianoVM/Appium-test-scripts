#######----------DISPOSITIVO EMULADO----------#######

##--------------- ALUMNOS UABC ---------------##

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
driver.find_element(By.ID, "com.android.chrome:id/url_bar").send_keys("https://alumnos.uabc.mx/web/alumnos/bienvenido")
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]").click()


####======= Alumnos Uabc =======####

time.sleep(4)
driver.find_element(By.ID, "topNavToggler").click()
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View/android.view.View").click()

time.sleep(1)

###################
usuario=""
contra=""
###################

driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").click()
driver.hide_keyboard()
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").clear()
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").send_keys(usuario)
driver.hide_keyboard()

driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").click()
driver.hide_keyboard()
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").send_keys(contra)
driver.hide_keyboard()

time.sleep(3)

#driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_rtqd").click()

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button").click()
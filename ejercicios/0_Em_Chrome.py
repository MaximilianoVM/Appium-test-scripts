#######----------DISPOSITIVO EMULADO----------#######

##--------------- ALUMNOS UABC ---------------##

import time

from appium import webdriver
from selenium.webdriver.common.by import By
import appium.webdriver.common.touch_action
import funciones.datos as datos

def swipe():
    # Step 1 : Find the device width and height
    deviceSize = driver.get_window_size()

    # Step 2 : Find the x,y coordinate to swipe from Bottom to Top
    # LG2 MAX: 719x1599
    startx = 650
    endx = 650
    starty = 1250
    endy = 150

    # Step 3 : Create TouchAction class object
    actions = appium.webdriver.common.touch_action.TouchAction(driver)

    # Step 4 : Call long press method along with move_to method
    actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

    time.sleep(3)
    driver.implicitly_wait(2)

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
time.sleep(3)
driver.get("https://alumnos.uabc.mx/web/alumnos/bienvenido")
time.sleep(15)
driver.implicitly_wait(2)

####======= Alumnos Uabc =======####

time.sleep(4)
driver.find_element(By.ID, "topNavToggler").click()

driver.find_element(By.ID, "collapsibleNavbar").click()

time.sleep(1)

###################
usuario= nombre
contra= contrasena
###################

driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").click()
driver.hide_keyboard()
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").clear()
time.sleep(2)
#
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").send_keys("usuario")
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").clear()
#
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").send_keys(usuario)
driver.hide_keyboard()

driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").click()
driver.hide_keyboard()
driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").send_keys(contra)
driver.hide_keyboard()

time.sleep(3)

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button").click()

###================+
time.sleep(3)
swipe()
swipe()
swipe()

driver.find_element(By.ID, 'fragment-zdda-02-04-link').click()

time.sleep(15)






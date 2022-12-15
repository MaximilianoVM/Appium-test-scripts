#######----------DISPOSITIVO EMULADO----------#######

##--------------- ALUMNOS UABC ---------------##

import time

from appium import webdriver
from selenium.webdriver.common.by import By
import appium.webdriver.common.touch_action

def swipe():
    # Step 1 : Find the device width and height

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
  "appium:platformVersion": "11",
  "appium:deviceName": "mdh15lm",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "org.mozilla.firefox",
  "appium:appActivity": "org.mozilla.firefox.App"
}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

# cerrar inicio
time.sleep(2)

swipe()
swipe()

driver.find_element(By.ID, "org.mozilla.firefox:id/finish_button").click()
#driver.find_element(By.ID, "com.android.chrome:id/negative_button").click()

# ingresar busqueda
time.sleep(3)
driver.get("https://alumnos.uabc.mx/web/alumnos/bienvenido")
time.sleep(4)
driver.implicitly_wait(2)

####======= Alumnos Uabc =======####

time.sleep(4)

#driver.find_element(By.ID, "topNavToggler").click()
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.widget.Button/android.view.View").click()

time.sleep(4)
driver.find_element(By.XPATH, '//android.view.View[@content-desc="Entrar"]').click()
#//android.view.View[@content-desc="Entrar"]/android.widget.Image

time.sleep(4)

###################
usuario=""
contra=""
###################

barraUsuario = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText')

barraUsuario.click()
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[1]/android.widget.EditText
#_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login
driver.hide_keyboard()
barraUsuario.clear()
time.sleep(2)
#
barraUsuario.send_keys("usuario")
barraUsuario.clear()
#
barraUsuario.send_keys(usuario)
driver.hide_keyboard()

barraContra = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]/android.view.View[2]/android.widget.EditText')
barraContra.click()

driver.hide_keyboard()
barraContra.send_keys(contra)
driver.hide_keyboard()

time.sleep(3)

driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button').click()
#_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_rebt
#/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.FrameLayout/android.webkit.WebView/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.Button


###================+
time.sleep(3)
swipe()
swipe()
swipe()

driver.find_element(By.XPATH, '//android.view.View[@content-desc="Ver boleta"]/android.view.View').click()
#//android.view.View[@content-desc="Ver boleta"]/android.view.View
#fragment-zdda-02-04-link

time.sleep(15)






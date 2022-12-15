import time
import appium.webdriver.common.touch_action
from appium import webdriver
from selenium.webdriver.common.by import By
from funciones.Paginas import AlumnosUABC
from funciones.Navegadores import ChromeNav
import pytest

desired_cap = {
  "platformName": "Android",
  "appium:platformVersion": "11",
  "appium:deviceName": "mdh15lm",
  "appium:automationName": "UiAutomator2",
  "appium:appPackage": "com.android.chrome",
  "appium:appActivity": "com.google.android.apps.chrome.Main"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)


chrome = ChromeNav(driver)
chrome.cerrar_inicio_chrome()
time.sleep(3)
driver.get("https://www.aarp.org/espanol/salud/enfermedades-y-tratamientos/info-10-2012/trivia-sintomas-infarto.html#quest1")
time.sleep(20)
driver.implicitly_wait(2)
print("--------------------------------------      --------------------------------------")


#driver.swipe(driver.)
#action = appium.webdriver.common.touch_action.TouchAction(driver)
#action.press(el).move_to(x=10, y=-500).release().perform()


# Step 1 : Find the device width and height
deviceSize = driver.get_window_size()

# Step 2 : Find the x,y coordinate to swipe from Bottom to Top
#LG2 MAX: 719x1599
startx = 688
endx = 662
starty = 1373
endy = 140

# Step 3 : Create TouchAction class object
actions = appium.webdriver.common.touch_action.TouchAction(driver)

# Step 4 : Call long press method along with move_to method
actions.long_press(None,startx,starty).move_to(None,endx,endy).release().perform()

time.sleep(3)
driver.implicitly_wait(2)



driver.find_element(By.XPATH, '//*[@id="answer0_0"]/div[1]').click()
print("=================         =================")
time.sleep(10)
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View/android.widget.Button").click()
print("=================      =================")
time.sleep(3)

driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.widget.Button").click()

#driver.find_element(By.ID, "TopNav-login").click()


#chrome.ingresar_busqueda_nuevo()
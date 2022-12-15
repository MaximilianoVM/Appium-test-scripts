#######----------DISPOSITIVO EMULADO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By
import time


class ChromeNav(object):
    def __init__(self, driver):
        self.driver = driver

    def cerrar_inicio_chrome(self):
        # cerrar inicio
        time.sleep(2)
        self.driver.find_element(By.ID, "com.android.chrome:id/terms_accept").click()
        self.driver.find_element(By.ID, "com.android.chrome:id/negative_button").click()

    def ingresar_busqueda(self):
        # ingresar busqueda
        time.sleep(1)
        self.driver.find_element(By.ID, "com.android.chrome:id/search_box_text").click()
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, "com.android.chrome:id/url_bar").send_keys("https://alumnos.uabc.mx/web/alumnos/bienvenido")
        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.ListView/android.view.ViewGroup[1]/android.view.ViewGroup/android.widget.TextView[2]").click()

    def ingresar_busqueda_nuevo(self):
        time.sleep(3)
        barraGoogXpath = '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View/android.widget.EditText'
        self.driver.find_element(By.XPATH, barraGoogXpath ).click()
        self.driver.hide_keyboard()
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.EditText').send_keys("https://alumnos.uabc.mx/web/alumnos/bienvenido")
#######----------DISPOSITIVO EMULADO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By
import time

class AlumnosUABC(object):
    def __init__(self, driver):
        self.driver = driver

    def puerta(self):
        time.sleep(4)
        self.driver.find_element(By.ID, "topNavToggler").click()
        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View[3]/android.widget.ListView/android.view.View/android.view.View").click()
        time.sleep(1)

    def ingresar(self, correo, contrasenia):
        usuario = correo
        contra = contrasenia
        ###################

        self.driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").click()
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").clear()
        self.driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_login").send_keys(
            usuario)
        self.driver.hide_keyboard()

        self.driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").click()
        self.driver.hide_keyboard()
        self.driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_password").send_keys(
            contra)
        self.driver.hide_keyboard()

        time.sleep(3)

        # driver.find_element(By.ID, "_com_liferay_login_web_portlet_LoginPortlet_INSTANCE_0_rtqd").click()

        self.driver.find_element(By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.webkit.WebView/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View[2]/android.view.View[3]/android.view.View[2]/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View/android.widget.Button").click()



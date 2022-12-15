#######----------DISPOSITIVO EMULADO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By


class Calculadora(object):
    def __init__(self, driver):
        self.driver = driver

    def suma_dos_numeros(self):
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_7").click()
        self.driver.find_element(By.ID, "com.android.calculator2:id/op_add").click()
        self.driver.find_element(By.ID, "com.android.calculator2:id/digit_5").click()
        self.driver.find_element(By.ID, "com.android.calculator2:id/eq").click()

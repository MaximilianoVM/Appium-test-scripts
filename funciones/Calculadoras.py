#######----------DISPOSITIVO EMULADO----------#######

from appium import webdriver
from selenium.webdriver.common.by import By


class Calculadora(object):
    def __init__(self, driver):
        self.driver = driver

    def suma_dos_numeros(self, package):
        if package == 'com.google.android.calculator':
            cosa = 'com.google.android.calculator:id'
        else:
            cosa = 'com.android.calculator2:id'

        self.driver.find_element(By.ID, cosa + "/digit_7").click()
        self.driver.find_element(By.ID, cosa + "/op_add").click()
        self.driver.find_element(By.ID, cosa + "/digit_5").click()
        self.driver.find_element(By.ID, cosa + "/eq").click()


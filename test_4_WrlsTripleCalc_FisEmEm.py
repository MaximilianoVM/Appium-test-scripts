from appium import webdriver
from selenium.webdriver.common.by import By
from funciones.Calculadoras import Calculadora
import pytest

@pytest.mark.parametrize("udid, deviceName, systemPort, version, package",
                         [('10.41.35.150:5555', 'mdh15lm', '8200', '11', 'com.google.android.calculator'),
                          ('emulator-5554', 'generic_x86_arm', '8201', '9', 'com.android.calculator2'),
                          ('emulator-5556', 'generic_x86_arm', '8202', '9', 'com.android.calculator2')])
def test_calculadora(udid, deviceName, systemPort, version, package):
    desired_cap = {
      "platformName": "Android",
      "appium:platformVersion": version,
      "appium:deviceName": deviceName,
      "appium:automationName": "UiAutomator2",
      "appium:appPackage": package,
      "appium:appActivity": "com.android.calculator2.Calculator",
      "newCommandTimeout": 60,
      "systemPort": int(systemPort)
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    calculadora = Calculadora(driver)
    calculadora.suma_dos_numeros(package)

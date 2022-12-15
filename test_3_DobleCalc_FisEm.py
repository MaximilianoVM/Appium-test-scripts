from appium import webdriver
from selenium.webdriver.common.by import By
from funciones.Calculadoras import Calculadora
import pytest

@pytest.mark.parametrize("udid, deviceName, systemPort", [('emulator-5554', 'generic_x86_arm', '8200'), ('emulator-5556', 'generic_x86_arm', '8201'), ('92GBB18622575576', 'HWLDN-Q', '8202')])
def test_calculadora(udid, deviceName, systemPort):
    desired_cap = {
      "platformName": "Android",
      "appium:platformVersion": "9",
      "appium:udid": udid,
      "appium:deviceName": deviceName,
      "appium:automationName": "UiAutomator1",
      "appium:appPackage": "com.android.calculator2",
      "appium:appActivity": "com.android.calculator2.Calculator",
      "newCommandTimeout": 60,
      "systemPort": int(systemPort)
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    calculadora = Calculadora(driver)
    calculadora.suma_dos_numeros()

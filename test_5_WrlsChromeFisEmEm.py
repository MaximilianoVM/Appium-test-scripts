from appium import webdriver
from selenium.webdriver.common.by import By
from funciones.Paginas import AlumnosUABC
from funciones.Navegadores import ChromeNav
import pytest

@pytest.mark.parametrize("udid, deviceName, systemPort", [('emulator-5554', 'generic_x86_arm', '8200'), ('emulator-5556', 'generic_x86_arm', '8201'), ('10.41.35.150:5555', 'mdh15lm', '8202')])
def test_busqueda(udid, deviceName, systemPort):
    desired_cap = {
        "platformName": "Android",
        "appium:platformVersion": "9",
        "appium:udid": udid,
        "appium:deviceName": deviceName,
        "appium:automationName": "UiAutomator1",
        "appium:appPackage": "com.android.chrome",
        "appium:appActivity": "com.google.android.apps.chrome.Main",
        "newCommandTimeout": 60,
        "systemPort": int(systemPort)


    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

    chrome = ChromeNav(driver)

    chrome.cerrar_inicio_chrome()
    chrome.ingresar_busqueda()
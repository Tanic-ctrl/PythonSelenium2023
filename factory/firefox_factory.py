from selenium import webdriver
from selenium.webdriver.firefox.service import Service

FIREFOX_DRIVER_PATH = "./drivers/geckodriver.exe"
FIREFOX_SERVICE = Service(FIREFOX_DRIVER_PATH)


def create_driver():
    return webdriver.Firefox(service=FIREFOX_SERVICE)
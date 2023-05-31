import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_search_item(self):

        navbar_search = self.driver.find_element(By.XPATH, '//*[@name="search"]')
        assert navbar_search.is_displayed(), "El campo de busqueda debe mostrarse"
        navbar_search.send_keys("iphone")

        search_btn = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        assert search_btn.is_displayed(), "El boton de busqueda debe mostrarse"
        search_btn.click()

        find_item = self.driver.find_element(By.XPATH, '//img[@alt="iPhone"]')
        assert find_item.is_displayed(), "La imagen de Iphone tiene que mostrarse en el DOM"

    def teardown_method(self):
        self.driver.quit()

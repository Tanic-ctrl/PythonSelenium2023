import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_valid_option(self):
        # Select Laptops & Notebooks option from Navbar
        laptops_option = self.driver.find_element(By.XPATH, '//a[contains(text(), "Laptops & Notebooks")]')
        ActionChains(self.driver).move_to_element(laptops_option).perform()
        time.sleep(3)

        # Select Windows option
        windows_option = self.driver.find_element(By.XPATH, '//a[contains(text(), "Windows")]')
        assert windows_option.is_displayed(), "La opción Windows debe ser visible"
        assert windows_option.is_enabled(), "La opción Windows debe estar habilitado"
        windows_option.click()
        time.sleep(3)

        # Validate no items message
        items_message = self.driver.find_element(By.XPATH, '//div[@id="content"]/p')
        assert items_message.is_displayed(), "El mensaje debe ser visible"

        # Validate Continue button
        continue_button = self.driver.find_element(By.XPATH, '//a[@class="btn btn-primary"]')
        assert continue_button.is_displayed(), "El botón de Continue debe mostrarse"
        assert continue_button.is_enabled(), "El botón de Continue debe estar habilitado"
        continue_button.click()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
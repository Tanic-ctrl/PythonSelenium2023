import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = " https://demoqa.com/select-menu"


class TestDemoQAPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_standard_multi_select(self):
        time.sleep(2)
        element = self.driver.find_element(By.ID, "cars")
        select = Select(element)
        select.select_by_visible_text("Volvo")
        select.select_by_value("audi")
        assert select.first_selected_option.text == "Volvo"
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()


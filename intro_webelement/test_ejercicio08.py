from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html"


class TestDownloadPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.implicitly_wait(3)
        self.wait_driver = WebDriverWait(self.driver, 45)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_download_progress(self):
        # Obtener el elemento y verificar que aparece el mensaje 100% después de presionar download
        download_button = self.__find_clickable_element(By.XPATH, '//button[@id="cricle-btn"]')
        download_button.click()
        self.__find_by_text(By.XPATH, '//*[@class="percenttext"]', '100')

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def teardown_method(self):
        self.driver.quit()

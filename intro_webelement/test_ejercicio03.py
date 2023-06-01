import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_invalid_login(self):
        # Enter an invalid email
        email_input = self.driver.find_element(By.XPATH, '//input[@name="email"]')
        assert email_input.is_displayed(), "El campo email address debe mostrarse"
        assert email_input.is_enabled(), "El campo email debe estar habilitado"
        email_input.click()
        email_input.send_keys("test@email.com")
        time.sleep(3)

        # Enter password
        pwd_input = self.driver.find_element(By.XPATH, '//input[@name="password"]')
        assert pwd_input.is_displayed(), "El campo password debe mostrarse"
        assert pwd_input.is_enabled(), "El campo password debe estar habilitado"
        pwd_input.click()
        pwd_input.send_keys("pwd1234!")
        time.sleep(3)

        # Press Login button
        login_button = self.driver.find_element(By.XPATH, '//input[@class="btn btn-primary"]')
        assert login_button.is_displayed(), "El boton de login debe mostrarse"
        assert login_button.is_enabled(), "El boton de login debe estar habilitado"
        login_button.click()

        # Validate warning message
        warning_msg = self.driver.find_element(By.XPATH, '//*[contains(text(), "Warning")]')
        assert warning_msg.is_displayed(), "El warning error debe mostrarse"
        assert warning_msg.is_enabled(), "El warning error debe estar habilitado"
        time.sleep(3)
    def teardown_method(self):
        self.driver.quit()

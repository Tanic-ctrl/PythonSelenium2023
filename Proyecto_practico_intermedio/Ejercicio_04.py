import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from factory.webdriver_factory import create_chrome_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = create_chrome_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 20)

    def test_currency_option(self):
        # Enter search term Samsung
        search_term = self.__find_clickable_element(By.NAME, "search")
        search_term.click()

        search_term.send_keys("Samsung SyncMaster 941BW")
        search_term.send_keys(Keys.ENTER)

        # Select Samsung SyncMaster option
        item = self.__find_clickable_element(By.PARTIAL_LINK_TEXT, 'Samsung SyncMaster 941BW')
        item.click()

        # Click on Currency option and select USD
        currency_option = self.__find_clickable_element(By.XPATH, '//*[@id="form-currency"]//button/span')
        currency_option.click()

        usd_currency_option = self.__find_clickable_element(By.XPATH, '//button[@name="USD"]')
        usd_currency_option.click()

        time.sleep(3)

        usd_price = self.__find_visible_element(By.XPATH, '//h2[contains(text(), "$242.00")]').text

        # Click on Currency option
        option_currency = self.__find_visible_element(By.XPATH, '//*[@id="form-currency"]//button/span')
        option_currency.click()

        # Select Euro currency option
        eur_currency_option = self.__find_visible_element(By.XPATH, '//button[@name="EUR"]')
        eur_currency_option.click()

        eur_price = self.__find_visible_element(By.XPATH, '//h2[contains(text(), "189.87€")]').text

        # Validate item price is minor than in dollar
        assert usd_price.replace("$", "") > eur_price.replace("€", ""), "The EUR price should be minor" \
                                                                        "than USD"

        time.sleep(3)

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def __wait_until_disappears(self, by: By, value: str):
        self.wait_driver.until(EC.invisibility_of_element((by, value)))

    def teardown(self):
        self.driver.quit()
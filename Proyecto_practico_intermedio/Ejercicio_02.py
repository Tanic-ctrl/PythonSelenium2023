from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from factory.webdriver_factory import create_firefox_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = create_firefox_driver()
        self.driver.get(URL)
        self.wait_driver = WebDriverWait(self.driver, 20)

    def test_search_products(self):
        # Enter the search term "display"
        search_term = self.__find_clickable_element(By.NAME, "search")
        search_term.send_keys("display")
        search_term.send_keys(Keys.ENTER)

        # Validate if the search term is visible
        self.__find_visible_element(By.XPATH, '//p[contains(text(),"There is no product")]')

        # Select the Search in product descriptions checkbox
        select_checkbox = self.__find_clickable_element(By.XPATH, '//input[@name="description"]')
        select_checkbox.click()

        # Search the term "display"
        search_button = self.__find_clickable_element(By.XPATH, '//input[@id="button-search"]')
        search_button.click()

        #  Validate search term results
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "Apple Cinema 30")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iPod Nano")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iPod Touch")]')
        self.__find_visible_element(By.XPATH, '//a[contains(text(), "MacBook Pro")]')

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def teardown(self):
        self.driver.quit()
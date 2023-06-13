from selenium.webdriver import ActionChains
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

    def test_add_item_to_cart(self):

        desktop_option = self.__find_visible_element(By.XPATH, '//a[contains(text(), "Desktops")]')
        ActionChains(self.driver).move_to_element(desktop_option).perform()

        select_mac_option = self.__find_clickable_element(By.XPATH, '//a[contains(text(), "Mac")]')
        select_mac_option .click()

        self.__find_visible_element(By.XPATH, '//a[contains(text(), "iMac")]')

        cart_option = self.__find_clickable_element(By.XPATH, '//*[contains(@onclick, "cart.add")]')
        cart_option.click()

        self.__find_by_text(By.ID, 'cart-total', '1 item(s) - $122.00')

    def __find_clickable_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.element_to_be_clickable((by, value)))

    def __find_visible_element(self, by: By, value: str) -> WebElement:
        return self.wait_driver.until(EC.visibility_of_element_located((by, value)))

    def __find_by_text(self, by: By, value: str, text: str) -> WebElement:
        return self.wait_driver.until(EC.text_to_be_present_in_element((by, value), text))

    def teardown(self):
        self.driver.quit()

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
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_select_tablets_option(self):
        # Expected values
        exp_title = "Samsung Galaxy Tab 10.1"
        exp_cost = "$241.99"
        exp_wish_list = "1"
        exp_success_msg = "Success: You have added"

        # Select tablets options
        # tablets_option = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[4]/a")
        tablets_option = self.driver.find_element(By.XPATH, "//a[contains(@href,'category&path=57')]")
        assert tablets_option.is_displayed() and tablets_option.is_enabled(), "La opcion tablets tiene que ser visible"
        tablets_option.click()
        time.sleep(2)

        # Display expected item
        # tablet_item = self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div/div[1]/a")
        title_item = self.driver.find_element(By.XPATH, "//div[@class='caption']//a[contains(@href,'product_id=49')]")
        assert title_item.is_displayed() and title_item.is_enabled(), "El titulo tiene que ser visible"
        assert title_item.text == exp_title, f"title should be {exp_title}"

        # Select displayed item
        title_item.click()
        tablet_info = self.driver.find_element(By.XPATH, "//*[@id='product-product']/ul/li[3]/a")
        assert tablet_info.is_displayed(), "Muestra la informacion del item seleccionado"

        # Display item cost
        item_cost = self.driver.find_element(By.XPATH, "//div[@id='content']//li//h2")
        assert item_cost.is_displayed(), "El costo del item seleccionado debe ser visible"
        assert item_cost.text == exp_cost, f"El costo tiene que ser {exp_cost}"

        # Add to the wishlist
        wishlist_option = self.driver.find_element(By.XPATH, "//div[@id='content']//button/i[@class='fa fa-heart']")
        assert wishlist_option.is_displayed() and wishlist_option.is_enabled(), "La option Wishlist debe ser visible"
        wishlist_option.click()
        time.sleep(3)

        # Validate wishlist updated
        wish_list_alert = self.driver.find_element(By.XPATH, "//a[@id='wishlist-total']/span")
        assert wish_list_alert.is_displayed(), f"La alerta de wishlist actualizada debe ser visible"
        assert exp_wish_list in wish_list_alert.text, f"Mensaje wishlist actualizada debe contener {exp_wish_list}"

        # Add to the cart
        cart_option = self.driver.find_element(By.ID, "button-cart")
        assert cart_option.is_displayed() and cart_option.is_enabled(), "La opcion del carrito deb ser visible"
        cart_option.click()
        time.sleep(3)

        cart_total = self.driver.find_element(By.XPATH, "//*[@id='cart-total']")
        assert cart_total.is_displayed(), "El item seleccionado se debe agregar al carrito"

        success_msg = self.driver.find_element(By.CLASS_NAME, "alert-success")
        assert success_msg.is_enabled(), "Success message should be displayed"
        print(success_msg.text)
        assert exp_success_msg in success_msg.text, f"Success message should contain {exp_success_msg}"

    def teardown_method(self):
        self.driver.quit()

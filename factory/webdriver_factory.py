from enum import Enum

from selenium.webdriver.remote.webdriver import WebDriver
from factory.chrome_factory import create_driver as create_chrome_driver
from factory.firefox_factory import create_driver as create_firefox_driver


class DriverType(Enum):
    """
    List of valid and accepted drivers types.
    """
    CHROME = 1
    FIREFOX = 2


def get_driver(driver_type: DriverType) -> WebDriver:
    """Get driver based on driver type.

    :param driver_type: Driver instance type to initialize
    :return: Web driver instance
    """
    if type(driver_type) is not DriverType:
        raise TypeError(f"Cannot create driver, invalid type provided: {type(driver_type)}")
    if driver_type == DriverType.CHROME:
        driver = create_chrome_driver()
    elif driver_type == DriverType.FIREFOX:
        driver = create_firefox_driver()
    else:
        raise NotImplementedError(f"Driver type not supported: {driver_type.name}")
    driver.maximize_window()
    return driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from conftest import logger


class BasePage:
    def __init__(self, driver):
        self.__driver = driver
    def get_web_driver_wait(self):
        return WebDriverWait(self.__driver, 10)

    def wait_until_element_visible(self, locator):
        return self.get_web_driver_wait().until(
            EC.visibility_of_element_located(locator)
        )

    def enter_text(self, locator, text, field_name):
        #self.__driver.find_element(locator[0], locator[1]).send_keys(text)
        element =self.get_web_driver_wait().until(
            EC.visibility_of_element_located(locator)
        )
        element.clear()
        element.send_keys(text)
        logger.info(f"entered {text} on {field_name}")

    def click(self, locator, field_name):

        element = self.get_web_driver_wait().until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        logger.info(f"clicked on {field_name}")

    def is_displayed(self, locator, field_name):
        element = self.get_web_driver_wait().until(
            EC.visibility_of_element_located(locator)
        )
        if element:
            logger.info(f"{field_name} is Displayed")
            return True
        logger.info(f"{field_name} is Not Displayed")
        return False

    def get_text(self, locator, field_name):
        element = self.wait_until_element_visible(locator)
        text = element.text
        logger.info(f"got {text} as a Text from {field_name
        }")
        return text
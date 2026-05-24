from selenium.webdriver.common.by import By

from page_object.base_page import BasePage
from utilities.db_helper import DbHelper


class HomePage(BasePage):

    __search_text_box = (By.XPATH, "//button[@title='Search for Products, Brands and More']/following-sibling::div/input")
    __searched_product = (By.XPATH, "//span[text()='{}']")
    __user_authentication_popup_close_button =(By.XPATH, "//span[text()='✕' and @role='button']")
    __user_authentication_popup = (By.XPATH, "//p[text()='Get access to your Orders, Wishlist and Recommendations']")

    def enter_search_string_in_search_box(self, value):
        self.enter_text(self.__search_text_box, value, "Product Search Box")

    def click_on_searched_product(self, value):
        locator = (self.__searched_product[0], self.__searched_product[1].format(value))
        self.click(locator, f"{value} Option")

    def close_authentication_popup(self):
        if self.is_displayed(self.__user_authentication_popup, "authentication popup"):
            self.click(self.__user_authentication_popup_close_button, "Authentication popup close Button")


    def read_user_data(self):

        value = DbHelper.execute_query("SELECT * FROM automation2026.standared;")
        print(value)
from selenium.webdriver.common.by import By

from page_object.base_page import BasePage


class ProductListPage(BasePage):

    __product_list_header = (By.XPATH, "//span[@class='_Omnvo']")

    def get_product_list_header(self):
        return self.get_text(self.__product_list_header, "Product list page header")


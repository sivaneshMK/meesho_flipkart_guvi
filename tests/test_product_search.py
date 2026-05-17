import pytest

from conftest import logger
from page_object.home_page import HomePage
from page_object.product_list_page import ProductListPage
from utilities.excel_helper import ExcelHelper


class TestProductSearch:

    def test_user_is_able_to_search_product(self, driver):
        home_page = HomePage(driver)
        data = ExcelHelper.get_test_data(file_path="C:\\Users\\sivan\\PycharmProjects\\Meesho\\test_data\\test_data.xlsx",
                                  sheet_name= "product_search",
                                  test_name="test_user_is_able_to_search_product")
        logger.info(f"Test Data is {data}")
        home_page.close_authentication_popup()
        home_page.enter_search_string_in_search_box(data["Search product"])
        home_page.click_on_searched_product(data["Search product"])
        product_list_page = ProductListPage(driver)
        assert data["Search product"] in product_list_page.get_product_list_header(), "The searched product is not listed"

    @pytest.mark.wip
    @pytest.mark.parametrize("search", ["shoe", "mobile", "kurti", "watch"])
    def test_user_is_able_to_search_different_product(self, driver, search):
        home_page = HomePage(driver)
        home_page.close_authentication_popup()
        home_page.enter_search_string_in_search_box(search)
        home_page.click_on_searched_product(search)
        product_list_page = ProductListPage(driver)
        assert search in product_list_page.get_product_list_header(), "The searched product is not listed"
        driver.back()

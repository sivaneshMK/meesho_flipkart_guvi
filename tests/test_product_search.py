from page_object.home_page import HomePage
from page_object.product_list_page import ProductListPage


class TestProductSearch:

    def test_user_is_able_to_search_product(self, driver):
        home_page = HomePage(driver)
        home_page.close_authentication_popup()
        home_page.enter_search_string_in_search_box("shoe")
        home_page.click_on_searched_product("shoe")
        product_list_page = ProductListPage(driver)
        assert "shoe" in product_list_page.get_product_list_header(), "The searched product is not listed"


"""Category page."""

from selenium.webdriver import Remote
from dp189.pages.base_page import BasePage
from dp189.components import SortByDropdownComponent, ShowNumberProductsDropdownComponent, \
    ProductsViewComponent, CategoryProductWidgetComponent, ProductCompareLinkComponent, ProductWidgetsListComponent
from dp189.locators import LocatorCategoryTitle


class CategoryPage(BasePage):
    """Category page class."""

    def __init__(self, driver: Remote) -> None:
        """All objects on the category page.

        :param driver: Remote driver.
        """
        super().__init__(driver)
        self.category_title = driver.find_element(*LocatorCategoryTitle.CATEGORY_TITLE)
        self.products_view_button = ProductsViewComponent(driver)
        self.product_compare_link = ProductCompareLinkComponent(driver)
        self.sort_by_dropdown = SortByDropdownComponent(driver)
        self.show_number_products_dropdown = ShowNumberProductsDropdownComponent(driver)


if __name__ == "__main__":
    from selenium.webdriver import Chrome
    from selenium.webdriver.chrome.options import Options

    options = Options()
    options.add_argument('--ignore-certificate-errors')
    driver = Chrome(options=options)
    driver.maximize_window()

    driver.get('http://34.71.14.206/index.php?route=information/sitemap')

    ProductWidgetsListComponent(driver).open_category("Desktops")
    list = ProductWidgetsListComponent(driver).get_list_product_widgets()

    SortByDropdownComponent(driver).click_option("Model (Z - A)")
    ShowNumberProductsDropdownComponent(driver).click_option("100")
    ProductsViewComponent(driver).click_list_view_button()
    CategoryProductWidgetComponent(driver, "iPhone").click_add_to_shopping_cart_button()
    CategoryProductWidgetComponent(driver, "Canon EOS 5D").click_add_to_wish_list_button()

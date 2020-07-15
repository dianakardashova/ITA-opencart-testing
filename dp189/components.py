from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Remote
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from .locators import LocatorsSearch, LocatorsNavBar, RightMenuLocators, LocatorsShoppingCartButton, \
    LocatorsYourPersonalDetailsComponent, LocatorsYourPasswordComponent, LocatorsRegisterPage, \
    LocatorsNewsletterComponent, LocatorsAddAddressComponent


class SearchArea:
    """"This class describes the search area common in all pages. It consists or search field and search button"""

    def __init__(self, driver):
        self._driver = driver
        self._search_field = driver.find_element(*LocatorsSearch.SEARCH_FIELD)
        self._search_button = driver.find_element(*LocatorsSearch.SEARCH_BUTTON)

    def fill_search_field_and_hit_return(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item).send_keys(Keys.RETURN)
        # return SearchPage(self._driver)

    def fill_search_field_and_click(self, item: str):
        self._search_field.clear()
        self._search_field.send_keys(item)
        self._search_button.click()
        # return SearchPage(self._driver)


class ShopCartButton:
    # TODO test functionality
    def __init__(self, driver):
        self._driver = driver
        self._shop_cart_button = driver.find_element(*LocatorsShoppingCartButton.SHOP_CART_BUTTON)

    def click_shop_cart_button(self):
        self._shop_cart_button.click()
        cart_items = self._driver.find_elements(*LocatorsShoppingCartButton.CART_ITEMS)
        if len(cart_items) == 0:
            return 'Your cart is empty!'
        else:
            return ShopCartDropdown(self._driver)


class ShopCartDropdown:
    def __init__(self, driver):
        pass


class BaseNavBar:
    """This class describes the top nav bar of the base page"""

    def __init__(self, driver):
        self._driver = driver
        self._currency = driver.find_element(*LocatorsNavBar.CURRENCY)
        self._nav_bar = driver.find_element(*LocatorsNavBar.NAVBAR)

    def click_currency_euro(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.EUR).click()

    def click_currency_pound(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.POUND).click()

    def click_currency_usd(self):
        self._currency.click()
        self._currency.find_element(*LocatorsNavBar.USD).click()

    def click_contact_us(self):
        self._nav_bar.find_element(*LocatorsNavBar.CONTACT_US).click()

    def click_wishlist(self):
        self._nav_bar.find_element(*LocatorsNavBar.WISH_LIST).click()

    def click_shopping_cart(self):
        self._nav_bar.find_element(*LocatorsNavBar.SHOPPING_CART).click()


class BaseRightMenu:
    def __init__(self, driver) -> None:
        self._driver = driver
        self._right_menu = driver.find_element_by_class_name('list-group')

    def click_my_account(self):
        self._right_menu.find_element(*RightMenuLocators.MY_ACCOUNT).click()

    def click_address_book(self):
        self._right_menu.find_element(*RightMenuLocators.ADDRESS_BOOK).click()

    def click_wish_list(self):
        self._right_menu.find_element(*RightMenuLocators.WISH_LIST).click()

    def click_order_history(self):
        self._right_menu.find_element(*RightMenuLocators.ORDER_HISTORY).click()

    def click_downloads(self):
        self._right_menu.find_element(*RightMenuLocators.DOWNLOADS).click()

    def click_recurring_payments(self):
        self._right_menu.find_element(*RightMenuLocators.RECURRING_PAYMENTS).click()

    def click_reward_points(self):
        self._right_menu.find_element(*RightMenuLocators.REWARD_POINTS).click()

    def click_returns(self):
        self._right_menu.find_element(*RightMenuLocators.RETURNS).click()

    def click_transactions(self):
        self._right_menu.find_element(*RightMenuLocators.TRANSACTIONS).click()

    def click_newsletter(self):
        self._right_menu.find_element(*RightMenuLocators.NEWSLETTER).click()


class YourPersonalDetailsComponent:
    """Your personal details form сonsists four fields to fill first name, last name, email, telephone."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields first name, last name, email, telephone.

        :param driver: Remote.
        """
        self._driver = driver
        self.first_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.FIRST_NAME_FIELD)
        self.last_name_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.LAST_NAME_FIELD)
        self.email_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.EMAIL_FIELD)
        self.telephone_field = InputFieldComponent(self._driver, LocatorsYourPersonalDetailsComponent.TELEPHONE_FIELD)


class YourPasswordComponent:
    """Your password form сonsists two fields to fill password, password confirm."""

    def __init__(self, driver: Remote) -> None:
        """Initialize input fields password field, password confirm field.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.password_field = InputFieldComponent(self._driver, LocatorsYourPasswordComponent.PASSWORD_FIELD)
        self.password_confirm_field = InputFieldComponent(self._driver,
                                                          LocatorsYourPasswordComponent.PASSWORD_CONFIRM_FIELD)


class InputFieldComponent:
    """An input field to fill with data from user."""

    def __init__(self, driver: Remote, input_field_locator: tuple, parent_element: WebElement = None) -> None:
        """Initialize the input field.

        :param driver: Remote
        :param input_field_locator: tuple (example: PASSWORD_FIELD=(By.ID, 'input-password'))
        :return: None
        """
        self._driver = driver
        self.input_field_locator = input_field_locator
        self.parent_element = parent_element

    def clear_and_fill_input_field(self, data: str) -> None:
        """Clear and fill input field with data.

        :param data: str
        :return: None
        """
        if self.parent_element:
            input_field = self.parent_element.find_element(*self.input_field_locator)
        else:
            input_field = self._driver.find_element(*self.input_field_locator)
        input_field.clear()
        input_field.send_keys(data)

    def choose_selector_by_text(self, data: str) -> None:
        """Choose option by text in selector.

        :param data: str
        :return: None
        """
        selector = Select(self._driver.find_element(*self.input_field_locator))
        selector.select_by_visible_text(data)

    def check_radio_button(self, data: str) -> None:
        radio_container = self._driver.find_element(*self.input_field_locator)
        radio_container.find_element(By.XPATH, f'//label[contains(.,"{data}")]/input').click()

    def get_error_message_for_input_field(self) -> str:
        """Get error message for input field if it were incorrect data.

        :return: str
        """
        error_message_locator = f'#{self.input_field_locator[1]} ~ div.text-danger'
        error_message = WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, error_message_locator))
        )
        return error_message.text


class NewsletterComponent:
    """Two radio buttons to subscribe or unsubscribe to newsletter."""

    def __init__(self, driver: Remote) -> None:
        """Initialize radio buttons.

        :param driver: Remote
        :return: None
        """
        self._driver = driver
        self.subscribe_radio_buttons_locator = LocatorsNewsletterComponent.SUBSCRIBE_RADIO_BUTTONS

    def is_subscribed(self) -> bool:
        """Check user is subscribed or not.

        :return: bool
        """
        self.subscribe_radio_buttons = self._driver.find_elements(*self.subscribe_radio_buttons_locator)
        for button in self.subscribe_radio_buttons:
            if button.get_attribute('checked') == 'true' and button.get_attribute('value') == '1':
                return True
        return False

    def subscribe_to_newsletter(self) -> None:
        """Subscribe to newsletter.

        :return: None
        """
        self.subscribe_to_newsletter_locator = f'[{self.subscribe_radio_buttons_locator[0]}="{self.subscribe_radio_buttons_locator[1]}"][value="1"]'
        self._driver.find_element_by_css_selector(self.subscribe_to_newsletter_locator).click()


class AddAddressComponent:
    def __init__(self, driver: Remote, parent_locator: WebElement) -> None:
        self._driver = driver
        self._parent_locator = parent_locator
        self.first_name_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.FIRST_NAME_INPUT)
        self.last_name_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.LAST_NAME_INPUT)
        self.company_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.COMPANY_INPUT)
        self.address_1_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.ADDRESS_1_INPUT)
        self.address_2_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.ADDRESS_2_INPUT)
        self.city_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.CITY_INPUT)
        self.post_code_field = InputFieldComponent(self._driver, LocatorsAddAddressComponent.POST_CODE_INPUT)
        self.country = InputFieldComponent(self._driver, LocatorsAddAddressComponent.COUNTRY_SELECTOR)
        self.region = InputFieldComponent(self._driver, LocatorsAddAddressComponent.REGION_SELECTOR)
        self.default_address = InputFieldComponent(self._driver,
                                                   LocatorsAddAddressComponent.DEFAULT_ADDRESS_RADIO_CONTAINER)
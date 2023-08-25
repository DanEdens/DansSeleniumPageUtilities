import os
import time

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.support.wait import WebDriverWait


#import testKitUtils
import logging as logger
#logging = testKitUtils.makeLogger(__name__)
logging = logger.getlogger(__name__)


class PageUtilities:
    def __init__(self, driver):
        """
            Initializes the PageUtilities class with the specified web driver
            :param driver: The web driver to use
        """
        self.timeout = 5
        self.driver = driver
        self._use_coordinates = False
        self._take_screenshot_before_click = False
        self._screenshot_count = {}

    @property
    def use_coordinates(self):
        """
            Property to get the use_coordinates value
            :return: The value of use_coordinates
        """
        return self._use_coordinates

    @use_coordinates.setter
    def use_coordinates(self, value):
        """
            Property to set the use_coordinates value
            :param value: The value to set use_coordinates to
        """
        self._use_coordinates = value

    @property
    def take_screenshot_before_click(self):
        """
            Property to get the take_screenshot_before_click value
            :return: The value of take_screenshot_before_click
        """
        return self._take_screenshot_before_click

    @take_screenshot_before_click.setter
    def take_screenshot_before_click(self, value):
        """
            Property to set the take_screenshot_before_click value
            :param value: The value to set take_screenshot_before_click to
        """
        self._take_screenshot_before_click = value

    def take_screenshot(self):
        """
            Takes a screenshot of the current page and names the file based on the current URL
        """
        current_url = self.driver.current_url
        if current_url not in self._screenshot_count:
            self._screenshot_count[current_url] = 1
        else:
            self._screenshot_count[current_url] += 1

        filename = f"{current_url.replace('/', '_')}_{self._screenshot_count[current_url]}.png"
        filepath = os.path.join('screenshots', filename)

        self.driver.save_screenshot(filepath)

    def click_element(self, element) -> WebElement:
        """
            Clicks on the specified element on the webpage. If use_coordinates is set to True, it will use
            click_element_coordinates instead

            :param element: The element to click on
            :return: The WebElement that was clicked
        """
        if self._use_coordinates:
            return self.click_element_coordinates(element)
        else:
            try:
                click_elem = WebDriverWait(self.driver, self.timeout).until(
                    expect.element_to_be_clickable(element))
                logger.debug(f"Clicked: {element}")
            except TimeoutException:
                print(f"\ntimed out looking for {element}, will click anyway")
            click_elem.click()
            return click_elem

    def click_element_coordinates(self, element) -> WebElement:
        """
            Clicks on the specified element on the webpage by clicking on
            its center coordinate

            :param element: The element to click on
            :return: The WebElement that was clicked
        """
        coord_elem = None
        try:
            coord_elem = WebDriverWait(self.driver, self.timeout).until(
                expect.element_to_be_clickable(element))
        except TimeoutException:
            logger.warning(
                f"\ntimed out looking for {element}, will click anyway")

        # Get the center coordinate of the element
        element_x = coord_elem.location['x'] + coord_elem.size['width'] / 2
        element_y = coord_elem.location['y'] + coord_elem.size['height'] / 2

        # Use the ActionChains class to perform the click
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(coord_elem, element_x, element_y)
        action.click()
        action.perform()

        return coord_elem

    def set_attribute_value(self, element, keys: str) -> WebElement:
        """
        Sends the specified keys to the specified element on the webpage

        :param element: The element to send keys to
        :param keys: The keys to send to the element
        """
        _elem = WebDriverWait(self.driver, self.timeout).until(
            expect.element_to_be_clickable(element))
        _elem.clear()
        _elem.send_keys(keys)
        return _elem

    def send_keystrokes_to_element(self, element, keys: str) -> WebElement:
        """
        Sends the specified keys to the specified element on the webpage using key press and release actions

        :usage: set_attribute_value(element, "Hello World!\n")
        :param element: The element to send keys to
        :param keys: The keys to send to the element
        """
        _elem = WebDriverWait(self.driver, self.timeout).until(
            expect.element_to_be_clickable(element))
        _elem.clear()

        action = ActionChains(self.driver)
        for key in keys:
            action.key_down(key).key_up(key)
        action.perform()

        return _elem

    def get_attribute_value(self, element, attribute='value'):
        """
        Gets the value of the specified attribute of the specified element on the webpage.

        :param element: The element to get the attribute value from.
        :param attribute: The attribute to get the value of.
        :return: The value of the specified attribute of the specified element.
        """
        _elem = WebDriverWait(self.driver, self.timeout).until(
            expect.element_to_be_clickable(element))
        return _elem.get_attribute(attribute)

    def element_text(self, element):
        """
            Returns the text of the specified element on the webpage

            :param element: The element to retrieve the text from
        """
        _elem = WebDriverWait(self.driver, self.timeout).until(
            expect.element_to_be_clickable(element))
        return _elem.text

    def element_is_displayed(self, element, timeout=10) -> bool:
        """
            Checks if the specified element is displayed on the webpage

            :param element: The element to check
            :param timeout: The time to wait for element to be displayed
        """
        return WebDriverWait(self.driver, timeout).until(
            expect.visibility_of_element_located(element)).is_displayed()

    def await_clickable(self, element) -> WebElement:
        """
            Returns the text of the specified element on the webpage

            :param element: The element to retrieve the text from
        """
        return WebDriverWait(self.driver, self.timeout).until(
            expect.element_to_be_clickable(element))

    def handle_alert_window(browser) -> str:
        """
        Switches to the alert window and verifies its text.
        """
        ale = browser.driver.switch_to.alert
        result_text = ale.text
        browser.driver.switch_to.alert.accept()
        return result_text

    def check_home(self, browser) -> bool:
        result = browser.driver.current_url.lower()
        if "home" in result:
            return True
        else:
            time.sleep(1)
            result = browser.driver.current_url.lower()
            if "home" in result:
                return True
            else:
                return False

    def scroll_page_bottom(self, browser):
        return browser.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

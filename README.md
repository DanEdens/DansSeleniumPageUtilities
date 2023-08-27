PageUtilities Class for Web Automation
The PageUtilities class is designed to provide various utility functions for web automation tasks. This class is specifically tailored for interaction with web pages using the Selenium library. It offers methods to handle interactions with web elements, perform actions like clicking, sending keystrokes, and more.

Getting Started
To use the PageUtilities class, you need to have the Selenium library installed. You can install it using the following command:

## bash

::
  pip install selenium

Make sure you have a compatible web driver for your browser installed as well. The class requires a web driver instance to operate.

### Usage
You can use the PageUtilities class by creating an instance and passing the web driver instance to its constructor. Here's an example of how to use the class to interact with web elements:

### python

from selenium import webdriver
from page_utilities import PageUtilities  # Import the PageUtilities class

# Create a web driver instance
driver = webdriver.Chrome()  # Use the appropriate driver for your browser

# Initialize PageUtilities with the web driver
page_utils = PageUtilities(driver)

# Example usage: Clicking an element
element_to_click = driver.find_element_by_id("element_id")
page_utils.click_element(element_to_click)

# Example usage: Sending keys to an element
input_element = driver.find_element_by_name("input_name")
page_utils.set_attribute_value(input_element, "Hello, PageUtilities!")

# Don't forget to close the web driver when done
driver.quit()
Save to grepper
Features
Clicking Elements
The click_element method allows you to click on a specified element. It supports both regular clicking and clicking based on element coordinates.

Sending Keystrokes
The send_keystrokes_to_element method enables you to send keystrokes to a specific element. This is useful for interacting with input fields or triggering certain actions on the page.

Getting and Setting Attribute Values
The get_attribute_value and set_attribute_value methods provide functionality to get and set attribute values of web elements.

Checking Element Display
The element_is_displayed method allows you to check if a specific element is displayed on the page within a specified timeout.

Handling Alerts
The handle_alert_window method can be used to switch to an alert window, retrieve its text, and accept the alert.

Checking Current Page
The check_home method helps you determine if the current page is the "home" page by examining the URL.

Scrolling the Page
The scroll_page_bottom method lets you scroll the page to the bottom.

Customization
The PageUtilities class provides options for customization, such as enabling click based on element coordinates and taking screenshots before clicks. These settings can be configured using the provided properties.

For more details on each method's parameters and usage, refer to the docstrings within the class implementation.

Compatibility
The provided code has been designed to work with Selenium and is compatible with various web drivers and browsers. Make sure to use the appropriate web driver for your chosen browser.

Contributions
Contributions and improvements to the PageUtilities class are welcome. If you find any issues or have suggestions, feel free to open an issue or submit a pull request on GitHub.

Happy web automation!

Please note that the above README is a general guide to using the PageUtilities class. You might need to adjust and expand the content based on your project's specific requirements and the audience you intend to share it with.

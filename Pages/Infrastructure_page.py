import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

from webdriver_manager.core import driver

from Pages.Login_page import LoginPage


class InfraPage:
    def __init__(self, driver):
        self.driver = driver
        self.my_infrastructure_button = (By.ID, "buttonMyInfrastructure")
        self.add_system_button = (By.XPATH, "//a[text()='Add System/Network Device']")
        self.display_name_field = (By.NAME, "display_name")
        self.description_field = (By.NAME, "description")
        self.hostname_field = (By.NAME, "value_[hostname]")
        self.save_button = (By.XPATH, "//input[@value='Save']")
        self.system_added_locator = (By.XPATH, "//*[contains(text(), 'nagesh Localhost (Localhost)')]")
        self.login_page = LoginPage(driver)

    def navigate_to_my_infrastructure(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.my_infrastructure_button)).click()
        logging.info("Navigated to My Infrastructure")

    def click_add_system(self):
        add_system_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.add_system_button))
        add_system_button.click()
        logging.info("Clicked Add System button")

    def switch_to_new_window(self, original_window):
        WebDriverWait(self.driver, 10).until(EC.number_of_windows_to_be(2))
        logging.info("New window detected")
        for window in self.driver.window_handles:
            if window != original_window:
                self.driver.switch_to.window(window)
                break

    def fill_system_details(self, display_name="nagesh Localhost", description="description", hostname="Localhost"):
        display_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.display_name_field))
        display_name_field.clear()
        display_name_field.send_keys(display_name)

        description_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.description_field))
        description_field.send_keys(description)

        hostname_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.hostname_field))
        hostname_field.clear()
        hostname_field.send_keys(hostname)
        logging.info(f"Filled system details: {display_name}, {description}, {hostname}")

    def click_save(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.save_button)).click()
        logging.info("Clicked Save button")

    def switch_to_original_window(self, original_window):
        self.driver.switch_to.window(original_window)
        self.driver.refresh()
        logging.info("Switched back to original window and refreshed")

    from selenium.common.exceptions import TimeoutException

    def verify_system_added(self, display_name="nagesh Localhost (Localhost)"):
        try:

            system_added = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{display_name}')]"))
            )
            logging.info(f"Local Network Device '{display_name}' found in the list")
            return True
        except TimeoutException:
            logging.error(f"Local Network Device '{display_name}' not found within the given time.")
            return False

    def login(self, username, password):

        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(2)
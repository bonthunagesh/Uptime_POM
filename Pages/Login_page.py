import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Initialize WebDriverWait with 10-second timeout

    # Locators for username, password, and login button
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    login_button = (By.ID, "loginButton")

    def enter_username(self, username):
        # Wait for the username input field to be visible and interactable
        username_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
        username_field.send_keys(username)

    def enter_password(self, password):
        # Wait for the password input field to be visible and interactable
        password_field = self.wait.until(EC.visibility_of_element_located(self.password_input))
        password_field.send_keys(password)

    def click_login(self):
        # Wait for the login button to be clickable
        login_button = self.wait.until(EC.element_to_be_clickable(self.login_button))
        login_button.click()

    def login(self, username, password):
        # Combined method to perform the full login action with waits
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(2)
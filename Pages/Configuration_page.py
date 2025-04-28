# pages/Configuration_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ConfigurationPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://localhost:9999/index.php?loggedout"
        self.username_field = (By.ID, "username")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "loginButton")
        # Configuration page locators
        self.infra_tab = (By.XPATH, "//button[@id='buttonConfig-button']")
        self.license_info_link = (By.XPATH, "//a[normalize-space()='License Info']")
        self.license_message = (By.XPATH, "//td[contains(., 'HEADS UP: Your Uptime license will expire in')]")

    def open_login_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        ).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()

    def click_infra_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.infra_tab)
        ).click()

    def click_license_info(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.license_info_link)
        ).click()

    def get_license_message(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.license_message)
        )
        return element.text.strip()

    def is_valid_license(self):
        message = self.get_license_message()
        return "heads up" in message.lower()
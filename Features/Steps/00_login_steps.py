import logging
import time

from Pages.Login_page import LoginPage
from Utilities.config import USERNAME, PASSWORD, BASE_URL
from selenium import webdriver

from behave import *


log_file_path = r'C:\Users\BonthuNageshRao\PycharmProjects\Uptime_POM_Framework\Logs\Execution.log'

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'  # Customize log format
)



@given('the user is on the Login Page')
def step_impl(context):
    print("Initializing driver in step_impl...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(BASE_URL)
    time.sleep(5)
    context.login_page = LoginPage(context.driver)
    logging.info("User is on the Login Page")

@when('the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(USERNAME, PASSWORD)
    logging.info("User Enetred username and password")

@then('the user should be able to log in to the application')
def step_impl(context):

    expected_title = "My Portal"
    actual_title = context.driver.title
    assert expected_title in actual_title, f"Expected '{expected_title}' in title, but got: '{actual_title}'"
    print(f"Login successful, page title: {actual_title}")

    logging.info("Logged int o the application and itle is also matched")

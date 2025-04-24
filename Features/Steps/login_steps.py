import time

from Pages.Login_page import LoginPage
from Utilities.config import USERNAME, PASSWORD, BASE_URL
from selenium import webdriver

from behave import *

@given('the user is on the Login Page')
def step_impl(context):
    print("Initializing driver in step_impl...")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get(BASE_URL)
    time.sleep(5)
    context.login_page = LoginPage(context.driver)

@when('the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    # Use the login method from LoginPage to enter credentials and click login
    context.login_page.login(USERNAME, PASSWORD)

@then('the user should be able to log in to the application')
def step_impl(context):

    expected_title = "My Portal"
    actual_title = context.driver.title
    assert expected_title in actual_title, f"Expected '{expected_title}' in title, but got: '{actual_title}'"
    print(f"Login successful, page title: {actual_title}")

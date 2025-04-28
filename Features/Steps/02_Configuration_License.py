# steps/02_Configuration_License.py
import logging
import time

import allure
from selenium import webdriver
from behave import *
from Pages.Configuration_page import ConfigurationPage

from Pages.Login_page import LoginPage

@allure.step("user is logged in")
@given(u'user is logged in')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.config_page = ConfigurationPage(context.driver)
    context.config_page.open_login_page()
    time.sleep(2)
    context.config_page.login("nagesh", "Alpha122@")
    time.sleep(2)

@allure.step("user click on Infra Tab")
@when(u'user click on Infra Tab')
def step_impl(context):
    context.config_page.click_infra_tab()

@allure.step("User click on License Info")
@when(u'User click on License Info')
def step_impl(context):
    context.config_page.click_license_info()


@allure.step("User should be validate for Valid License")
@then(u'User should be validate for Valid License')
def step_impl(context):
    try:
        print("Starting license validation step")

        if context.config_page.is_valid_license():
            print("Validation passed: 'HEADS UP' found in the license message")
        else:
            message = context.config_page.get_license_message()
            print(f"Validation failed: 'HEADS UP' not found in '{message}'")

    finally:
        context.driver.quit()
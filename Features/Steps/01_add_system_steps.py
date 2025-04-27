from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Infrastructure_page import InfraPage
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

@given('the user is on the Uptime Infrastructure Monitor dashboard')
def step_user_on_dashboard(context):
    # Assuming login is handled elsewhere, ensure driver is initialized
    assert context.driver is not None, "WebDriver not initialized"
    logging.info("User is on the Uptime Infrastructure Monitor dashboard")

@when('the user navigates to My Infrastructure')
def step_navigate_to_my_infrastructure(context):
    context.infra_page = InfraPage(context.driver)
    context.infra_page.navigate_to_my_infrastructure()

@when('the user clicks Add System button')
def step_click_add_system(context):
    context.infra_page.click_add_system()

@when('the user switches to the new window')
def step_switch_to_new_window(context):
    context.original_window = context.driver.current_window_handle
    context.infra_page.switch_to_new_window(context.original_window)

@when('the user fills in the system details with display name "{display_name}", description "{description}", and hostname "{hostname}"')
def step_fill_system_details(context, display_name, description, hostname):
    context.infra_page.fill_system_details(display_name, description, hostname)

@when('the user clicks Save')
def step_click_save(context):
    context.infra_page.click_save()

@when('the user switches back to the original window')
def step_switch_to_original_window(context):
    context.infra_page.switch_to_original_window(context.original_window)

@then('the system "{display_name}" should be added successfully')
def step_verify_system_added(context, display_name):
    result = context.infra_page.verify_system_added(display_name)
    assert result, f"System '{display_name}' was not found in the list"
    logging.info(f"Verified system '{display_name}' was added successfully")
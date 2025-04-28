from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from Pages.login_page import LoginPage
from Utilities.config import BASE_URL, USERNAME, PASSWORD

print("Loading environment.py...")

def before_all(context):
    print("Inside before_all: Initializing browser...")
    try:
        context.driver = webdriver.Chrome(ChromeDriverManager().install())
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)
        print(f"Browser initialized")
    except Exception as e:
        print(f"Error in before_all: {e}")
        raise

def before_scenario(context, scenario):
    print(f"Before scenario: {scenario.name}")
    try:
        context.login_page = LoginPage(context.driver)
        context.driver.get(BASE_URL)
        context.login_page.login(USERNAME, PASSWORD)
        print("Login completed")
    except Exception as e:
        print(f"Error in before_scenario: {e}")
        raise

def after_scenario(context, scenario):
    print(f"After scenario: {scenario.name}")

def after_all(context):
    print("Inside after_all: Closing browser...")
    if hasattr(context, 'driver'):
        context.driver.quit()
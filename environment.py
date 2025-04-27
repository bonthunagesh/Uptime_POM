from selenium import webdriver
from Pages.Login_page import LoginPage
from Utilities.config import BASE_URL

print("Loading environment.py...")  # Debug to confirm file is loaded

def before_all(context):
    print("Inside before_all: Initializing browser...")
    try:
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)  # Added for stability, optional
        context.driver.get(BASE_URL)
        print(f"Browser initialized and navigated to {BASE_URL}")
    except Exception as e:
        print(f"Error in before_all: {e}")
        raise

def after_all(context):
    print("Inside after_all: Closing browser...")
    try:
        if hasattr(context, 'driver'):
            context.driver.quit()
            print("Browser closed")
    except Exception as e:
        print(f"Error in after_all: {e}")
        raise
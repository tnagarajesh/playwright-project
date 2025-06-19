from page_objects.admin_page import admin_page
from page_objects.login_page import login
from utils.utils import clean_environment_variables, read_data
import pytest

# This file contains a test case for verifying the admin dashboard functionality using Playwright and pytest.
# It reads user credentials from a data source and performs navigation through the admin dashboard.
@pytest.mark.smoketest
def test_verify_admin_dashboard(initialize_browser, user_type, env_type):
    
    # Initialize the browser
    # This function is defined in conftest.py and sets up the browser
    page = initialize_browser

    # Read user data based on the user type and environment type
    # This function reads the user credentials from a file or environment variables
    #username, password, url = read_user_data(user_type, env_type)

    username, password, url = read_data(user_type, env_type)
    
    # Check if the user data was loaded successfully
    login_instance = login(page, url, username, password)

    # Perform the login operation
    # This will navigate to the login page, fill in the credentials, and submit the form
    page=login_instance.test_login()

    # Check if the login was successful by verifying the URL
    print(f"Logged in as {username} on {page.url}")

    # Assuming the user is already logged in, we can directly access the admin dashboard
    admin_page_instance = admin_page(page)

    menu_items_list = clean_environment_variables("menu_item_role_link_list") + clean_environment_variables("menu_role_link_list")

    # Loop and navigate
    for menu_item in menu_items_list:
        print(f"Navigating to: {menu_item} in admin dashboard")
        # Navigate to each menu item in the admin dashboard
        admin_page_instance.admin_navigate(menu_item)

 
 
    

    
  
    
    
    
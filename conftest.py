import pandas as pd
import pytest
from playwright.sync_api import Playwright
import os
from page_objects.admin_page import admin_page
from page_objects.login_page import login
from utils.utils import clean_environment_variables, read_data

# This file is used to configure pytest fixtures and command line options for the test suite.
def pytest_addoption(parser):
    parser.addoption("--user_type", action="store", default="admin", help="Specify user type (e.g., admin, guest)")
    parser.addoption("--env_type", action="store", default="QA", help="Specify environment type (e.g., staging, prod)")
    parser.addoption("--browser_type", action="store", default="chromium", help="Specify browser type (e.g., chromium, firefox, webkit)")

@pytest.fixture
def user_type(request):
    return request.config.getoption("--user_type")

@pytest.fixture
def env_type(request):
    return request.config.getoption("--env_type")

@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser_type")

@pytest.fixture(scope="session")
def initialize_browser(playwright: Playwright,request):
    # Initialize the browser with the specified type
    browser_name = request.config.getoption("--browser_type")
    if browser_name == "chromium":
        browser = playwright.chromium.launch(headless=False)    
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False) 
    elif browser_name == "webkit":
        browser = playwright.webkit.launch(headless=False)
  
    page = browser.new_page()  # Create a new page
    yield page
    browser.close()

@pytest.fixture
def navigate_admin_dashboard(initialize_browser, request):

    user_type, env_type, menu_item = request.param
    
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

    #return admin_page_instance
    return_page=admin_page_instance.admin_navigate(menu_item)

    return return_page


        



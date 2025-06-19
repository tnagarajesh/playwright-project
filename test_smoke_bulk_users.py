from page_objects.login_page import login
from utils.utils import read_data
import pytest

# This file contains a test case for bulk user login using Playwright and pytest.
# It reads user credentials from a data source and performs login for multiple user types.
@pytest.mark.smoketest
@pytest.mark.parametrize("user_type, env_type", [("admin", "QA"), ("Subscriber", "QA"), ("Contributor", "QA")])
def test_bulk_user_login(initialize_browser, user_type, env_type):
    
    page = initialize_browser

    #result = read_user_data(user_type, env_type)
    result = read_data(user_type, env_type)
    if result is not None:
        username, password, url = result
    else:
        raise ValueError("Failed to load user data.")

    login_instance = login(page, url, username, password)
    page=login_instance.test_login()
    print(f"Logged in as {username} on {page.url}")


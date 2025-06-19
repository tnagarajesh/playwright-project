from playwright.sync_api import expect
import pytest,os
from utils.utils import load_test_data

@pytest.mark.parametrize(
    "navigate_admin_dashboard",
    load_test_data(os.environ["file_path"], "test_add_post"),  # or .xlsx
    indirect=True
)
def test_add_post(initialize_browser, navigate_admin_dashboard):
    return_page_name = navigate_admin_dashboard
    return_page_name.locator("#wpbody-content").get_by_role("link", name="Add Post").click()
    expect(return_page_name.locator("#wpbody-content")).to_contain_text("Add Post")
    return_page_name.screenshot(path="screenshots/test_tc2_add_post.png")



  
    
  
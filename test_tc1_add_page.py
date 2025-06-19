from playwright.sync_api import expect
import pytest,os
from utils.utils import load_test_data

@pytest.mark.parametrize(
    "navigate_admin_dashboard",
    load_test_data(os.environ["file_path"], "test_add_page"),  # or .xlsx
    indirect=True
)
def test_add_page(initialize_browser, navigate_admin_dashboard):
    return_page_name = navigate_admin_dashboard
    return_page_name.locator("#wpbody-content").get_by_role("link", name="Add Page").click()
    expect(return_page_name.locator("#wpbody-content")).to_contain_text("Add Page")
    return_page_name.screenshot(path="testcases/screenshots/test_tc1_add_page.png")



  
    
  
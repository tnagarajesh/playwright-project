from playwright.sync_api import expect
import os

# This file defines an admin page object for testing admin functionalities using Playwright.
# It includes methods to navigate to different admin menu items based on environment variables.
class admin_page:

    def __init__(self, page):
        self.page = page

    def admin_navigate(self, menu_item):
        """
        Navigate to a specific admin menu item.
        :param menu_item: The menu item to navigate to (e.g., "Dashboard", "Posts", "Media").
        """
           
        if menu_item in os.environ["menu_item_role_link_list"]:
            self.page.get_by_role("link", name=menu_item,exact=True).click()
            expect(self.page.get_by_role("link", name=menu_item, exact=True)).to_be_visible()
            print(f"Navigated to {menu_item} successfully.")
            return self.page
        
        if menu_item in os.environ["menu_role_link_list"]:
            self.page.locator(f"#menu-{menu_item.lower()}").get_by_role("link", name=menu_item, exact=True).click()
            expect(self.page.locator(f"#menu-{menu_item.lower()}").get_by_role("link", name=menu_item, exact=True)).to_be_visible()
            print(f"Navigated to {menu_item} successfully.")
            return self.page

  
            

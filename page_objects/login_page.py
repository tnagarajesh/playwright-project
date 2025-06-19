from playwright.sync_api import expect

# This file defines a login page object for testing login functionality using Playwright.
# It includes methods to navigate to the login page, fill in credentials, and handle cookie prompts
class login:
   
    def __init__(self, page, url, username, password):
        self.page = page
        self.url = url
        self.username = username
        self.password = password
  
    def test_login(self):
        self.page.goto(self.url)
        self.page.get_by_label("Username or Email Address").fill(self.username)
        self.page.locator("input[type='password']").fill(self.password)
        self.page.get_by_role(role="button", name="Log In").click() 
        if self.page.get_by_text("enable cookies").is_visible():
            self.page.get_by_role(role="link", name="Go to televisionshop.in").click()
            self.page.get_by_text("televisionshop.in").click() 
        return self.page
        
     
        

        
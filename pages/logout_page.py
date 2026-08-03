class LogoutPage:

    def __init__(self, page):
        self.page = page

    def click_menu(self):
        self.page.locator("#react-burger-menu-btn").click()

    def click_logout(self):
        self.page.locator("#logout_sidebar_link").click()
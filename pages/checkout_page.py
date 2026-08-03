class CheckoutPage:

    def __init__(self, page):
        self.page = page

    def enter_first_name(self, first_name):
        self.page.locator("#first-name").fill(first_name)

    def enter_last_name(self, last_name):
        self.page.locator("#last-name").fill(last_name)

    def enter_postal_code(self, postal_code):
        self.page.locator("#postal-code").fill(postal_code)

    def click_continue(self):
        self.page.locator("#continue").click()
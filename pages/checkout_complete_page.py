class CheckoutCompletePage:

    def __init__(self, page):
        self.page = page

    def click_finish(self):
        self.page.locator("#finish").click()

    def get_success_message(self):
        return self.page.locator(".complete-header").text_content()
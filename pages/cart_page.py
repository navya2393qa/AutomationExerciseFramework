class CartPage:

    def __init__(self, page):
        self.page = page

    def open_cart(self):
        self.page.locator(".shopping_cart_link").click()

    def get_product_name(self):
        return self.page.locator(".inventory_item_name").text_content()

    def click_checkout(self):
        self.page.locator("#checkout").click()

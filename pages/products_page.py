class ProductsPage:

    def __init__(self, page):
        self.page = page

    def add_product_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

    def get_cart_count(self):
        return self.page.locator(".shopping_cart_badge").text_content()
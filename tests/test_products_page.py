from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_products_page(page):
    login = LoginPage(page)
    products = ProductsPage(page)

    page.goto("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products.add_product_to_cart()

    assert products.get_cart_count() == "1"

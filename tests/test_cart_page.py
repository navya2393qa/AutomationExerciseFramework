from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_cart_page(page):
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)

    page.goto("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products.add_product_to_cart()

    cart.open_cart()

    assert cart.get_product_name() == "Sauce Labs Backpack"

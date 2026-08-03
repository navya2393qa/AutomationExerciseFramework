from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_page(page):

    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    checkout = CheckoutPage(page)

    page.goto("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    products.add_product_to_cart()

    cart.open_cart()
    cart.click_checkout()

    checkout.enter_first_name("Navya")
    checkout.enter_last_name("K")
    checkout.enter_postal_code("500001")
    checkout.click_continue()

    assert "checkout-step-two" in page.url

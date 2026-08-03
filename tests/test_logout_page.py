from pages.login_page import LoginPage
from pages.logout_page import LogoutPage


def test_logout_page(page):

    login = LoginPage(page)
    logout = LogoutPage(page)

    page.goto("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    logout.click_menu()
    logout.click_logout()

    assert page.url == "https://www.saucedemo.com/"
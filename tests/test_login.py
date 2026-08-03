from pages.login_page import LoginPage


def test_login_page(page):
    login = LoginPage(page)

    page.goto("https://www.saucedemo.com/")

    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    assert "inventory" in page.url

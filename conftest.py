import pytest
from playwright.sync_api import sync_playwright

from config.config import BASE_URL, HEADLESS


@pytest.fixture()
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=HEADLESS,
            slow_mo=1000
        )

        page = browser.new_page()

        page.goto(BASE_URL)

        yield page

        browser.close()
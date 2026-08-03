from playwright.sync_api import sync_playwright
import pytest
from utils.config import HEADLESS


@pytest.fixture()
def page():

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            slow_mo=1000
        )

        page = browser.new_page()
        yield page

        browser.close()
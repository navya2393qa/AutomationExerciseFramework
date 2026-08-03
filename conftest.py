import os
import pytest
from playwright.sync_api import sync_playwright
from config.config import HEADLESS

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def page(request):

    with sync_playwright() as p:
        browser = p.chromium.launch(
            headless=HEADLESS,
            slow_mo=1000
        )

        page = browser.new_page()

        yield page

        # Capture screenshot if test fails
        if request.node.rep_call.failed:
            os.makedirs("screenshots", exist_ok=True)

            page.screenshot(
                path=f"screenshots/{request.node.name}.png"
            )

        browser.close()
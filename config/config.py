import os

BASE_URL = "https://www.saucedemo.com/"

BROWSER = "chromium"

HEADLESS = os.getenv("HEADLESS", "False") == "True"

TIMEOUT = 10000

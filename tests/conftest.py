import pytest
from playwright.sync_api import Page, Playwright, sync_playwright

# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#         print("Before")
#         yield browser.new_page()
#         print("After")


# @pytest.fixture
# def chromium_page(playwright: Playwright) -> Page:
#     browser = playwright.chromium.launch(headless=False)
#     yield browser.new_page()
#     browser.close()


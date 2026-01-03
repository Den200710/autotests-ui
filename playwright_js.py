from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
              wait_until='networkidle')

    text_button = 'Логин'
    page.evaluate(
        f"""
        const button = document.getElementById('login-page-login-button')
        button.textContent = '{text_button}'
        """
    )

    page.wait_for_timeout(2000)
from playwright.sync_api import sync_playwright
from playwright_stealth import Stealth


def get_price(article):

    url = f"https://www.wildberries.ru/catalog/{article}/detail.aspx"

    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled",
                "--no-sandbox"
            ]
        )

        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36",
            viewport={"width": 1400, "height": 900}
        )

        stealth = Stealth()
        stealth.apply_stealth_sync(page)

        page.goto(url, wait_until="networkidle", timeout=60000)

        print("TITLE:", page.title())
        print(page.content()[:3000])

        browser.close()

from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync


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
            viewport={"width": 1400, "height": 900},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        )

        stealth_sync(page)

        page.goto(url, wait_until="domcontentloaded", timeout=60000)

        page.wait_for_timeout(5000)

        print(page.title())

        print(page.content()[:2000])

        browser.close()

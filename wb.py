from playwright.sync_api import sync_playwright


def get_price(article):

    url = f"https://www.wildberries.ru/catalog/{article}/detail.aspx"

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page(
            user_agent="Mozilla/5.0"
        )

        page.goto(url, wait_until="networkidle")

        text = page.content()

        print("Страница загружена")

        if "price" in text:
            print("Цена найдена в коде")

        print(text[:1000])

        browser.close()

import requests

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

def get_price(article):
    url = f"https://card.wb.ru/cards/v2/detail?appType=1&curr=rub&dest=-1257786&nm={article}"

    r = requests.get(url, headers=HEADERS, timeout=20)
    r.raise_for_status()

    data = r.json()

    products = data.get("data", {}).get("products", [])

    if not products:
        return None

    product = products[0]

    sizes = product.get("sizes", [])

    if not sizes:
        return None

    price = sizes[0]["price"]["product"] / 100

    return int(price)

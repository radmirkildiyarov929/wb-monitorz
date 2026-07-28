import requests


def get_price(article):

    url = f"https://card.wb.ru/cards/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={article}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://www.wildberries.ru",
        "Referer": "https://www.wildberries.ru/"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(article, "Ошибка:", response.status_code)
        return None

    try:
        product = response.json()["data"]["products"][0]

        price = product["sizes"][0]["price"]["product"] / 100

        return price

    except Exception as e:
        print(article, "Ошибка обработки:", e)
        return None

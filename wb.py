import requests


def get_price(article):

    url = f"https://card.wb.ru/cards/detail?nm={article}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(article, "Ошибка:", response.status_code)
        return None

    data = response.json()

    try:
        product = data["data"]["products"][0]

        price = product["salePriceU"] / 100

        return price

    except Exception as e:
        print(article, "Ошибка обработки:", e)
        return None

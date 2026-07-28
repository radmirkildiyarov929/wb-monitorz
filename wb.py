import requests


def get_price(article):

    url = f"https://www.wildberries.ru/catalog/{article}/detail.aspx"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "ru-RU,ru;q=0.9"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(article, "Ошибка:", response.status_code)
        return None

    text = response.text

    marker = '"salePrice":'

    if marker in text:
        price = text.split(marker)[1].split(",")[0]
        return int(price) / 100

    print(article, "цена не найдена")
    return None

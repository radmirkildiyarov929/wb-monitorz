import requests


def get_price(article):

    url = f"https://basket-02.wbbasket.ru/vol{article//100000}/part{article//1000}/{article}/info/ru/card.json"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print(article, response.status_code)

    if response.status_code != 200:
        return None

    data = response.json()

    for key, value in data.items():
        if "price" in key.lower():
            print(key, value)

    return None

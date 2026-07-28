import requests


def get_price(article):

    url = f"https://basket-02.wbbasket.ru/vol{article//100000}/part{article//1000}/{article}/info/ru/card.json"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(url, headers=headers)

    print(article, r.status_code)

    data = r.json()

    print(data.keys())

    return None

import requests
import json


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

    print(json.dumps(data, indent=2)[:1000])

    return None

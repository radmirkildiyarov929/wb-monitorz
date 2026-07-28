import requests
import json


def get_price(article):

    url = f"https://basket-02.wbbasket.ru/vol{article//100000}/part{article//1000}/{article}/info/ru/card.json"

    response = requests.get(url)

    print("STATUS:", response.status_code)

    data = response.json()

    print(json.dumps(data, indent=2, ensure_ascii=False))

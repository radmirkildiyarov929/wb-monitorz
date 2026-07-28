import requests
import json


def get_price(article):

    vol = article // 100000
    part = article // 1000

    urls = [
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/card.json",
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/price.json",
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/product.json"
    ]

    for url in urls:

        r = requests.get(url)

        print(url)
        print("STATUS:", r.status_code)

        if r.status_code == 200:
            try:
                data = r.json()
                print(data.keys())
            except:
                pass

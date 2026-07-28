import requests


def get_price(article):

    vol = article // 100000
    part = article // 1000

    url = f"https://basket-{vol:02d}.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/card.json"

    response = requests.get(url)

    print(article, response.status_code)

    if response.status_code != 200:
        return None

    data = response.json()

    print(data.keys())

    return None

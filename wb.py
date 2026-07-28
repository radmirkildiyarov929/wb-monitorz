import requests


def get_price(article):

    url = f"https://basket-02.wbbasket.ru/vol{article//100000}/part{article//1000}/{article}/info/ru/price-history.json"

    response = requests.get(url)

    print(article, response.status_code)

    if response.status_code != 200:
        return None

    data = response.json()

    print(data)

    return None

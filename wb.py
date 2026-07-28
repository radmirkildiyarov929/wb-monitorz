import requests


def get_price(article):

    vol = article // 100000
    part = article // 1000

    urls = [
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/options.json",
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/details.json",
        f"https://basket-02.wbbasket.ru/vol{vol}/part{part}/{article}/info/ru/metadata.json"
    ]

    for url in urls:

        r = requests.get(url)

        print(url)
        print("STATUS:", r.status_code)

        if r.status_code == 200:
            try:
                print(r.json().keys())
            except:
                print(r.text[:500])

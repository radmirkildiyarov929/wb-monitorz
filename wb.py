import requests
import re


def get_price(article):

    url = f"https://www.wildberries.ru/catalog/{article}/detail.aspx"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)

    print("STATUS:", response.status_code)

    text = response.text

    for word in ["price", "salePrice", "finalPrice", "priceU"]:
        if word in text:
            print("Найдено:", word)

    numbers = re.findall(r'\d{3,6}', text)

    print(numbers[:50])

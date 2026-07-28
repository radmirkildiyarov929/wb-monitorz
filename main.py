from wb import get_price
from sheets import save_price

ARTICLES = [
    178660879,
    67119249,
    16237115,
    25929128,
    114868569,
    48896844,
    355637600,
    355629983,
    361862902
]

for article in ARTICLES:
    try:
        price = get_price(article)

        if price is not None:
            save_price(article, price)
            print(f"{article}: {price} ₽")
        else:
            print(f"{article}: цена не найдена")

    except Exception as e:
        print(f"{article}: {e}")

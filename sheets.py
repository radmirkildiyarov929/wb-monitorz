import os
import json
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

credentials = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    credentials,
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("WB Monitor").sheet1


def save_price(article, price):
    from datetime import datetime

    now = datetime.now()

    sheet.append_row([
        now.strftime("%d.%m.%Y"),
        now.strftime("%H:%M"),
        str(article),
        price
    ])

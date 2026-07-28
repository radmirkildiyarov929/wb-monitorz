import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets"
]

credentials = json.loads(os.environ["GOOGLE_CREDENTIALS"])

creds = Credentials.from_service_account_info(
    credentials,
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open_by_key(
    "1TaCX9GEReGMeXEJARbwT8q7-UUD8lFZyPhfpTTB2tPs"
).sheet1


def save_price(article, price):
    now = datetime.now()

    sheet.append_row([
        now.strftime("%d.%m.%Y"),
        now.strftime("%H:%M"),
        article,
        price
    ])

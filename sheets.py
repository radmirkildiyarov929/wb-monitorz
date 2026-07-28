import os
import json
from datetime import datetime

import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

def get_sheet():
    creds_dict = json.loads(os.environ['GOOGLE_CREDENTIALS'])

    creds = Credentials.from_service_account_info(
        creds_dict,
        scopes=SCOPES
    )

    client = gspread.authorize(creds)

    sheet = client.open('WB Monitor').sheet1

    return sheet

def append_price(article, price):
    sheet = get_sheet()

    now = datetime.now()

    sheet.append_row([
        now.strftime('%d.%m.%Y'),
        now.strftime('%H:%M'),
        str(article),
        price
    ])

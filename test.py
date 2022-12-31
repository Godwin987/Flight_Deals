import os
from dotenv import load_dotenv
load_dotenv("api_details.env")

SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
TEQUILLA_API_KEY = os.getenv('TEQUILLA_API_KEY')

print(BEARER_TOKEN)
# from datetime import datetime, timedelta
#
# print(datetime.now().date().strftime("%d/%m/%Y"))
#
# time = datetime.now().date() + timedelta((30*6))
# print(time.strftime("%d/%m/%Y"))

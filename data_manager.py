import requests
import os
import gspread
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv("api_details.env")
SHEET_ENDPOINT = os.getenv('SHEET_ENDPOINT')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')
NUM = 1
SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"
         , "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("Flight Manager API Key.json", SCOPE)
client = gspread.authorize(credentials)

flight_deal = client.open("Flight Deals").worksheet("prices")
flight_deals = client.open("Flight Deals").worksheet("users")


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.flight_deal = flight_deal
        self.flight_deals = flight_deals
        # self.flight_search = flight_search
        # self.sheet_header = {
        #             "Content-Type": "application/json",
        #             "Authorization": f"Bearer {BEARER_TOKEN}"
        #         }

    def get(self):
        self.flight_deal = client.open("Flight Deals").worksheet("prices")
        return flight_deal.get_all_records()
        # response = requests.get(url=SHEET_ENDPOINT, headers=self.sheet_header)
        # return response.json()

    def each_user(self):
        self.flight_deals = client.open("Flight Deals").worksheet("users")
        return flight_deals.get_all_records()

    def post(self, city_code):
        global NUM
        NUM += 1
        sheet_endpoint = f"https://api.sheety.co/72166356ac38b8d96bbcee85de172cba/flightDeals/prices/{NUM}"
        data = {
                "price": {
                    "iataCode": f"{city_code}",
                }
            }
        print(data)
        response = requests.put(url=sheet_endpoint, json=data, headers=self.sheet_header)
        print(response.text)

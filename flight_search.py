import requests
import os
from dotenv import load_dotenv
load_dotenv("api_details.env")
from datetime import datetime, timedelta

LOCATION_ENDPOINT = "https://api.tequila.kiwi.com/locations/query"
SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILLA_API_KEY = os.getenv('TEQUILLA_API_KEY')

# get the date for the next day
tomorrows_date = datetime.now().date().strftime("%d/%m/%Y")

# gets the date for the next 6 months
after_6_months = datetime.now().date() + timedelta((30 * 6))
after_6_months.strftime("%d/%m/%Y")

return_from = datetime.now().date() + timedelta(7)
return_from.strftime("%d/%m/%Y")

return_to = datetime.now().date() + timedelta(28)
return_to.strftime("%d/%m/%Y")


class FlightSearch:
    from data_manager import DataManager
    # This class is responsible for talking to the Flight Search API.

    def __init__(self, data_manager_object: DataManager):
        self.data_manager = data_manager_object
        self.header = {
            "apikey": TEQUILLA_API_KEY,
            "Content-Type": "application/json",
        }

    def get(self, city):
        location_params = {
            "term": f"{city}",
            "location_types": "city",

        }
        response = requests.get(url=LOCATION_ENDPOINT, params=location_params, headers=self.header)
        return response.json()

    def response(self, city):
        if city:
            self.data_manager.post(self.get(city)["locations"][0]["code"])

    def search(self, city, max_stopover=0):
        search_params = {
            "fly_from": "LOS",
            "fly_to": f"{city}",
            "date_from": f"{tomorrows_date}",
            "date_to": f"{after_6_months.strftime('%d/%m/%Y')}",
            "return_from": f"{return_from.strftime('%d/%m/%Y')}",
            "return_to": f"{return_to.strftime('%d/%m/%Y')}",
            "curr": "NGN",
            "max_stopovers": f"{max_stopover}",
            "flight_type": "round"
        }
        response = requests.get(url=SEARCH_ENDPOINT, params=search_params, headers=self.header)
        return response.json()

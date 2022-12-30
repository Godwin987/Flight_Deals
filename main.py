# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager
# from oauth2client.service_account import ServiceAccountCredentials
# import gspread

# SCOPE = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive.file"
#          , "https://www.googleapis.com/auth/drive"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("Flight Manager API Key.json", SCOPE)
# client = gspread.authorize(credentials)
#
# flight_deal = client.open("Flight Deals").worksheet("prices")
# flight_deals = client.open("Flight Deals").worksheet("users")
# pprint(flight_deal.get_all_records())


sheet_api = DataManager()
#
sheet_data = sheet_api.get()
pprint(sheet_data)
user_data = sheet_api.each_user()

flight_search = FlightSearch(sheet_api)

# pprint(flight_search.get()["locations"][0]["code"])
#
"""Price

Departure City Name

Departure Airport IATA Code

Arrival City Name

Arrival Airport IATA Code

Outbound Date

Inbound Date"""
for item in sheet_data:
    city = item["IATA Code"]
    # city = flight_search.response(item["iataCode"])
    try:
        price = flight_search.search(city)["data"][0]["price"]
    except IndexError:
        data = flight_search.search(city, max_stopover=2)["data"][0]
        pprint(data)
        price = flight_search.search(city, max_stopover=2)["data"][0]["price"]
        departure_airport_code = flight_search.search(city, max_stopover=2)["data"][0]["flyFrom"]
        arrival_airport_code = flight_search.search(city, max_stopover=2)["data"][0]["flyTo"]
        city_from = flight_search.search(city, max_stopover=2)["data"][0]["cityFrom"]
        city_to = flight_search.search(city, max_stopover=2)["data"][0]["cityTo"]
        local_arrival = flight_search.search(city, max_stopover=2)["data"][0]["local_arrival"]
        local_departure = flight_search.search(city, max_stopover=2)["data"][0]["local_departure"]
        deep_link = flight_search.search(city, max_stopover=2)["data"][0]["deep_link"]
        cities1 = flight_search.search(city, max_stopover=2)["data"][0]["route"][0]["cityTo"]
        cities2 = flight_search.search(city, max_stopover=2)["data"][0]["route"][1]["cityTo"]
        cities3 = flight_search.search(city, max_stopover=2)["data"][0]["route"][2]["cityFrom"]

        # print(deep_link)

        flight_data = FlightData(
            price=price, airport_code=departure_airport_code,
            city_from=city_from, city_to=city_to,
            arrival_airport_code=arrival_airport_code, inbound_date=local_arrival,
            outbound_date=local_departure, stop_overs=2,
            via_city=f"{cities1}, {cities2}", deep_link=deep_link
        )

        # print(flight_data.deep_link())

        price_1 = item["Lowest Price"]
        if price < price_1:
            notification_manager = NotificationManager(
                price=price, airport_code=departure_airport_code,
                city_from=city_from, city_to=city_to,
                arrival_airport_code=arrival_airport_code, inbound_date=local_arrival, outbound_date=local_departure,
                deep_link=deep_link, stop_overs=2, via_city=f"{cities1}, {cities2}"
            )
            message = notification_manager.stopover_message()
            print(message)
            for user in user_data:
                each_user = user["Email"]
                notification_manager.send_emails(users=each_user)
        # print(f"No direct flights found for {item['city']}, {city}")
    else:
        departure_airport_code = flight_search.search(city)["data"][0]["flyFrom"]
        arrival_airport_code = flight_search.search(city)["data"][0]["flyTo"]
        city_from = flight_search.search(city)["data"][0]["cityFrom"]
        city_to = flight_search.search(city)["data"][0]["cityTo"]
        local_arrival = flight_search.search(city)["data"][0]["local_arrival"]
        local_departure = flight_search.search(city)["data"][0]["local_departure"]
        deep_link = flight_search.search(city)["data"][0]["deep_link"]

        # print(deep_link)

        flight_data = FlightData(
            price=price, airport_code=departure_airport_code,
            city_from=city_from, city_to=city_to,
            arrival_airport_code=arrival_airport_code, inbound_date=local_arrival, outbound_date=local_departure, deep_link=deep_link
        )

        # flight_data.deep_link()
        # flight_data.send()
        price_1 = item["Lowest Price"]
        if price < price_1:
            notification_manager = NotificationManager(
                price=price, airport_code=departure_airport_code,
                city_from=city_from, city_to=city_to,
                arrival_airport_code=arrival_airport_code, inbound_date=local_arrival, outbound_date=local_departure,
                deep_link=deep_link, stop_overs=0, via_city=""
            )
            message = notification_manager.flight_message()
            print(message)
            for user in user_data:
                each_user = user["Email"]
                notification_manager.send_emails(users=each_user)
# cities = ["PAR", "BER", "TYO", "SYD", "IST", "KUL", "NYC", "SFO", "CPT"]
#
# flight_search = FlightSearch(sheet_api)
# for city in cities:
#     price = flight_search.search(city)["data"][0]["price"]
#     departure_airport_code = flight_search.search(city)["data"][0]["flyFrom"]
#     city_from = flight_search.search(city)["data"][0]["cityFrom"]
#     city_to = flight_search.search(city)["data"][0]["cityTo"]
#
#     flight_data = FlightData(price=price, airport_code=departure_airport_code, city_from=city_from, city_to=city_to)
#
#     flight_data.send()

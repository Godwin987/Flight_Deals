class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, airport_code, city_from, city_to, arrival_airport_code,
                 inbound_date, outbound_date, deep_link, stop_overs=0, via_city=""):
        self.price = price
        self.departure_airport_code = airport_code
        self.departure_city = city_from
        self.destination_city = city_to
        self.arrival_airport_code = arrival_airport_code
        self.inbound_date = inbound_date
        self.outbound_date = outbound_date
        self.stopover = stop_overs
        self.via_city = via_city
        self.deep_link = deep_link

    def send(self):
        print(f"{self.destination_city}: £{self.price}")

    def deep_link(self):
        return self.deep_link


from flight_data import FlightData
import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = "pythonlearncode114@gmail.com"
password = "ykiivixaeyphfpam"


class NotificationManager(FlightData):
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, airport_code, city_from, city_to, arrival_airport_code, inbound_date,
                 outbound_date, deep_link, stop_overs, via_city):
        super().__init__(price, airport_code, city_from, city_to, arrival_airport_code, inbound_date,
                         outbound_date, deep_link, stop_overs, via_city)
        self.bot_message = ""

    def flight_message(self):
        self.bot_message = (
            f"Low price alert!\nonly ₦{self.price} to fly ✈✈ from {self.departure_city}-{self.departure_airport_code}"
            f" to {self.destination_city}-{self.arrival_airport_code}, "
            f"from {self.outbound_date.split('T')[0]} to {self.inbound_date.split('T')[0]}\n.")

        bot_token = '5664737899:AAEZX-t3GHLljycZpueIgcjEycNWEgXKTk4'
        bot_chatID = '1999930604'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='\
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.bot_message
        send_link = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='\
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.deep_link
        self.print()
        response = requests.get(send_text)
        response1 = requests.get(send_link)

        return response.json()

    def stopover_message(self):
        self.bot_message = (
            f"Low price alert!\nonly ₦{self.price} to fly ✈✈ from {self.departure_city}-{self.departure_airport_code}"
            f" to {self.destination_city}-{self.arrival_airport_code}, "
            f"from {self.outbound_date.split('T')[0]} to {self.inbound_date.split('T')[0]}. "
            f"Flight has {self.stopover} stop overs,via {self.via_city}\n")

        bot_token = '5664737899:AAEZX-t3GHLljycZpueIgcjEycNWEgXKTk4'
        bot_chatID = '1999930604'
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                    '&parse_mode=Markdown&text=' + self.bot_message
        send_link = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.deep_link

        response = requests.get(send_text)
        response1 = requests.get(send_link)

        return response.json()

    def send_emails(self, users):
        from_adr = my_email
        to_adr = users

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "Low Price Flight Alert!"
        msg['From'] = from_adr
        msg['To'] = to_adr

        html = f"""
                <html>
                <head></head>
                  <body>
                    <p>{self.bot_message}</p>
                    <p>Book here👇👇:</p>
                    <a href="{self.deep_link}">Flight Here</a>
                  </body>
                </html>
                """
        part1 = MIMEText(html, 'html')
        part2 = MIMEText(f"{self.bot_message}")

        msg.attach(part2)
        msg.attach(part1)

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=from_adr, to_addrs=to_adr,
                                msg=msg.as_string().encode("utf-8"))

    def print(self):
        print(self.deep_link)

        # from_adr = "pythontutorial40@gmail.com"
        # to_adr = my_email
        #
        # msg = MIMEMultipart('alternative')
        # msg['Subject'] = "Low Price Flight Alert!"
        # msg['From'] = from_adr
        # msg['To'] = to_adr
        #
        # html = f"""
        # <html>
        # <head></head>
        #   <body>
        #     <p>Link:</p>
        #     <a href="{self.deep_link}">FLight Here</a>
        #   </body>
        # </html>
        # """
        #
        # part1 = MIMEText(html, 'html')
        # part2 = MIMEText(f"{self.bot_message}")
        #
        # msg.attach(part1)
        # msg.attach(part2)
        #
        # s = smtplib.SMTP('localhost')
        # s.sendmail(from_adr, to_adr, msg.as_string())

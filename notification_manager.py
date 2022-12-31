import requests
import smtplib
import os
from flight_data import FlightData
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv("api_details.env")

my_email = os.getenv('my_email')
password = os.getenv('password')


class NotificationManager(FlightData):
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, price, airport_code, city_from, city_to, arrival_airport_code, inbound_date,
                 outbound_date, deep_link, stop_overs, via_city):
        super().__init__(price, airport_code, city_from, city_to, arrival_airport_code, inbound_date,
                         outbound_date, deep_link, stop_overs, via_city)
        self.bot_message = ""

    def flight_message(self):

        """
        This function is used to send a telegram message using a telegram bot
        """

        self.bot_message = (
            f"Low price alert!\nonly ₦{self.price} to fly ✈✈ from {self.departure_city}-{self.departure_airport_code}"
            f" to {self.destination_city}-{self.arrival_airport_code}, "
            f"from {self.outbound_date.split('T')[0]} to {self.inbound_date.split('T')[0]}\n.")

        bot_token = os.getenv('bot_token')
        bot_chatID = os.getenv('bot_chatID')
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='\
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.bot_message
        send_link = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id='\
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.deep_link
        self.print()
        response = requests.get(send_text)
        response1 = requests.get(send_link)

        return response.json()

    def stopover_message(self):

        """
        This function is used to send a telegram message using a telegram bot for flights with stopovers
        """

        self.bot_message = (
            f"Low price alert!\nonly ₦{self.price} to fly ✈✈ from {self.departure_city}-{self.departure_airport_code}"
            f" to {self.destination_city}-{self.arrival_airport_code}, "
            f"from {self.outbound_date.split('T')[0]} to {self.inbound_date.split('T')[0]}. "
            f"Flight has {self.stopover} stop overs,via {self.via_city}\n")

        bot_token = os.getenv('bot_token')
        bot_chatID = os.getenv('bot_chatID')
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + \
                    '&parse_mode=Markdown&text=' + self.bot_message
        send_link = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' \
                    + bot_chatID + '&parse_mode=Markdown&text=' + self.deep_link

        response = requests.get(send_text)
        response1 = requests.get(send_link)

        return response.json()

    def send_emails(self, users):

        """
        This function is used to send emails.
        """

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


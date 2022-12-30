# from __future__ import print_function
#
# import os.path
#
# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError
#
# from google.oauth2 import service_account
#
#
# # Creating Google Sheets Scopes
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# SERVICE_ACCOUNT_FILE = 'keys.json'
#
# credentials = None
# credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#
# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1hGbo9Kmctpew6J8QqxL97lvHssNQyWH2iY8pypM87z8'
#
#
# # Create service and call it
# service = build('sheets', 'v4', credentials=credentials)
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range="sample!A1:B39").execute()
# values = result.get('values', [])
#
# for row in values:
#     print(row)

strtest = """https://www.kiwi.com/deep?affilid=basseygodwinflightsearch&currency=GBP&flightsId=032d10284b870000f1aa7e6b_0%7C1028009f4b874b8b8c1fdda0_0%7C1028009f4b874b8b8c1fdda0_1%7C1028009f4b874b8b8c1fdda0_2%7C1028009f4b874b8b8c1fdda0_3%7C1028032d4b8c0000dd6b8da1_0&from=STN&lang=en&passengers=1&to=DPS&booking_token=E5YOLlia5aCyXqi9iZ_hv2AiEO2y75wZySeSwIk-SDlKMBw00C840LOVMY_CeaCpTyAiKnOSB3hWf4uY-HZcBjKo4Z_P1ZPVRm584vXkz-nMOZ4hK_etJtsEpKM36z11H0s76C0h3YwBL5eV_9MtJYJoDRDEkInpWkqJb4_URckIBylTZOB7xE4w8li10VDV8ZdE0o2MxN3VgEb5CCPsq-z-0ieotU7jxCLPgVnlGPCIJYxEF0lpfK6khGqRvxVVz_--cY4-WxjlLA0ACv0suD78w7VCS5veUFj7HUj8exmJXjzgxFFCt_-mpx1QAKRODUg2NDRlGtC7i8arE2ACgRqpRE5MQ2BRC_K5ItpgE-i8V3qJyIKICSwbPLpnmGTOohyEeUlnR5HCnWGghjTQrHb7_0v3NTYH4qtJKAB6-uW4m6Nv12NCFGpuE9rpioeDtG74-mXhTBLOs_QQrDlCqG0CkmpCvxhlGS8kI4KbY--WQo4-s67qn1RNX01Wh75moRQ4p4JrPd3eL2HGh3wiHjwfLIIem1Wb7fuRa7xmVWrDHvz-o1d8N2-ykKd_A5UomzFDQo-AD5K5q5OAfy3jFcAnOjxJvEGq6IRzQexi2wH7UK-y9K_-cKHKgCXObCCGr9-4IZjylBP0_8yxboqkUYDUoR7b_zaVAqktUHBdV9xUVkgw8VQncpXgWXwfgCftc
https://www.kiwi.com/deep?affilid=basseygodwinflightsearch&currency=GBP&flightsId=22f50a7c4b7d0000ef7d7f9e_0%7C0a7c22f54b8800000a125d5f_0&from=LGW&lang=en&passengers=1&to=ORY&booking_token=ER8ka_NQqO8n4YyU53YY1JT8_M3JNjHZjDu2iEkx3wyDs9n3jPsBeALqkhv_deOBCr222rvgB7NtWLn_90D8aBKxE5-C3cLjI4AFSpJFuppn8fumk2EE2f0evBD7qJoYfrirXsHNWiMi-MdwUFnv5Z1mqRCED4xEsmZXt_f0s1vG7Vp_8KW1g-dv8EIjgjX6nkyUoauCL_7nd61NngEKanWLaCOwJpVRhFlf16_5STE15LDjTqadsdNvx2xr3eRNEDVNmIwYOe0WXQb51cNYmdNNdGaAvH_zal0EEgr75R3SuhhMNrYagb3yvmAg5LgLWssNrQeqcgjFb1KJRoUVmofGC0mc_zPHoK08ZAVnjwO5Q7-NV7CM64FWu5vFxlJqZdYFo3SJluHGIz0OarAeaqt_x1VyZElw54o5Y9jBOxLPSnwpHg-ytLTD0c-3qeNujIV8NMZirKn9-kd9fng7uuRy1bA2ZbGSSJf_mQMOEtpRsi5rWrieBnhliAyFAcpYX"""


print(strtest)



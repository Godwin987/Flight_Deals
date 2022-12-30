from datetime import datetime, timedelta

print(datetime.now().date().strftime("%d/%m/%Y"))

time = datetime.now().date() + timedelta((30*6))
print(time.strftime("%d/%m/%Y"))

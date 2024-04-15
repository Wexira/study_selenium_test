#import datetime
import time
from datetime import timedelta
import datetime

#Текущая дата
now_date = datetime.date.today()
print(now_date.strftime("%m/%d/%y"))

# Для получения будущей даты
future_date = now_date + datetime.timedelta(days=10)
print(future_date.strftime("%m/%d/%y"))

from datetime import date, timedelta
import time

today_form = date.today()
yesterday_form = date.today() - timedelta(1)

today = today_form.strftime('%Y%m%d')
yesterday = yesterday_form.strftime('%Y%m%d')

now = time.localtime()

print(today)
print(yesterday)

print(now.tm_hour)

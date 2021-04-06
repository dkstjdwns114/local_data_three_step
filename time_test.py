import datetime

now = datetime.datetime.now()
print(now)  # 2018-07-28 12:11:32.669083

nowDate = now.strftime('%Y-%m-%d')
print(nowDate)  # 2018-07-28

nowTime = now.strftime('%H:%M:%S')
print(nowTime)  # 12:11:32

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print(nowDatetime)  # 2018-07-28 12:11:32

nowHour = now.strftime('%H')

print(nowHour)
